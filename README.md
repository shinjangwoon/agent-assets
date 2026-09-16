# agent-assets

에이전트·스킬·자동화 설계 자산. 플랫폼 무관 자산을 최상위에, 플랫폼 전용은 그 플랫폼 이름 폴더 아래에 둔다. 특정 고객 정보는 넣지 않는다.

## 구조

```
templates/    플랫폼 무관 틀 — 이슈 본문 형식, 태스크 스키마 정의 방식, 에이전트/스쿼드 명세 틀
skills/       플랫폼 무관 스킬 (Agent Skills 표준: frontmatter + SKILL.md + reference/ + examples/)
              Claude Code · Codex · Multica import 모두 읽을 수 있다
multica/      Multica 전용 — API 형식, 검증된 제약, (필요 시) Multica 에서만 쓰는 스킬
```

## 원칙

- 민감정보(사람 이름, 계정 ID, 토큰, 웹훅 URL)는 넣지 않는다. 필요한 자리는 `<placeholder>` 로 둔다.
- **고객 고유 정보(기관 목록, 라벨 체계, 매핑, 담당자)는 넣지 않는다.** 그건 각 플랫폼(Multica 등)의 스킬·지침에만 둔다.
- 예시에 나오는 기관·시스템·사람 이름은 전부 가상이다.
