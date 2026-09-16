---
name: task-creator
description: 채팅 요청을 정리된 태스크(이슈)로 만든다. 절차·판단 기준·본문 형식·검증 스크립트를 제공한다. 고객별 값(기관·라벨·담당자)은 이 스킬을 가져간 플랫폼의 SKILL.md 가 덮어쓴다.
metadata:
  version: "1.0"
---

# Task Creator

사람이 말로 한 요청을 **정리된 태스크**로 바꾼다. 받아쓰기가 아니다.
핵심 원칙: 추측으로 채우지 않는다. 빠진 건 묻고, 만들기 전에 스크립트로 검증한다.

## 워크플로

### 1. 요청 분석

요청에서 뽑는다: **제목 · 분류(SR/내부) · 기관 · 담당자 · 기한 · 본문 재료**.
판단 기준은 `references/routing.md`. 애매하면 **한 번** 묻는다.

### 2. 필수 확인

플랫폼 SKILL.md 의 필수 항목이 빠졌으면 **한 번에 모아** 묻는다. 답을 받은 뒤 진행한다.

### 3. 본문 작성

`references/issue-format.md` 형식. 핵심 정보 목록 → `---` → 체크리스트 섹션.
크기(단순 / 일반 / 상위)에 따라 분량이 다르다. 확정 안 된 값은 `**(확정 필요)**`.

### 4. 검증

```bash
python3 scripts/validate_task.py task.json --schema schema.json
```

`task.json` 은 만들 태스크, `schema.json` 은 플랫폼 SKILL.md 의 값(기관·라벨)을 JSON 으로 옮긴 것.
`ERR` 가 하나라도 있으면 만들지 않는다. `WARN` 은 사용자에게 알리고 진행한다.

### 5. 생성

라벨·속성·날짜·부모 연결을 플랫폼 SKILL.md 대로. 하위 이슈는 상위를 먼저 만들고 부모 연결.

### 6. 보고

만든 이슈 식별자와 링크 한 줄. 상위/하위면 전부. `(확정 필요)` 로 남긴 항목이 있으면 같이 알린다.

## 하지 말 것

- 요청자가 말하지 않은 값을 채우지 않는다.
- 기존 이슈를 수정하지 않는다 (생성 전용).
- 담당자를 에이전트로 지정하지 않는다.
- 검증을 건너뛰지 않는다.

## 파일

| 파일 | 언제 읽나 |
|---|---|
| `references/routing.md` | 1단계. SR/내부/단순/계층 판단 |
| `references/issue-format.md` | 3단계. 본문 쓸 때 |
| `scripts/validate_task.py` | 4단계. 생성 직전 |
| `assets/example-task.json` | 입력 형식 참고 |
| `assets/example-schema.json` | 스키마 JSON 형식 참고 |
