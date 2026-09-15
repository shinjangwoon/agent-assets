# agent-assets

에이전트·스킬·자동화 설계 자산. 특정 플랫폼(Multica, Claude Code, Codex 등)이나 특정 고객에 묶이지 않도록 구성한다.

## 구조

```
templates/    고객 무관 틀 — 이슈 본문 형식, 태스크 스키마 정의 방식, 에이전트/스쿼드 명세 틀
skills/       폴더형 스킬 패키지 (SKILL.md + reference/ + examples/). 어느 플랫폼에서든 참조
customers/    고객별 적용 사례. templates/skills 를 어떻게 채웠는지
docs/         플랫폼 API·제약 등 알아낸 사실
```

## 원칙

- 민감정보(사람 이름, 계정 ID, 토큰, 웹훅 URL)는 넣지 않는다. 필요한 자리는 `<placeholder>` 로 둔다.
- 고객 고유 정보는 `customers/<name>/` 아래에만 둔다. `templates/`, `skills/` 는 고객 이름을 모른다.
- 새 고객 = `customers/` 폴더 하나 추가. 스킬은 그대로 재사용.
