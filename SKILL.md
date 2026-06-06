# last30days-skill-wrap — Skill Specification

## Name
`last30days-skill-wrap`

## Description (EN)
AI agent research skill that aggregates Reddit, X/Twitter, YouTube, Hacker News, Polymarket, GitHub, and the open web into a single synthesized brief. Research any topic — person, company, product, or "X vs Y" — in one command.

## Description (中文)
AI agent 研究技能，聚合 Reddit、X/Twitter、YouTube、Hacker News、Polymarket、GitHub 和全网信息，生成综合简报。研究任何话题——人物、公司、产品或"X vs Y"——一条命令搞定。

## Category
research, ai, productivity, social-media, analysis

## Platforms
- Claude Code: `/plugin marketplace add mvanhorn/last30days-skill`
- Codex/Cursor/Copilot/Gemini CLI: `npx skills add mvanhorn/last30days-skill -g`
- OpenClaw: `clawhub install last30days-official`
- Manual: `git clone` + symlink

## Commands

### `/last30days <topic>`
Research any topic across all enabled sources.

### `/last30days <topic> --emit=html`
Export as a self-contained, dark-mode, print-friendly HTML brief.

### `/last30days <person> --github-user=<username>`
Person-mode: focus on what a person is shipping on GitHub.

### `/last30days <topic> eli5`
Rewrite synthesis in plain language (ELI5 mode).

### `/last30days <topic> --competitors`
Auto-discover and compare top 2 competitors.

## Environment Variables

| Variable | Sources | Required |
|----------|---------|----------|
| (none) | Reddit, HN, Polymarket, GitHub | ❌ Free |
| Browser login | X/Twitter | ❌ Free |
| `yt-dlp` | YouTube | ❌ Free |
| `SCRAPECREATORS_API_KEY` | TikTok, Instagram, Threads, Pinterest | ✅ PAYG |
| `OPENROUTER_API_KEY` | Perplexity Sonar | ✅ PAYG |
| `BRAVE_SEARCH_KEY` | Web search | ✅ 2K/month free |

## Save Directory
- Default: `~/Documents/Last30Days/`
- Override: `LAST30DAYS_MEMORY_DIR` env var or `--save-dir <path>`

## Output Files
- Raw markdown: `<slug>-raw[-suffix].md`
- HTML brief: `<slug>-brief.html`

## License
MIT

## Source
[mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)

## Wrapped By
[q15004040209-creator/last30days-skill-wrap](https://github.com/q15004040209-creator/last30days-skill-wrap)