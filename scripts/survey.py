#!/usr/bin/env python3
"""Render the dated review cohort and evidence matrix from the shared catalogue."""

import argparse
import csv
import io
import json
from collections import Counter, defaultdict
from datetime import date

from catalog import ROOT, SOURCE, md, validate

REVIEW = ROOT / 'survey'
DETAILS = ('method', 'time', 'finance', 'limit', 'why_core')
CORE_FIELDS = ('id', 'year', 'title', 'venue', 'track', 'object', 'supervision', *DETAILS,
               'verification_level', 'evidence_locator', 'url', 'reading')
CANDIDATE_FIELDS = ('id', 'year', 'title', 'venue', 'track', 'role', 'branch', 'core',
                    'verification_level', 'evidence_locator', 'url', 'reading')


def csv_content(rows, fields):
    stream = io.StringIO(newline='')
    writer = csv.DictWriter(stream, fieldnames=fields, extrasaction='ignore', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue()


def source_row(paper):
    review = paper.get('review', {})
    row = {**paper, **review}
    row['track'] = review.get('track', '前期书目')
    row['core'] = '是' if review.get('why_core') else '否'
    row['verification_level'] = paper.get('verification_level', '前期收录，正文定位待补')
    if row['core'] == '是':
        for field in (*DETAILS, 'track', 'evidence_locator'):
            if not isinstance(row.get(field), str) or not row[field].strip():
                raise ValueError(f"核心条目 {paper['id']} 缺少 {field}")
    return row


def render(papers):
    scope = json.loads((REVIEW / 'scope.json').read_text(encoding='utf-8'))
    cutoff = date.fromisoformat(scope['searched_through'])
    cohort = set(scope['paper_ids'])
    by_id = {p['id']: p for p in papers}
    if len(cohort) != len(scope['paper_ids']) or not cohort.issubset(by_id):
        raise ValueError('专题名单含重复或无书目记录的 ID')
    if any(not scope['first_year'] <= by_id[key]['year'] <= cutoff.year for key in cohort):
        raise ValueError('专题名单中的发表年份超出检索窗口')
    eligible = sorted((source_row(by_id[key]) for key in cohort),
                      key=lambda p: (p['track'], -p['year'], p['id']))
    core = [p for p in eligible if p['core'] == '是']
    groups = defaultdict(list)
    for p in core:
        groups[p['track']].append(p)
    lines = ['# 核心文献方法与证据矩阵', '',
             f'检索截至 {cutoff.isoformat()}。{len(eligible)} 篇近五年候选中，{len(core)} 篇已写明入选理由、方法、时间信息、金融证据及限制。主题分组标明每篇承担的综述角色。', '',
             '[可筛选的完整矩阵](core-matrix.csv) · [全部近五年候选](candidates.csv) · [跨论文评测例解](evaluation-crosswalk.md) · [筛选口径](protocol.md)', '']
    for track, rows in groups.items():
        lines += [f'## {md(track)}（{len(rows)} 篇）', '',
                  '| 原文与证据位置 | 评分对象与监督 | 方法与时间协议 | 金融证据和比较限制 | 核心纳入理由 |',
                  '| --- | --- | --- | --- | --- |']
        for p in rows:
            source = f"[{md(p['title'])}](<{p['url']}>)（{p['year']}）<br>{md(p['verification_level'])} · {md(p['evidence_locator'])}"
            if p.get('reading'):
                source += f" · [中文卡](../{p['reading']})"
            lines.append(f"| {source} | {md(p['object'])}<br>{md(p['supervision'])} | {md(p['method'])}<br>{md(p['time'])} | {md(p['finance'])}<br>{md(p['limit'])} | {md(p['why_core'])} |")
        lines.append('')
    return {'core-matrix.csv': csv_content(core, CORE_FIELDS), 'candidates.csv': csv_content(eligible, CANDIDATE_FIELDS),
            'core-matrix.md': '\n'.join(lines)}, eligible, core


def check_experiments(papers):
    ids = {paper['id'] for paper in papers}
    seen = set()
    with (REVIEW / 'experiment-evidence.csv').open(encoding='utf-8-sig', newline='') as stream:
        reader = csv.DictReader(stream)
        for row in reader:
            key = (row['paper_id'], row['experiment_id'])
            if key[0] not in ids or key in seen or not key[1].strip():
                raise ValueError(f'逐实验提取表含未登记论文或重复实验：{key}')
            for field in ('prediction_object', 'time_and_split', 'positive_and_negative',
                          'evidence_locator', 'source_url'):
                if not row[field].strip():
                    raise ValueError(f'实验 {key} 缺少 {field}')
            seen.add(key)
    return len(seen)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    papers = json.loads(SOURCE.read_text(encoding='utf-8'))
    validate(papers)
    experiments = check_experiments(papers)
    outputs, eligible, core = render(papers)
    for filename, content in outputs.items():
        path = REVIEW / filename
        if args.check:
            if not path.is_file() or path.read_text(encoding='utf-8') != content:
                raise SystemExit(f'{filename} 未同步，请运行 python3 scripts/survey.py')
        else:
            path.write_text(content, encoding='utf-8')
    cards = sum(bool(p.get('reading')) for p in papers)
    if len(eligible) < 150 or len(core) < 60 or cards < 30:
        raise SystemExit('当前专题快照低于约定的候选、核心或独立阅读卡数量')
    print(f'{len(papers)} papers / {len(eligible)} recent / {len(core)} core / {cards} papers with cards / {experiments} experiment rows')
    print(dict(sorted(Counter(p['year'] for p in eligible).items())))


if __name__ == '__main__':
    main()
