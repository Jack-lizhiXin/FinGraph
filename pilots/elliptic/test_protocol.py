"""Offline regression check. All CSVs are temporary, hand-constructed fixtures."""

import csv
import json
import math
import tempfile
import unittest
from pathlib import Path

from run import FILES, MODELS, run, write_csv


def fixture(folder):
    folder.mkdir()
    nodes = [(1, 1, "2"), (2, 1, "2"), (3, 1, "1"), (4, 1, "unknown"), (5, 1, "2"),
             (10, 31, "1"), (11, 31, "2"), (12, 31, "unknown")]
    for idx in range(25):
        label = "1" if idx in {0, 24} else "2" if idx <= 8 else "unknown"
        nodes.append((4001 + idx, 40, label))
    nodes.extend([(4101, 41, "2"), (4102, 41, "unknown"), (4901, 49, "unknown")])
    # Reverse input row order to exercise ID alignment and explicit tie-breaking.
    with (folder / FILES["nodes"]).open("w", newline="") as stream:
        csv.writer(stream).writerows((n, t, 99) for n, t, _ in reversed(nodes))
    write_csv(folder / FILES["labels"], ["txId", "class"], ((n, label) for n, _, label in nodes))
    write_csv(folder / FILES["edges"], ["txId1", "txId2"],
              [(1, 2), (1, 3), (2, 3), (1, 3), (3, 5), (10, 11), (4101, 4102)])


def rows(folder, name):
    with (folder / name).open(newline="") as stream:
        return list(csv.DictReader(stream))


class ProtocolTests(unittest.TestCase):
    def test_windows_labels_alerts_and_direction(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            src, out = root / "fixture", root / "result"
            fixture(src)
            run(src, out, MODELS)
            with self.assertRaises(FileExistsError):
                run(src, out, MODELS)

            manifest = json.loads((out / "manifest.json").read_text())
            self.assertEqual(manifest["fit_counts"], {"supervised": 4, "normal-only": 3})
            self.assertEqual(manifest["duplicate_edges_collapsed"], 1)
            self.assertEqual(len(manifest["input_sha256"]), 3)
            self.assertEqual(len(rows(out, "step_counts.csv")), 49)
            masks = {int(row["txId"]): row for row in rows(out, "masks_features.csv")}
            self.assertAlmostEqual(float(masks[3]["log_in_degree"]), math.log(3))
            self.assertAlmostEqual(float(masks[3]["mean_predecessor_log_in_degree"]), math.log(2) / 2)
            self.assertEqual(masks[4]["eligible_supervised_fit"], "0")
            self.assertEqual(masks[10]["eligible_supervised_fit"], "0")
            results = {(r["model"], r["step"]): r for r in rows(out, "metrics.csv")}
            for model in MODELS:
                metric = results[model, "40"]
                self.assertAlmostEqual(float(metric["known_ap"]), 0.2)
                self.assertEqual((metric["all_illicit"], metric["all_licit"], metric["all_unknown"]),
                                 ("1", "8", "11"))
                self.assertAlmostEqual(float(metric["all_lower"]), 0.05)
                self.assertAlmostEqual(float(metric["all_upper"]), 0.60)
                self.assertAlmostEqual(float(metric["all_label_coverage"]), 0.45)
                self.assertEqual(results[model, "41"]["known_ap"], "")
                self.assertEqual(results[model, "42"]["all_k"], "0")
                self.assertEqual(results[model, "49"]["all_precision_among_labeled"], "")
                self.assertEqual(results[model, "pooled"]["all_k"], "23")

            baseline_scores = {(r["model"], r["txId"]): r["score"] for r in rows(out, "scores.csv")}
            self.assertEqual(len(baseline_scores), 56)
            # Add a downstream transaction to step 40 and change an existing held-out label.
            with (src / FILES["nodes"]).open("a") as f:
                f.write("4099,40,999999\n")
            with (src / FILES["edges"]).open("a") as f:
                f.write("4001,4099\n")
            labels = rows(src, FILES["labels"])
            for row in labels:
                if row["txId"] == "4001":
                    row["class"] = "2"
            labels.append({"txId": "4099", "class": "unknown"})
            with (src / FILES["labels"]).open("w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=["txId", "class"])
                writer.writeheader()
                writer.writerows(labels)
            for model in MODELS:
                second = root / model
                run(src, second, (model,))
                for row in rows(second, "scores.csv"):
                    if row["txId"] != "4099":
                        self.assertEqual(row["score"], baseline_scores[model, row["txId"]])


if __name__ == "__main__":
    unittest.main()
