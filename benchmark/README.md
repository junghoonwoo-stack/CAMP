# CAMP Benchmark

CAMP Benchmark는 **명시적으로 동의한 조직의 익명화된 CAMP 결과만** 모아 분포를 만드는 선택형 벤치마크입니다.

## Privacy first

기본적으로 수집하지 않는 것:
- 회사명
- 개인 이름
- 이메일
- 자유서술형 내부정보
- 과제명/시스템명

수집하는 최소 정보:
- 제출일
- 국가
- 업종
- 진단 범위(회사/사업부/팀/AI-native 신설조직)
- 인원 구간
- Function
- CAMP Stage
- CAMP Score
- 5개 Dimension Score
- AI Operations 수준
- Sovereign AI 수준

**주의:** GitHub Issue로 제출하는 경우 회사명은 수집하지 않더라도 제출자의 GitHub 계정은 공개될 수 있습니다. 완전한 익명 제출을 보장하지 않습니다. 민감한 조직 정보는 절대 Issue에 적지 마세요.

## 제출 방법

Repository의 `CAMP Benchmark Submission` Issue Form을 사용합니다.

Issue Form은 객관식/선택형 중심으로 구성되어 있으며 회사명 입력을 요구하지 않습니다.

## Ranking 원칙

- 전체 N < 10: 순위 제공 안 함 (`표본 부족`)
- 세부 그룹 N < 10: 해당 그룹 percentile 제공 안 함
- 기본 순위는 CAMP Score 기준 percentile
- 가능하면 Overall / Country / Industry / Size band를 분리
- 모든 비교에는 N과 기준일 표시

## CAMP Score

5개 핵심 Dimension × 20점 = 100점.

1. AI Access
2. AI Delegation
3. Enterprise Connection
4. Knowledge Compounding
5. Role Transformation

AI Operations와 Sovereign AI는 중요한 Supporting Capability이지만 CAMP Score에는 포함하지 않습니다.

## 데이터 사용 원칙

Benchmark는 경쟁 순위표가 아니라 **조직이 자신의 상대적 위치와 다음 투자 우선순위를 이해하는 보조자료**입니다.

CAMP Stage와 Score를 채용평가, 직원 개인평가, 공급업체 제재 등 고위험 의사결정의 단독 근거로 사용하지 마세요.
