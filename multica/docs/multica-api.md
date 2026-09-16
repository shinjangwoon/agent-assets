# Multica API (실측)

CLI 요청을 로컬 에코 서버로 캡처해 확정. 문서 없음.

```
베이스      https://<multica-host>
인증        Authorization: Bearer <token>
workspace   ?workspace_id=<ws>   ← 쿼리스트링. 본문에 넣으면 400

이슈 목록   GET  /api/issues?workspace_id&project_id&metadata={"k":v}&sort=created_at&direction=desc&limit
            응답 {issues:[…], total} — description·metadata·labels·properties 포함
이슈 생성   POST /api/issues?workspace_id   {project_id, title, description, status, start_date, due_date, assignee_id, assignee_type:"member"}
이슈 수정   PUT  /api/issues/{id}?workspace_id
이슈 삭제   DELETE /api/issues/{id}?workspace_id   → 204
코멘트      POST /api/issues/{id}/comments?workspace_id   {content}
라벨        POST /api/issues/{id}/labels?workspace_id     {label_id}
metadata   PUT  /api/issues/{id}/metadata/{key}?workspace_id   {value}     ← 키별. 객체 통째는 405
속성        PUT  /api/issues/{id}/properties/{prop_id}?workspace_id   {value}
멤버        GET  /api/workspaces/{ws}/members   → 배정에는 `user_id` (not `id`)
autopilot  POST /api/webhooks/autopilots/<secret>   {…}  → 에이전트 실행, 페이로드가 프롬프트로 전달
```

## 함정
- `assignee_id` 는 멤버 목록의 `user_id`. `id` 는 멤버십 레코드.
- `assignee_id` 와 `assignee_type` 은 함께 있어야 함.
- Header Auth 자격증명: Name=`Authorization`, Value=`Bearer <token>`. 이름 자리에 자격증명 이름을 넣으면 헤더가 안 나감.
- 이슈에 에이전트를 배정하면 즉시 실행됨. 사람 태스크에 절대 금지.
- 이슈 status 를 바꾸면 진행 중 에이전트 태스크가 취소됨.
