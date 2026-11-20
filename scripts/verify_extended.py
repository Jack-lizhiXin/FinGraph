#!/usr/bin/env python3
"""Check the local resource catalog, import history and Markdown links."""

import csv
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

from catalog import ROOT, SOURCE, subbranch_code, validate

DATASET_COLUMNS = (
    "id", "name", "provenance", "graph_construction", "label_semantics", "target_granularity",
    "scale", "access", "license", "leakage_and_limits", "official_url", "primary_paper_or_code",
    "verified_on",
)
PAPER_INDEX = ROOT / "catalog/README.md"
LINK = re.compile(r"\[[^\]]*\]\((?:<([^>]+)>|([^)]+))\)")
ANCHOR = re.compile(r'<a id="([^"]+)"></a>')


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def check_datasets():
    records = read_json(ROOT / "datasets/index.json")
    if not isinstance(records, list) or not records:
        raise ValueError("datasets/index.json 应包含数据资源列表")
    ids = set()
    for record in records:
        for field in DATASET_COLUMNS:
            if not isinstance(record.get(field), str) or not record[field].strip():
                raise ValueError(f"数据资源 {record.get('id')} 缺少 {field}")
        key = record["id"]
        if key in ids:
            raise ValueError(f"数据资源 ID 重复：{key}")
        ids.add(key)
        source = urlsplit(record["official_url"])
        if source.scheme != "https" or not source.hostname or record.get("redistributed") is not False:
            raise ValueError(f"请核对 {key} 的官方来源和原始数据分发标记")
    with (ROOT / "datasets/index.csv").open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != list(DATASET_COLUMNS):
            raise ValueError("datasets/index.csv 的列名或顺序与索引格式不符")
        expected = [{column: record[column] for column in DATASET_COLUMNS} for record in records]
        if list(reader) != expected:
            raise ValueError("datasets/index.csv 与 datasets/index.json 的内容或顺序不同")
    return len(records)


def check_import_history(paper_ids):
    history = read_json(ROOT / "research/new-additions-2026-11-20.json")
    new = set(history["new_ids"])
    if (len(new) != len(history["new_ids"]) or len(new) != history["new_count"]
            or not new.issubset(paper_ids)):
        raise ValueError("首轮增补记录的论文 ID 或数量与书目不符")
    merge = history["package_merge"]
    recovered = set(merge["startup_only_ids"])
    if (not recovered.issubset(paper_ids) or recovered.intersection(new)
            or len(recovered) != len(merge["startup_only_ids"])
            or merge["startup_count"] != merge["common_count"] + len(recovered)
            or merge["expansion_count"] != history["baseline_count"] + len(new)
            or merge["total_count"] != merge["expansion_count"] + len(recovered)
            or merge["total_count"] > len(paper_ids)):
        raise ValueError("附件合并记录的论文 ID 或数量关系不一致")
    return len(new)


def check_papers(papers):
    validate(papers)
    dois = set()
    for paper in papers:
        source = urlsplit(paper["url"])
        if source.hostname in {"doi.org", "dx.doi.org"}:
            doi = unquote(source.path).strip("/").casefold()
            if doi in dois:
                raise ValueError(f"重复 DOI：{doi}")
            dois.add(doi)
    branches = {subbranch_code(paper["branch"]) for paper in papers}
    tree = (ROOT / "docs/tree.md").read_text(encoding="utf-8")
    tree_branches = set(re.findall(r"\.\./catalog/README\.md#branch-([a-z]+[0-9]+)\)", tree))
    if branches != tree_branches:
        raise ValueError("docs/tree.md 的分支编号与书目使用的分支不同")
    return len(branches)


def check_links():
    anchors = set(ANCHOR.findall(PAPER_INDEX.read_text(encoding="utf-8")))
    count = 0
    for source in ROOT.rglob("*.md"):
        for match in LINK.finditer(source.read_text(encoding="utf-8")):
            raw = match.group(1) or match.group(2)
            url = urlsplit(raw)
            if url.scheme or url.netloc:
                continue
            target = (source.parent / unquote(url.path)).resolve() if url.path else source
            if not target.exists():
                raise ValueError(f"{source.relative_to(ROOT)} 的本地链接不存在：{raw}")
            if (target == PAPER_INDEX and url.fragment.startswith(("p-", "branch-"))
                    and unquote(url.fragment) not in anchors):
                raise ValueError(f"{source.relative_to(ROOT)} 指向不存在的论文或分支：{raw}")
            if url.path:
                count += 1
    return count


def main():
    papers = read_json(SOURCE)
    branches = check_papers(papers)
    imported = check_import_history({paper["id"] for paper in papers})
    datasets = check_datasets()
    links = check_links()
    print(f"PASS: {len(papers)} papers, {imported} in the first expansion, "
          f"{branches} leaves, {datasets} datasets, {links} internal relative links")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, OSError) as error:
        sys.exit(f"校验失败：{error}")
