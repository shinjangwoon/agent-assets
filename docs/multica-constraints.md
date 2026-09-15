# Multica 제약 (검증됨)

| 제약 | 검증 | 대응 |
|---|---|---|
| 외부로 이벤트/웹훅을 보내지 않음 | autopilot webhook 은 인바운드만 | 폴링 |
| 본문(description) 멘션은 에이전트를 깨우지 않음 | UI·API 각 1회, 105초 대기 | 폴링 → autopilot 웹훅 |
| 코멘트 멘션은 에이전트를 즉시 깨움 | 다수 확인 | — |
| 멤버 본문 멘션은 자체 알림 감 | 사용자 확인 | — |
| 멤버 그룹 개념 없음 | team/group 명령 없음 | 에이전트를 그룹 대용으로 멘션 |
| squad 는 리더 에이전트 필수 | CLI | 작업 위임용. 알림 그룹 아님 |
| 퀵 액션은 UI 전용 | CLI 없음 | 실행해도 이슈 상태 안 바뀜 |
| 멘션 저장 형식 | `[@name](mention://member/<user_id>)` / `mention://agent/<id>` | 텍스트에 박힘, 별도 필드 없음 |
| 에이전트 지침 "외부 API 금지" | 웹훅 호출도 거부 | 허용 대상 명시 |
| 속성 select 옵션 | `property update --option` 이 전체 교체 | 기존 이름 유지하면 id 보존 |

## 원인 추적
`agent tasks <id>` 의 `trigger_summary` / `delivered_comment_ids` 로 무엇이 깨웠는지 확인.
`issue runs <id>` 로 큐/취소 상태 확인.
