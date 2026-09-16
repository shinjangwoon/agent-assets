# NRC 업무 스쿼드

`templates/squad-spec.md` 를 채운 것. ID·이름은 Multica 워크스페이스 기준. 담당자 개인정보 없음.

## 목적
NRC 프로젝트 요청의 단일 채팅 진입점. 리더가 분류해 위임한다.

## 리더 — NRC 업무 리더
요청 주체가 **고객 기관이면 SR**, **우리면 내부 업무**. 애매하면 한 번 묻는다. 직접 만들지 않는다.

## 멤버
| 에이전트 | 담당 | 스킬 |
|---|---|---|
| NRC SR 태스크 생성 | 고객 요청 태스크. 기관 필수. 단순처리 판단 | nrc-task-schema · msp-safety-baseline |
| NRC 일반업무 태스크 생성 | 내부 업무. 상위/하위 구조 | nrc-task-schema · msp-safety-baseline |
| NRC 주간보고 | 주간보고 워크플로 실행·전달 | nrc-task-schema · msp-safety-baseline |
| 경사연 담당자 | 그룹 멘션 대용 | nrc-task-schema · msp-safety-baseline |
| NRC 태스크 알림 | 퀵 액션 Teams 재발송 | nrc-task-schema · msp-safety-baseline |

## 라우팅 예시
- "육아연에서 NGS 계정 하나 만들어달래" → SR 태스크 생성
- "아코디언 업그레이드 작업 정리해줘" → 일반업무 태스크 생성 (상위/하위)
- "주간보고 줘" → NRC 주간보고
- 담당자들에게 알려야 함 → 경사연 담당자

## 스킬
- `nrc-task-schema` — Multica 안에서만 관리. 절차·기관·라벨·상태·담당자·본문 형식·예시·점검 목록 전부 포함. 6개 에이전트 공통 배정.
- `msp-safety-baseline` — 기존 공용 안전 스킬.
- 런타임: 6개 모두 `sjw-kirocrew` (Kiro). Kiro 는 thinking_level 을 받지 않으므로 비워둔다.
