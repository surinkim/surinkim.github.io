---
name: weekly-digest
description: 주간 테크/개발 뉴스 다이제스트를 생성한다. RSS 수집, GitHub Trending 한국어 요약, 마크다운 포스트 생성까지 자동화.
disable-model-invocation: false
allowed-tools: Bash Read Edit Grep Glob WebFetch AskUserQuestion
---

# 주간 테크/개발 뉴스 다이제스트 생성

이 스킬은 주간 테크 뉴스 마크다운 포스트를 자동 생성한다.

## 1단계: 날짜 확인

가장 최근 작성된 주간 뉴스 포스트의 날짜 범위를 기반으로 다음 주 범위를 자동 계산한다:

1. `normal/_posts/` 디렉토리에서 `*weekly-dev-links*` 파일 중 가장 최신 파일을 찾는다
2. 해당 파일의 title에서 날짜 범위를 추출한다 (예: `#2026 4/5 ~ 4/11`)
3. 종료일 다음 날을 새 시작일, 시작일 + 6일을 새 종료일로 계산한다
   - 예: 최신이 `4/5 ~ 4/11`이면 → 새 범위는 `4/12 ~ 4/18`

`AskUserQuestion`을 사용하여 사용자에게 날짜를 확인받는다:
- 질문: "주간 뉴스 생성 기간이 맞나요?"
- 옵션 1: "{시작일} ~ {종료일} 로 진행" (기본 추천)
- 옵션 2: "날짜 직접 입력"

사용자가 "날짜 직접 입력"을 선택하면, 입력받은 날짜를 사용한다.

## 2단계: 스크립트 실행

확정된 날짜로 다이제스트 생성 스크립트를 실행한다:

```
bash jobs/run_weekly_digest.sh --from {시작일} --to {종료일} --verbose
```

실행 결과 로그에서 다음 정보를 추출한다:
- 수집된 소스 수, 총 항목 수
- 최종 선택된 항목 수
- 생성된 마크다운 파일 경로
- 오류/경고 메시지

## 3단계: GitHub Trending 한국어 요약 보정

실행 로그에서 `claude CLI not found` 또는 `summarization failed` 경고가 있는지 확인한다.

경고가 있으면:
1. 생성된 마크다운 파일에서 `## GitHub Trending` 섹션을 찾는다
2. **GitHub Developer 항목** (예: `[GitHub Developer: Name (@username)](url)` 형태)은 한국어 요약 없이 그대로 둔다
3. `github_trending_repositories` 항목 중 영문 fallback 텍스트(예: `Star owner / repo ...` 패턴)가 있는 항목을 식별한다
4. 각 프로젝트에 대해:
   - `curl -s https://api.github.com/repos/{owner}/{repo}/readme -H "Accept: application/vnd.github.v3.raw"` 로 README를 가져온다
   - README 내용을 바탕으로 한국어 3문장 이내 요약을 생성한다
   - 요약 작성 규칙:
     - 단순 번역이 아니라 주요 기능, 특징, 주목할 만한 이유를 정리
     - 기술 용어(라이브러리명, 프레임워크명 등)는 영문 그대로 유지
     - 요약만 작성, 부가 설명 없음
5. `Edit` 도구로 영문 텍스트를 한국어 요약으로 교체한다

## 4단계: 결과 보고

사용자에게 다음을 보고한다:
- 생성된 파일 경로
- 수집/선택 통계 요약
- GitHub Trending 요약 보정 여부
- 커밋 & 푸시 여부를 묻는다
