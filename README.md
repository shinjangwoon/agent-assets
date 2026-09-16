# agent-assets

에이전트·스킬·자동화 설계 자산. 플랫폼 무관 자산을 최상위에, 플랫폼 전용은 그 플랫폼 이름 폴더 아래에 둔다. 특정 고객 정보는 넣지 않는다.

## 구조

[Agent Skills 개방 표준](https://agentskills.io/specification)을 따른다. `skills/` 아래 각 폴더가 스킬 하나이고, Claude Code · Codex · Cursor · Gemini CLI · Multica 가 같은 파일을 그대로 쓴다.

```
skills/            스킬. 폴더마다 SKILL.md (+ reference/ examples/ scripts/)
templates/         스킬이 아닌 틀 — 이슈 본문 형식, 태스크 스키마 정의 방식, 에이전트/스쿼드 명세 틀
docs/<platform>/   플랫폼별로 알아낸 사실 (API 형식, 제약)
AGENTS.md          항상 적용되는 규칙. CLAUDE.md 는 이 파일의 심볼릭 링크
```

## 설치

```bash
npx skills add <owner>/agent-assets            # 설치된 에이전트 자동 감지
npx skills add <owner>/agent-assets -g          # 전역
npx skills add <owner>/agent-assets --list      # 목록만
```

Multica 는 `multica skill import --url github.com/<owner>/agent-assets/tree/main/skills/<name>` 으로 스킬 단위 import.

## 원칙

- 민감정보(사람 이름, 계정 ID, 토큰, 웹훅 URL)는 넣지 않는다. 필요한 자리는 `<placeholder>` 로 둔다.
- **고객 고유 정보(기관 목록, 라벨 체계, 매핑, 담당자)는 넣지 않는다.** 그건 각 플랫폼(Multica 등)의 스킬·지침에만 둔다.
- 예시에 나오는 기관·시스템·사람 이름은 전부 가상이다.
