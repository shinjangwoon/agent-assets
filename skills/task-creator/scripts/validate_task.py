#!/usr/bin/env python3
"""태스크 생성 전 검증.

입력: JSON (stdin 또는 파일)
  {
    "title": "[육아] NGS 계정 생성",
    "kind": "sr" | "internal",
    "org": "육아정책연구소" | "",
    "labels": ["경제인문사회연구회", "단순처리업무"],
    "description": "...",
    "start_date": "2026-09-16",
    "due_date": "",
    "parent_title": ""          # 하위 이슈면 상위 제목
  }
스키마: --schema <json>  (플랫폼 스킬 SKILL.md 에서 뽑은 값. 없으면 구조 검증만)
  {
    "orgs": {"육아": "육아정책연구소", ...},          # 약칭 → 정식명
    "always_labels": ["경제인문사회연구회"],
    "kind_labels": {"internal": "내부업무", "simple": "단순처리업무"},
    "hierarchy_labels": ["상위업무", "하위업무"]
  }
출력: 문제 목록. 없으면 "OK". 종료 코드 0/1.
"""
import json, re, sys, argparse

def load(path):
    return json.load(open(path)) if path else json.load(sys.stdin)

def check(t, s):
    errs, warns = [], []
    title = t.get("title", "").strip()
    kind = t.get("kind", "")
    org = t.get("org", "").strip()
    labels = set(t.get("labels") or [])
    desc = t.get("description", "")

    # 제목
    if not title:
        errs.append("제목 없음")
    else:
        if len(title) > 40: warns.append(f"제목이 깁니다 ({len(title)}자). 15~30자 권장")
        for w in ("요청", "확인 부탁", "문의드립니다"):
            if title.endswith(w) or title.endswith(w + "건"):
                warns.append(f"제목에 접수 표현 '{w}' — 주제만 남길 것")
        m = re.match(r"^\[([^\]]+)\]\s*(.+)$", title)
        if s and m:
            abbr, rest = m.group(1), m.group(2)
            if abbr in s.get("orgs", {}) and org and s["orgs"][abbr] != org:
                errs.append(f"접두사 [{abbr}]={s['orgs'][abbr]} 인데 org='{org}' — 불일치")
            if abbr in s.get("orgs", {}) and s["orgs"][abbr] in rest:
                warns.append("제목에 기관명이 접두사와 중복")

    # 분류
    if kind not in ("sr", "internal"):
        errs.append("kind 는 sr | internal")
    if kind == "sr" and not org:
        errs.append("SR 은 org(기관) 필수")

    # 라벨
    if s:
        for L in s.get("always_labels", []):
            if L not in labels: errs.append(f"항상 라벨 '{L}' 누락")
        kl = s.get("kind_labels", {})
        internal, simple = kl.get("internal"), kl.get("simple")
        if kind == "internal" and internal and internal not in labels:
            errs.append(f"내부 업무인데 '{internal}' 라벨 없음")
        if kind == "sr" and internal and internal in labels:
            errs.append(f"SR 인데 '{internal}' 라벨 있음")
        if internal in labels and simple in labels:
            errs.append(f"'{internal}' 과 '{simple}' 동시 부착 — 하나만")
        hl = s.get("hierarchy_labels", [])
        if len(labels & set(hl)) > 1:
            errs.append("상위/하위 라벨 동시 부착")

    # 계층
    parent = t.get("parent_title", "").strip()
    if parent and not desc.lstrip().startswith("상위:"):
        errs.append("하위 이슈인데 본문 첫 줄이 '상위:' 로 시작하지 않음")

    # 본문
    if not desc.strip():
        errs.append("본문 없음")
    else:
        if "---" not in desc: warns.append("본문에 구분선(---) 없음 — 핵심 정보 / 본론 구분 권장")
        if "- [ ]" not in desc and "- [x]" not in desc: warns.append("본문에 체크리스트 없음")
        if re.search(r"[??]\s*$", desc, re.M): warns.append("본문에 물음표로 끝나는 줄 — 확정 안 된 값은 '(확정 필요)' 로")

    # 날짜
    if not t.get("start_date"): errs.append("start_date 없음 (기본 = 오늘)")
    for k in ("start_date", "due_date"):
        v = t.get(k, "")
        if v and not re.match(r"^\d{4}-\d{2}-\d{2}$", v): errs.append(f"{k} 형식 YYYY-MM-DD 아님: {v}")

    return errs, warns

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("task", nargs="?", help="task JSON 파일 (없으면 stdin)")
    ap.add_argument("--schema", help="스키마 JSON 파일")
    a = ap.parse_args()
    t = load(a.task)
    s = json.load(open(a.schema)) if a.schema else None
    errs, warns = check(t, s)
    for w in warns: print("WARN", w)
    for e in errs: print("ERR ", e)
    if not errs and not warns: print("OK")
    sys.exit(1 if errs else 0)

if __name__ == "__main__":
    main()
