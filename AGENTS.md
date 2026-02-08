# Repository Guidelines

## Project Structure & Module Organization
- Jekyll site with configuration in `_config.yml` (and `_1config.yml`).
- Layouts and includes live in `_layouts/` and `_includes/`.
- Posts are stored in `_posts.1/` using the Jekyll `YYYY-MM-DD-title.md` naming pattern.
- Static pages are in the repo root (for example `index.html`, `about.md`, `archive.md`).
- Assets live in `img/`, `public/`, `books/`, `games/`, and `normal/`.
- Generated site output is in `_site/` (do not edit by hand).

## Build, Test, and Development Commands
- `bundle install` installs Ruby dependencies from `Gemfile`.
- `bundle exec jekyll serve` runs the local dev server with live rebuilds.
- `bundle exec jekyll build` builds the static site into `_site/`.

## Coding Style & Naming Conventions
- Follow `.editorconfig`: 2-space indentation, LF, trim trailing whitespace, and final newline.
- Markdown files use lowercase, hyphenated slugs in filenames (for example `_posts.1/2024-01-01-my-post.md`).
- Keep front matter consistent with existing pages (title, layout, date, tags where applicable).

## Testing Guidelines
- No automated test framework is configured.
- Validate changes by running `bundle exec jekyll serve` and checking output in the browser.

## Commit & Pull Request Guidelines
- Commit messages are short, descriptive sentences (often starting with “Add …”); no strict convention.
- PRs should include a concise summary, link any related issues, and include screenshots for visual changes.

## Configuration & Content Tips
- Update site-wide settings in `_config.yml` (author, title, pagination, plugins).
- Avoid editing `_site/`; rebuild instead.
