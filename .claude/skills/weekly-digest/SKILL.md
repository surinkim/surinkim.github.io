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

확정된 날짜로 다이제스트 생성 스크립트를 **한 번만** 실행한다:

```
bash jobs/run_weekly_digest.sh --from {시작일} --to {종료일} --verbose 2>&1 | tee /tmp/weekly_digest_run.log
```

**중요: 절대 옵션 없이 두 번 실행하지 말 것.**
- 첫 실행 시 선택된 항목 70개가 `jobs/data/history/url_history.jsonl`에 자동 저장된다
- 옵션 없이 재실행하면 history dedup으로 이번 주 항목이 모두 제외되어 빈약한 `_v2.md` 부산물이 생성된다 (스크립트는 파일명 충돌 시 자동으로 `_v2`, `_v3` 접미사를 붙임)
- 따라서 단 한 번의 실행 결과(`/tmp/weekly_digest_run.log`)에서 필요한 모든 정보를 추출해야 한다

부득이하게 재실행해야 한다면 반드시 다음 옵션 중 하나를 사용한다:
- `--dry-run`: 파일 생성·history 업데이트 없이 미리보기만
- `--no-history`: history dedup을 건너뛰어 이번 주 항목이 다시 수집되게 함

실행 결과 로그에서 다음 정보를 추출한다 (`grep`이나 `tail`로 한 번에 처리):
- 수집된 소스 수, 총 항목 수: `grep -E "Collected|Source.*collected"`
- 최종 선택된 항목 수: `grep "Selected"`
- 생성된 마크다운 파일 경로: `grep "Markdown saved"`
- 오류/경고 메시지: `grep -iE "warning|failed|error"`

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

## 4단계: 직전 다이제스트와 URL 중복 검증

**왜 필요한가:** 일부 RSS 피드(특히 요즘IT `yozm_wishket`)는 `<pubDate>` 태그가 없어서 `published_at`이 fetch 시점(=오늘)으로 fallback된다. 이로 인해 매주 같은 글이 "이번 주 발행"으로 분류되어 다이제스트에 반복 등장한다. history dedup이 정상 작동하면 막히지만, 누락된 run이 있으면 그대로 통과한다. 따라서 출고 전 직전 다이제스트와 직접 교차 비교가 필수다.

직전 2개 주간 다이제스트와 URL을 비교한다:

```bash
# 직전 2주 포스트의 URL 추출
prev_urls=$(grep -hoE 'https?://[^)]+' normal/_posts/$(ls normal/_posts/*weekly-dev-links* | sort | tail -3 | head -2 | xargs -n1 basename | tr '\n' ' ') | sort -u)

# 이번 주 포스트와 교차 비교
this_urls=$(grep -oE 'https?://[^)]+' normal/_posts/{이번주_파일} | sort -u)

# 중복 URL 출력
comm -12 <(echo "$prev_urls") <(echo "$this_urls")
```

중복이 발견되면:
1. 중복 항목 목록을 사용자에게 보여준다 (URL과 제목)
2. `Edit` 도구로 중복된 항목을 마크다운 파일에서 제거한다
3. 제거 결과를 4단계 보고에 포함한다

## 5단계: 이번 주 pick! 섹션 작성

포스트 맨 위(front matter 바로 아래, `## AI` 섹션 위)에 `## 이번 주 pick!` 섹션을 추가한다.

**선정 기준 (순서대로 각 1개씩, 총 3개):**
1. **파급력** — 업계 판도에 영향을 줄 뉴스 (표준 발표, 주요 인사 이동, 메이저 릴리즈 등)
2. **흥미도** — 기술적으로 재미있거나 참신한 아이디어, 개발자가 공감할 사례
3. **실용성** — 지금 당장 실무에 써볼 수 있는 도구/라이브러리

**선정 범위:** 본문 목록에 포함된 항목 중에서만 고른다. 본문에 없는 항목을 에디터 픽에 넣으려면 해당 항목을 본문 목록에도 먼저 추가한다.

**형식:**
```markdown
## 이번 주 pick!

**1. [제목](링크)**

3~4줄 요약. 왜 주목할 만한지, 어떤 의미가 있는지를 중심으로 작성.
단순 번역이 아니라 에디터의 시각으로 풀어쓴다.

**2. [제목](링크)**

3~4줄 요약.

**3. [제목](링크)**

3~4줄 요약.

---
```

## 6단계: VS Code로 작업 폴더 열기

마크다운 페이지 작업(생성·요약 보정·중복 검증)이 완료되면 작업 폴더를 VS Code로 연다:

```bash
code /Users/kimhyunukkim/work/surinkim.github.io
```

## 7단계: 결과 보고

사용자에게 다음을 보고한다:
- 생성된 파일 경로
- 수집/선택 통계 요약
- GitHub Trending 요약 보정 여부
- 이번 주 pick! 선정 항목 3개 요약
- 커밋 & 푸시 여부를 묻는다
