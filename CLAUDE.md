# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Jekyll-based personal blog (surinkim.github.io) with automated weekly tech/dev news digest generation. Uses the Lanyon theme with custom modifications and includes a Python-based RSS aggregation tool for curating weekly content.

## Development Environment

**Ruby Setup:**
- Requires Ruby 2.6.10 (specified in `.ruby-version`)
- Install dependencies: `bundle install`
- Site runs locally: `bundle exec jekyll serve`
- Build static site: `bundle exec jekyll build`

**Python Setup (for weekly digest automation):**
- Python 3.10+ with virtual environment in `jobs/.venv/`
- Install dependencies: `cd jobs && pip install -r requirements.txt`

## Weekly Digest Automation

The `jobs/` directory contains a Python CLI tool that aggregates RSS feeds and generates Jekyll markdown posts for weekly tech news digests.

**Basic Usage:**
```bash
# Standard weekly run (last 7 days, max 50 links)
bash jobs/run_weekly_digest.sh

# Preview without creating files
bash jobs/run_weekly_digest.sh --dry-run

# Custom date range and options
bash jobs/run_weekly_digest.sh --from 2026-02-01 --to 2026-02-07 --max-links 25 --verbose
```

**Key Options:**
- `--dry-run`: Preview output without file creation or history updates
- `--translate-en-summary-to-ko`: Translate English summaries to Korean (requires `OPENAI_API_KEY`)
- `--no-history`: Skip duplicate checking (testing only)
- `--verbose`: Debug-level logging

**Configuration Files:**
- `jobs/sources.yml`: RSS feed sources with trust scores, keywords filters, and language settings
- `jobs/category_rules.yml`: Keyword-based categorization rules (AI, Backend, InfraCloud, Tools, Etc)
- `jobs/data/manual_items.yml`: Manual link additions outside of RSS feeds

**Output:**
- Markdown files: `normal/_posts/YYYY-MM-DD-weekly-dev-links-YYYYwWW.md`
- Run reports: `jobs/data/runs/YYYY-MM-DD/report.json`
- History tracking: `jobs/data/history/url_history.jsonl` (auto-purged after 90 days)

**Pipeline:**
RSS collection → URL normalization → deduplication (URL + title similarity) → history filtering → quality scoring → category assignment → markdown rendering

## Project Structure

**Posts:**
- `_posts.1/`: Legacy/example posts from theme
- `normal/_posts/`: Active blog posts (both manual and automated weekly digests)

**Layouts & Theming:**
- `_layouts/`: Jekyll page templates
- `_includes/`: Reusable template components
- `_sass/`: Sass stylesheets for theme
- `assets/`: Theme assets

**Static Content:**
- `img/`, `public/`, `books/`, `games/`: Static assets
- `about.md`, `archive.md`, `book.md`: Top-level pages
- `_site/`: Generated output (excluded from git, do not edit manually)

**Configuration:**
- `_config.yml`: Main Jekyll configuration (site title, pagination, plugins, excluded paths)
- `_1config.yml`: Alternative/backup config
- `.editorconfig`: 2-space indentation, LF line endings, trim trailing whitespace

## Content Creation

**Manual Blog Posts:**
1. Create file in `normal/_posts/` with naming: `YYYY-MM-DD-slug.md`
2. Include front matter with layout, title, date, categories, tags
3. Use kramdown markdown with rouge syntax highlighting
4. Preview with `bundle exec jekyll serve`

**Weekly Digest Posts:**
1. Run automation tool: `bash jobs/run_weekly_digest.sh`
2. Review generated markdown in `normal/_posts/`
3. Edit if needed (summaries, category assignments, link selection)
4. Rebuild site to see changes

## Managing RSS Sources

**Adding a New Source:**
Edit `jobs/sources.yml`:
```yaml
- id: source_id
  name: "Source Name"
  type: rss  # or atom, json, manual
  url: https://example.com/feed
  trust: 0.8  # 0.0-1.0, affects scoring
  language: en  # ko or en
  include_keywords: ["ai", "backend"]  # optional: require at least one match
  exclude_keywords: ["ads", "politics"]  # optional: filter out matches
  enabled: true
```

**Disabling a Source:**
Set `enabled: false` in the source entry.

## Key Plugins

- `jekyll-paginate`: Homepage pagination (5 posts per page)
- `jekyll-graphviz`: GraphViz diagram rendering
- `kramdown`: Markdown processor
- `rouge`: Syntax highlighting

## Build Output

- All site generation goes to `_site/`
- The `jobs/` and `.job/` directories are excluded from Jekyll builds (see `_config.yml`)
- Git ignores `_site/`, `.sass-cache/`, and `jobs/.venv/`

## Site Configuration

- Site URL: `https://corecode.pe.kr`
- Disqus comments enabled (shortname: `hyunblog`)
- Custom theme config: auto appearance, date format `%Y-%m-%d`
- Comments enabled by default for posts
