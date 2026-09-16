# agent-assets

에이전트·스킬·자동화 설계 자산. 플랫폼 무관 자산을 최상위에, 플랫폼 전용은 그 플랫폼 이름 폴더 아래에 둔다. 특정 고객 정보는 넣지 않는다.

## 구조

[Agent Skills 개방 표준](https://agentskills.io/specification)을 따른다.

```
skills/            스킬. 폴더마다 SKILL.md + references/ scripts/ assets/
                   고객 정보 없음 — 절차·판단 기준·본문 형식·검증 스크립트만
templates/         스킬이 아닌 틀 — 에이전트/스쿼드 명세, 스키마 정의 방식
docs/<platform>/   플랫폼별로 알아낸 사실
AGENTS.md          항상 적용되는 규칙. CLAUDE.md 는 심볼릭 링크
```

## 고객 값은 어디에

기관·라벨·담당자 같은 고객 고유 값은 **여기 두지 않는다.** 스킬을 배정받은 에이전트의 지침(플랫폼 안)에 둔다.
그래서 이 저장소는 공개여도 되고, 플랫폼에서 `refresh` 해도 고객 값이 지워지지 않는다.

## 설치

```bash
npx skills add shinjangwoon/agent-assets              # 설치된 에이전트 자동 감지
npx skills add shinjangwoon/agent-assets --list
```

Multica: `multica skill import --url github.com/shinjangwoon/agent-assets/tree/master/skills/<name>`.
수정 후 `git push` → `multica skill refresh <id>`.

## 원칙

- 민감정보(사람 이름, 계정 ID, 토큰, 웹훅 URL)는 넣지 않는다. 필요한 자리는 `<placeholder>` 로 둔다.
- **고객 고유 정보(기관 목록, 라벨 체계, 매핑, 담당자)는 넣지 않는다.** 그건 각 플랫폼(Multica 등)의 스킬·지침에만 둔다.
- 예시에 나오는 기관·시스템·사람 이름은 전부 가상이다.
