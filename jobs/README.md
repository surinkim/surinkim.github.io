# 주간 개발 소식 링크 모음 자동화

RSS 피드를 수집하여 Jekyll 블로그용 Markdown 초안을 생성하는 CLI 도구.

## 사용법

```bash
# 기본 실행 (최근 7일, 최대 50개 링크, normal/_posts/에 MD 생성)
bash jobs/run_weekly_digest.sh

# 미리보기 (파일 생성 없이 콘솔 출력만)
bash jobs/run_weekly_digest.sh --dry-run

# 옵션 지정
bash jobs/run_weekly_digest.sh --from 2026-02-01 --to 2026-02-07 --max-links 25 --verbose
```

## CLI 옵션

| 옵션 | 기본값 | 설명 |
|------|--------|------|
| `--from` | today - 6일 | 수집 시작일 (YYYY-MM-DD) |
| `--to` | today | 수집 종료일 (YYYY-MM-DD) |
| `--max-links` | 50 | 최종 선택 링크 수 상한 |
| `--output-dir` | `normal/_posts` | MD 파일 저장 경로 |
| `--dry-run` | - | 파일 미생성, 콘솔 출력만. 히스토리에도 기록하지 않음 |
| `--sources` | `jobs/sources.yml` | 소스 설정 파일 경로 |
| `--no-history` | - | 히스토리 중복 체크 건너뛰기 (테스트용) |
| `--verbose` | - | DEBUG 레벨 상세 로그 |
| `--summary-max-sentences` | 2 | 요약 최대 문장 수 |
| `--summary-max-chars` | 220 | 요약 최대 글자 수 (초과 시 `...`) |
| `--translate-en-summary-to-ko` | - | 영문 요약을 한글로 번역 (OPENAI_API_KEY 필요) |
| `--openai-model` | `gpt-4o-mini` | 번역에 사용할 OpenAI 모델 |

## 파이프라인

```
RSS 수집 → URL 정규화 → URL 중복제거 → 제목 유사도 중복제거
→ 히스토리 중복제거 → 품질 필터 → 카테고리 분류 → 점수화/선택 → Markdown 렌더링
```

## 출력물

- **MD 파일**: `normal/_posts/YYYY-MM-DD-weekly-dev-links-YYYYwWW.md`
- **실행 리포트**: `jobs/data/runs/YYYY-MM-DD/report.json`
- **히스토리**: `jobs/data/history/url_history.jsonl` (90일 자동 정리)

## 소스 관리

`jobs/sources.yml`에서 피드를 추가/삭제/비활성화할 수 있다.

```yaml
- id: my_source
  name: "My Source"
  type: rss          # rss | atom | json | manual
  url: https://example.com/feed
  trust: 0.8         # 0.0~1.0 (점수화에 사용)
  language: en        # ko | en
  curl_fallback: false  # true면 httpx 실패 시 curl로 1회 재시도
  headers:              # 필요 시 소스별 커스텀 헤더
    Referer: "https://example.com/"
  include_keywords: ["ai", "backend"]   # 있으면 제목/요약에 1개 이상 포함될 때만 채택
  exclude_keywords: ["광고", "정치"]     # 있으면 제목/요약에 포함 시 제외
  enabled: true       # false로 비활성화
```

수동 항목은 `jobs/data/manual_items.yml`에 직접 추가한다.

## 요약 표시 정책

- 기본: 모든 요약은 최대 2문장 + 최대 220자로 압축
- 길이 초과 시 말줄임표(`...`) 표시
- 영문 요약 한글 번역이 필요하면:

```bash
export OPENAI_API_KEY=your_key
bash jobs/run_weekly_digest.sh --translate-en-summary-to-ko
```

## 카테고리 규칙

`jobs/category_rules.yml`에서 키워드 기반 분류 규칙을 수정할 수 있다.
우선순위: AI > Backend > InfraCloud > Tools > Etc

## 종료 코드

| 코드 | 의미 |
|------|------|
| 0 | 정상 완료 |
| 2 | 성공한 소스가 30% 이하 |
| 3 | 출력 파일 생성 실패 |
