"""Run the FinGraph v1 Elliptic transaction-node pilot on locally supplied original CSVs."""

import argparse
from collections import Counter
import csv
import hashlib
import json
import math
import platform
from pathlib import Path
from warnings import catch_warnings, simplefilter

import numpy as np
import sklearn
from sklearn.exceptions import ConvergenceWarning
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score
from sklearn.preprocessing import StandardScaler


FILES = {
    "nodes": "elliptic_txs_features.csv",
    "edges": "elliptic_txs_edgelist.csv",
    "labels": "elliptic_txs_classes.csv",
}
MODELS = ("supervised", "normal-only")
K = 20
PROTOCOL = "FinGraph-Elliptic-upstream-v1"


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def txid(value):
    if not value.isascii() or not value.isdecimal() or str(int(value)) != value:
        raise ValueError(f"expected a canonical nonnegative integer transaction ID, found {value!r}")
    return int(value)


def read_steps(path):
    steps = {}
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        for row in reader:
            if len(row) < 2:
                raise ValueError(f"{path.name}:{reader.line_num}: missing transaction ID or time step")
            key = txid(row[0])
            step = int(row[1])
            if key in steps or step not in range(1, 50):
                raise ValueError(f"{path.name}:{reader.line_num}: duplicate ID or invalid time step")
            steps[key] = step
    if not steps:
        raise ValueError("empty feature file")
    return steps


def named_rows(path, header):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        if next(reader, []) != header:
            raise ValueError(f"{path.name}: expected header {header}")
        for row in reader:
            if len(row) != len(header):
                raise ValueError(f"{path.name}:{reader.line_num}: unexpected number of fields")
            yield row


def read_labels(path, steps):
    labels = {}
    for ident, value in named_rows(path, ["txId", "class"]):
        key = txid(ident)
        if key in labels or key not in steps or value not in {"1", "2", "unknown"}:
            raise ValueError(f"duplicate, unmatched or invalid class record for {ident}")
        labels[key] = value
    if len(labels) != len(steps):
        raise ValueError("classes CSV must explicitly cover every transaction ID, including unknowns")
    return labels


def compute_features(path, steps, ids):
    # Only incoming unique predecessors affect a target's features.
    predecessors = {}
    duplicates = 0
    for source, target in named_rows(path, ["txId1", "txId2"]):
        source, target = txid(source), txid(target)
        if source not in steps or target not in steps or source == target:
            raise ValueError(f"invalid endpoints {source}, {target}")
        if steps[source] != steps[target]:
            raise ValueError(f"edge crosses release time steps: {source}, {target}")
        neighbors = predecessors.setdefault(target, set())
        if source in neighbors:
            duplicates += 1
        neighbors.add(source)

    log_degrees = {i: math.log1p(len(neighbors)) for i, neighbors in predecessors.items()}
    features = np.zeros((len(ids), 2), dtype=np.float64)
    for idx, node in enumerate(ids):
        previous = predecessors.get(node)
        if previous:
            features[idx] = (
                log_degrees[node],
                math.fsum(log_degrees.get(i, 0.0) for i in previous) / len(previous),
            )
    return features, duplicates


def fit_supervised(x_fit, y_fit, x_test):
    if set(y_fit) != {0, 1}:
        raise ValueError("supervised training requires both licit and illicit training labels")
    scaler = StandardScaler().fit(x_fit)
    clf = LogisticRegression(C=1.0, solver="lbfgs", max_iter=1000, tol=1e-8, random_state=0)
    with catch_warnings():
        simplefilter("error", ConvergenceWarning)
        clf.fit(scaler.transform(x_fit), y_fit)
    scores = clf.predict_proba(scaler.transform(x_test))[:, int(np.flatnonzero(clf.classes_ == 1)[0])]
    params = {
        "method": "StandardScaler + L2 logistic regression; illicit=1",
        "estimator": clf.get_params(), "scaler_mean": scaler.mean_.tolist(),
        "scaler_scale": scaler.scale_.tolist(), "coef": clf.coef_.tolist(),
        "intercept": clf.intercept_.tolist(), "iterations": clf.n_iter_.tolist(),
    }
    return scores, params


def fit_normal_only(x_normal, x_test):
    if len(x_normal) == 0:
        raise ValueError("normal-only training requires a nonempty fixed licit training set")
    center = np.median(x_normal, axis=0)
    mad = np.median(np.abs(x_normal - center), axis=0)
    scores = np.max(np.abs(x_test - center) / np.maximum(mad, 0.1), axis=1)
    return scores, {"method": "maximum scaled absolute deviation", "center": center.tolist(),
                    "raw_mad": mad.tolist(), "mad_floor": 0.1}


def split(step):
    if step <= 30:
        return "train"
    if step <= 39:
        return "validation"
    return "test"


def ratio(a, b):
    return a / b if b else None


def measure(step, rows, known_alerts, all_alerts):
    # rows and both queues contain (ID, score, released class).
    known = [r for r in rows if r[2] != "unknown"]
    count = Counter(r[2] for r in known)
    ap = None
    if count["1"]:
        ap = float(average_precision_score([r[2] == "1" for r in known], [r[1] for r in known]))
    k_known, k_all = len(known_alerts), len(all_alerts)
    hits_known = sum(r[2] == "1" for r in known_alerts)
    p, l, u = (sum(r[2] == value for r in all_alerts) for value in ("1", "2", "unknown"))
    return {
        "step": step, "n_all": len(rows), "n_illicit": count["1"], "n_licit": count["2"],
        "n_unknown": len(rows)-len(known), "known_ap": ap,
        "ap_status": "ok" if ap is not None else "no_known_positive",
        "known_k": k_known, "known_hits": hits_known, "known_precision": ratio(hits_known, k_known),
        "all_k": k_all, "all_illicit": p, "all_licit": l, "all_unknown": u,
        "all_lower": ratio(p, k_all), "all_upper": ratio(p + u, k_all),
        "all_label_coverage": ratio(p + l, k_all), "all_precision_among_labeled": ratio(p, p + l),
    }


def evaluate(model, predictions, steps, labels):
    all_rows, all_known_alerts, all_alerts, metrics, alerts = [], [], [], [], []
    buckets = {t: [] for t in range(40, 50)}
    for node, score in predictions:
        buckets[steps[node]].append((node, score, labels[node]))
    for step, bucket in buckets.items():
        rows = sorted(bucket, key=lambda r: (-r[1], r[0]))
        known_top = [r for r in rows if r[2] != "unknown"][:K]
        full_top = rows[:K]
        metrics.append({"model": model, **measure(step, rows, known_top, full_top)})
        for pool, queue in (("known", known_top), ("all", full_top)):
            for rank, (node, score, label) in enumerate(queue, 1):
                alerts.append((model, step, pool, rank, node, score, label))
        all_rows.extend(rows)
        all_known_alerts.extend(known_top)
        all_alerts.extend(full_top)
    metrics.append({"model": model, **measure("pooled", all_rows, all_known_alerts, all_alerts)})
    return metrics, alerts


def write_csv(path, fields, rows):
    with path.open("x", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(fields)
        writer.writerows(rows)


def write_json(path, obj):
    with path.open("x", encoding="utf-8") as handle:
        json.dump(obj, handle, ensure_ascii=False, indent=2, allow_nan=False)
        handle.write("\n")


def run(data, out, models):
    paths = {key: data / name for key, name in FILES.items()}
    if out.exists():
        raise FileExistsError(f"choose a new output directory: {out}")
    source_hashes = {p.name: sha256(p) for p in paths.values()}
    steps = read_steps(paths["nodes"])
    ids = sorted(steps, key=lambda i: (steps[i], i))
    labels = read_labels(paths["labels"], steps)
    features, duplicates = compute_features(paths["edges"], steps, ids)
    train = np.array([steps[i] <= 30 for i in ids])
    test = np.array([steps[i] >= 40 for i in ids])
    if not test.any():
        raise ValueError("missing test transactions in steps 40 through 49")
    supervised_mask = train & np.array([labels[i] != "unknown" for i in ids])
    normal_mask = train & np.array([labels[i] == "2" for i in ids])
    test_ids = [i for i in ids if steps[i] >= 40]
    metrics, alerts, prediction_rows, fitted = [], [], [], {}
    for model in models:
        if model == "supervised":
            y_fit = np.array([int(labels[i] == "1") for i, use in zip(ids, supervised_mask) if use])
            scores, params = fit_supervised(features[supervised_mask], y_fit, features[test])
        else:
            scores, params = fit_normal_only(features[normal_mask], features[test])
        if not np.isfinite(scores).all():
            raise ValueError(f"non-finite scores: {model}")
        fitted[model] = params
        pairs = list(zip(test_ids, scores.tolist()))
        prediction_rows.extend((model, i, steps[i], s) for i, s in pairs)
        model_metrics, model_alerts = evaluate(model, pairs, steps, labels)
        metrics.extend(model_metrics)
        alerts.extend(model_alerts)

    counts = {t: Counter() for t in range(1, 50)}
    for j, i in enumerate(ids):
        counter = counts[steps[i]]
        counter[labels[i]] += 1
        counter["total"] += 1
        counter["no_predecessor"] += int(features[j, 0] == 0)
    out.mkdir(parents=True, exist_ok=False)
    write_csv(out / "step_counts.csv",
              ("step", "split", "n", "illicit", "licit", "unknown", "no_predecessor", "no_predecessor_share"),
              ((t, split(t), c["total"], c["1"], c["2"], c["unknown"], c["no_predecessor"],
                ratio(c["no_predecessor"], c["total"])) for t, c in counts.items()))
    write_csv(out / "masks_features.csv",
              ("txId", "step", "split", "evaluation_known", "eligible_supervised_fit", "eligible_normal_fit",
               "log_in_degree", "mean_predecessor_log_in_degree"),
              ((i, steps[i], split(steps[i]), int(labels[i] != "unknown"), int(supervised_mask[j]),
                int(normal_mask[j]), *features[j]) for j, i in enumerate(ids)))
    write_csv(out / "scores.csv", ("model", "txId", "step", "score"), prediction_rows)
    write_csv(out / "alerts.csv", ("model", "step", "pool", "rank", "txId", "score", "class"), alerts)
    write_csv(out / "metrics.csv", metrics[0].keys(), (row.values() for row in metrics))
    write_json(out / "models.json", fitted)
    outputs = {p.name: sha256(p) for p in sorted(out.iterdir()) if p.is_file()}
    write_json(out / "manifest.json", {
        "protocol": PROTOCOL, "input_sha256": source_hashes, "output_sha256": outputs,
        "source_url": "https://www.kaggle.com/datasets/ellipticco/elliptic-data-set",
        "script_sha256": sha256(Path(__file__)), "python": platform.python_version(),
        "numpy": np.__version__, "scikit_learn": sklearn.__version__, "models": list(models),
        "windows": {"train": [1, 30], "validation": [31, 39], "test": [40, 49]},
        "validation_use": "counts only; both models fixed in advance; no threshold selected",
        "duplicate_edges_collapsed": duplicates, "mask_version": "v1",
        "features": ["log1p(unique incoming degree)", "mean log1p(incoming degree of each predecessor)"],
        "top_k_per_step": K, "tie_break": "ascending numeric transaction ID",
        "fit_counts": {m: int((supervised_mask if m == "supervised" else normal_mask).sum()) for m in models},
    })
    print(f"{PROTOCOL}: {len(ids)} nodes, {len(test_ids)} test nodes, {len(models)} model(s).")
    print(f"Complete: {out / 'manifest.json'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, required=True, help="directory containing the three original CSVs")
    parser.add_argument("--output", type=Path, required=True, help="new directory for this run")
    parser.add_argument("--model", choices=("both", *MODELS), default="both")
    args = parser.parse_args()
    try:
        run(args.data, args.output, MODELS if args.model == "both" else (args.model,))
    except (ValueError, OSError, ConvergenceWarning) as exc:
        parser.exit(2, f"Run failed: {exc}\n")
