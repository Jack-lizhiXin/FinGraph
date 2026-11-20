#!/usr/bin/env python3
"""核查 FinGraph 书目，生成 GitHub 上可读的论文索引。"""

import argparse
import csv
import html
import io
import json
import re
import sys
import unicodedata
from collections import defaultdict
from datetime import date
from pathlib import Path
from urllib.parse import quote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "catalog" / "papers.json"
INDEX = SOURCE.with_name("README.md")
CSV_INDEX = SOURCE.with_suffix(".csv")
CSV_FIELDS = (
    "id", "title", "authors", "venue", "year", "track", "branch", "role",
    "supervision", "object", "domain", "url", "code", "reading", "model",
    "note", "evidence_locator", "source_verified_on", "verification_level",
)
FIELDS = ("id", "title", "venue", "branch", "role", "supervision", "object", "domain", "note", "url")
LOCAL_LINKS = {"model": ("models", "模型卡"), "reading": ("notes", "精读卡")}


def normalized_title(title):
    return "".join(c for c in unicodedata.normalize("NFKC", title).casefold() if c.isalnum())


def clean_text(value):
    return isinstance(value, str) and bool(value.strip()) and value == value.strip() and len(value.splitlines()) == 1


def subbranch_code(branch):
    child = branch.partition(" / ")[2]
    match = re.match(r"([A-Z]+[0-9]+)\s", child)
    return match.group(1).lower() if match else None


def validate(records):
    if not isinstance(records, list):
        raise ValueError("papers.json 顶层应为数组")
    seen = {"id": set(), "title": set(), "url": set()}
    branch_names = {}
    for position, paper in enumerate(records, 1):
        if not isinstance(paper, dict):
            raise ValueError(f"第 {position} 条应为对象")
        label = paper.get("id", f"第 {position} 条")
        for field in FIELDS:
            if not clean_text(paper.get(field)):
                raise ValueError(f"{label} 的 {field} 需要单行非空文本，请移除首尾空白")
        branch = paper["branch"]
        code = subbranch_code(branch)
        if code and branch_names.setdefault(code, branch) != branch:
            raise ValueError(f"{label} 的二级分支编号 {code.upper()} 对应了两个名称，请核对论文树")
        aliases = paper.get("aliases", [])
        if not isinstance(aliases, list):
            raise ValueError(f"{label} 的 aliases 应为旧 ID 列表")
        for key in [label, *aliases]:
            if not isinstance(key, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", key):
                raise ValueError(f"{label} 的 ID 或别名格式错误")
            if key in seen["id"]:
                raise ValueError(f"{label} 的 ID 或别名 {key} 重复")
            seen["id"].add(key)
        year = paper.get("year")
        if type(year) is not int or not 1900 <= year <= date.today().year + 1:
            raise ValueError(f"{label} 的 year 需要合理的四位整数")
        for field in ("url", "code"):
            if field not in paper:
                continue
            value = paper[field]
            if not clean_text(value) or any(c.isspace() or c in '<>' for c in value):
                raise ValueError(f"{label} 的 {field} 需要有效的 HTTPS 链接")
            parsed = urlsplit(value)
            if parsed.scheme != "https" or not parsed.hostname:
                raise ValueError(f"{label} 的 {field} 需要有效的 HTTPS 链接")
        for key, value in (("title", normalized_title(paper["title"])),
                           ("url", paper["url"].rstrip("/"))):
            if value in seen[key]:
                raise ValueError(f"{label} 的 {key} 重复，请更新已有条目")
            seen[key].add(value)
        if "authors" in paper and not clean_text(paper["authors"]):
            raise ValueError(f"{label} 的 authors 需要单行非空文本")
        tags = paper.get("tags", [])
        if not isinstance(tags, list) or not all(clean_text(tag) for tag in tags):
            raise ValueError(f"{label} 的 tags 应为字符串数组")
        for field, (folder, _) in LOCAL_LINKS.items():
            if field not in paper:
                continue
            raw = paper[field]
            if not clean_text(raw) or Path(raw).is_absolute():
                raise ValueError(f"{label} 的 {field} 需要仓库相对路径")
            target = (ROOT / raw).resolve()
            if ((ROOT / folder) not in target.parents or target.suffix != ".md"
                    or not target.is_file()):
                raise ValueError(f"{label} 的 {field} 应指向 {folder} 目录内已有的 Markdown 文件")


def md(text):
    text = html.escape(text, quote=False)
    return re.sub(r"([\\|\[\]*_~`])", r"\\\1", text)


def render(records):
    groups = defaultdict(list)
    for paper in records:
        groups[paper["branch"]].append(paper)
    lines = [
        "# FinGraph 论文索引", "",
        f"共 {len(records)} 篇。按主分支浏览，论文只收录一次。"
        "点英文题名进入原始来源，每篇附有选读理由。", "",
        "[首页](../README.md) · [贡献说明](../CONTRIBUTING.md) · [JSON](papers.json) · [CSV](papers.csv)", "",
        "## 分支导航", ""
    ]
    body = []
    last_parent = None
    for number, branch in enumerate(sorted(groups), 1):
        parent, separator, child = branch.partition(" / ")
        if separator and parent != last_parent:
            lines.append(f"- **{md(parent)}**")
            body += ["", f"## {md(parent)}"]
        last_parent = parent
        heading = md(child if separator else parent)
        indent = "  " if separator else ""
        depth = "###" if separator else "##"
        lines.append(f"{indent}- [{heading}](#branch-{number})（{len(groups[branch])} 篇）")
        anchors = [f'<a id="branch-{number}"></a>']
        code = subbranch_code(branch)
        if code:
            anchors.append(f'<a id="branch-{code}"></a>')
        body += ["", *anchors, "", f"{depth} {heading}", "",
                 "| 论文与出处 | 标签条件、对象与场景 | 选读理由及材料 |", "| --- | --- | --- |"]
        for paper in sorted(groups[branch], key=lambda p: (-p["year"], p["title"].casefold())):
            title = f'[{md(paper["title"])}](<{paper["url"]}>)'
            source = f'{md(paper["venue"])} {paper["year"]} · {md(paper["role"])}'
            if paper.get("authors"):
                source += " · " + md(paper["authors"])
            context = " · ".join(md(paper[k]) for k in ("supervision", "object", "domain"))
            context_tags = "、".join(md(tag) for tag in paper.get("tags", []))
            if context_tags:
                context += "<br>" + context_tags
            materials = []
            if paper.get("code"):
                materials.append(f'[代码](<{paper["code"]}>)')
            for field, (_, text) in LOCAL_LINKS.items():
                if field in paper:
                    materials.append(f'[{text}](../{quote(paper[field])})')
            annotation = md(paper["note"])
            if materials:
                annotation += "<br>" + " · ".join(materials)
            ids = [paper["id"], *paper.get("aliases", [])]
            paper_anchors = "".join(f'<a id="p-{key}"></a>' for key in ids)
            body.append(f'| {paper_anchors}{title}<br>{source}<br><code>{paper["id"]}</code> | {context} | {annotation} |')
    return "\n".join(lines + body) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--check", action="store_true", help="只读校验字段、去重、本地卡片链接与索引一致性")
    modes.add_argument("--find", nargs="+", metavar="关键词", help="查找同时包含这些关键词的条目")
    args = parser.parse_args()
    try:
        records = json.loads(SOURCE.read_text(encoding="utf-8"))
        validate(records)
        if args.find:
            for paper in records:
                fields = json.dumps(paper, ensure_ascii=False).casefold()
                if all(term.casefold() in fields for term in args.find):
                    print(f'{paper["id"]} | {paper["title"]} | {paper["venue"]} {paper["year"]}')
            return 0
        csv_output = io.StringIO(newline="")
        writer = csv.DictWriter(csv_output, fieldnames=CSV_FIELDS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(records)
        outputs = {
            INDEX: render(records).encode("utf-8"),
            CSV_INDEX: csv_output.getvalue().encode("utf-8-sig"),
        }
        for path, content in outputs.items():
            if args.check:
                expected = content.decode("utf-8").replace("\r\n", "\n")
                if not path.is_file() or path.read_text(encoding="utf-8") != expected:
                    raise ValueError(f"{path.name} 未同步，请运行 python3 scripts/catalog.py 后提交索引")
            else:
                path.write_bytes(content)
    except (OSError, ValueError, TypeError) as error:
        print(f"书目校验失败：{error}", file=sys.stderr)
        return 1
    print(f"通过，书目共 {len(records)} 条。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
