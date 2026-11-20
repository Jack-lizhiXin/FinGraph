"""Static, transductive node-ranking example. Requires Python 3.8+ only."""

import argparse
import csv
import itertools
import math
from pathlib import Path
from statistics import mean, pstdev


HERE = Path(__file__).resolve().parent


def read_nodes(path):
    features, splits, labels, normal_seeds = {}, {}, {}, []
    with path.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            node = row["node_id"].strip()
            split, label, seed = row["split"], row["label"], row["normal_seed"]
            if not node or node in features:
                raise ValueError(f"invalid or duplicate node_id: {node!r}")
            if split not in {"train", "test", "unlabeled"}:
                raise ValueError(f"{node}: invalid split")
            if label not in ({"0", "1"} if split in {"train", "test"} else {""}):
                raise ValueError(f"{node}: label incompatible with split")
            if seed not in {"0", "1"} or (seed == "1" and (split, label) != ("train", "0")):
                raise ValueError(f"{node}: normal seeds must be labeled training normals")
            activity, night = float(row["activity_index"]), float(row["night_share"])
            if not math.isfinite(activity) or activity < 0 or not 0 <= night <= 1:
                raise ValueError(f"{node}: invalid activity_index or night_share")
            features[node] = (activity, night)
            splits[node] = split
            if label:
                labels[node] = int(label)
            if seed == "1":
                normal_seeds.append(node)
    return features, splits, labels, normal_seeds


def one_hop_features(features, path):
    neighbors = {node: set() for node in features}
    with path.open(encoding="utf-8-sig", newline="") as handle:
        for edge in csv.DictReader(handle):
            a, b = edge["source"].strip(), edge["target"].strip()
            if a not in neighbors or b not in neighbors or a == b or b in neighbors[a]:
                raise ValueError(f"unknown endpoint, self-loop or duplicate edge: {a}, {b}")
            neighbors[a].add(b)
            neighbors[b].add(a)

    augmented = {}
    for node, own in features.items():
        rows = [features[n] for n in sorted(neighbors[node])]
        neighborhood = tuple(map(mean, zip(*rows))) if rows else own
        augmented[node] = own + neighborhood
    return augmented


def center_and_scale(rows):
    columns = list(zip(*rows))
    return tuple(map(mean, columns)), tuple(pstdev(col) or 1.0 for col in columns)


def squared_distance(row, center, scale):
    return sum(((value - middle) / unit) ** 2 for value, middle, unit in zip(row, center, scale))


def supervised_scores(features, train_labels, test_nodes):
    rows = [features[n] for n in train_labels]
    _, scale = center_and_scale(rows)
    centers = []
    for label in (0, 1):
        class_rows = [features[n] for n, observed in train_labels.items() if observed == label]
        centers.append(tuple(map(mean, zip(*class_rows))))
    result = []
    for node in test_nodes:
        normal = squared_distance(features[node], centers[0], scale)
        anomaly = squared_distance(features[node], centers[1], scale)
        result.append(normal - anomaly)
    return result


def normal_only_scores(features, normal_seeds, test_nodes):
    # This branch accepts only the IDs of known normal nodes. It never receives a two-class label map.
    center, scale = center_and_scale([features[n] for n in normal_seeds])
    return [squared_distance(features[n], center, scale) for n in test_nodes]


def ranking_metrics(scores, observed, k):
    """Non-interpolated AP by threshold, and expected precision@k if the boundary is tied."""
    ranked = sorted(zip(scores, observed), key=lambda item: item[0], reverse=True)
    positives = sum(observed)
    seen, hits, ap, expected_top_hits = 0, 0, 0.0, 0.0
    for _, tied in itertools.groupby(ranked, key=lambda item: item[0]):
        group = [label for _, label in tied]
        count, added = len(group), sum(group)
        slots = max(0, min(count, k - seen))
        expected_top_hits += slots * added / count
        seen += count
        hits += added
        ap += (added / positives) * (hits / seen)
    return ap, expected_top_hits / k


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--nodes", type=Path, default=HERE / "nodes.csv")
    parser.add_argument("--edges", type=Path, default=HERE / "edges.csv")
    parser.add_argument("--top-k", type=int, default=3)
    args = parser.parse_args()
    try:
        own, splits, labels, normal_seeds = read_nodes(args.nodes)
        graph = one_hop_features(own, args.edges)
        train_labels = {n: labels[n] for n in own if splits[n] == "train"}
        test = [n for n in own if splits[n] == "test"]
        observed = [labels[n] for n in test]
        if set(train_labels.values()) != {0, 1} or set(observed) != {0, 1}:
            raise ValueError("train and test must each contain both classes")
        if not normal_seeds or not 1 <= args.top_k <= len(test):
            raise ValueError("need a normal seed and top-k between 1 and the test set size")
        methods = [
            ("supervised / own", supervised_scores(own, train_labels, test)),
            ("supervised / own + neighbor mean", supervised_scores(graph, train_labels, test)),
            ("normal-only / own + neighbor mean", normal_only_scores(graph, normal_seeds, test)),
        ]
        print(f"Nodes={len(own)}  two-class labels={len(train_labels)}  normal-only labels={len(normal_seeds)}")
        print(f"Test={len(test)}  positives={sum(observed)}  prevalence={sum(observed) / len(test):.3f}")
        print(f"{'Method':36} {'AP':>7}  {'P@' + str(args.top_k):>7}")
        for name, scores in methods:
            ap, precision = ranking_metrics(scores, observed, args.top_k)
            print(f"{name:36} {ap:7.3f}  {precision:7.3f}")
    except (OSError, KeyError, ValueError) as error:
        parser.exit(2, f"Input error: {error}\n")


if __name__ == "__main__":
    main()
