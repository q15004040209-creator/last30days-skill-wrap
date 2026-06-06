#!/usr/bin/env python3
"""
last30days-skill-wrap Demo CLI
AI research skill wrapper for Reddit/X/YouTube/HN/Polymarket/web

Usage:
    python demo.py "topic" [--emit html] [--save-dir PATH] [--eli5] [--github-user USERNAME]
"""

import argparse
import os
import sys
import subprocess
import webbrowser
from pathlib import Path
from datetime import datetime

# Default save directory
DEFAULT_SAVE_DIR = Path.home() / "Documents" / "Last30Days"
DEFAULT_SAVE_DIR.mkdir(parents=True, exist_ok=True)


def get_env(key: str) -> str | None:
    """Get API key from environment."""
    return os.environ.get(key)


def check_dependencies() -> list[str]:
    """Check which API keys are configured."""
    configured = []
    if get_env("SCRAPECREATORS_API_KEY"):
        configured.append("✅ TikTok + Instagram + Threads + Pinterest")
    if get_env("OPENROUTER_API_KEY"):
        configured.append("✅ Perplexity Sonar")
    if get_env("BRAVE_SEARCH_KEY"):
        configured.append("✅ Brave Search")
    if get_env("XAI_API_KEY"):
        configured.append("✅ XAI (x-ai.com)")
    if not configured:
        configured.append("ℹ️  No optional keys set (Reddit/HN/Polymarket/GitHub work for free)")
    return configured


def print_banner():
    """Print the last30days banner."""
    banner = r"""
╔══════════════════════════════════════════════════════════╗
║           🔍 last30days-skill-wrap Demo                  ║
║   AI Research Skill · Reddit · X · YouTube · HN          ║
║   Polymarket · GitHub · Full Web                         ║
╚══════════════════════════════════════════════════════════╝
"""
    print(banner)


def print_configured_sources():
    """Print which sources are configured."""
    print("\n📡 Configured Sources:")
    for source in check_dependencies():
        print(f"   {source}")
    print()


def build_synthesis(topic: str, github_user: str | None, eli5: bool) -> str:
    """
    Simulate a synthesis result for demo purposes.
    In production, this would call the actual last30days-skill engine.
    """
    lines = []
    lines.append(f"=== last30days Research Brief ===")
    lines.append(f"Topic: {topic}")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"Sources: Reddit, X, YouTube, HN, Polymarket, GitHub, Web")
    lines.append("")
    lines.append("─" * 60)
    lines.append("")

    # Simulated synthesis structure
    lines.append("📌 Summary")
    lines.append(f"  '{topic}' is a trending topic with significant community")
    lines.append(f"  discussion across multiple platforms in the last 30 days.")
    lines.append("")

    lines.append("🔬 Key Findings")
    lines.append(f"  • Reddit: Multiple threads with high engagement (500-1500+ upvotes)")
    lines.append(f"  • X/Twitter: Hot takes, expert threads, and breaking reactions")
    lines.append(f"  • YouTube: Deep dives and reaction videos with full transcripts")
    lines.append(f"  • Hacker News: Technical discussions with 500+ points")
    lines.append(f"  • Polymarket: Prediction markets showing real-money sentiment")
    lines.append(f"  • GitHub: Active development, star growth, release activity")
    lines.append("")

    if github_user:
        lines.append("👤 Person Mode (GitHub)")
        lines.append(f"  GitHub user: {github_user}")
        lines.append(f"  • Recent PRs merged across active repositories")
        lines.append(f"  • Open issues and feature requests")
        lines.append(f"  • Release notes for recent versions")
        lines.append("")

    if eli5:
        lines.append("📝 ELI5 Summary")
        lines.append(f"  In simple terms: people are talking about '{topic}'")
        lines.append(f"  because it's relevant to what's happening right now.")
        lines.append(f"  The community has strong opinions and real data to back them up.")
        lines.append("")

    lines.append("─" * 60)
    lines.append("")
    lines.append("📚 Top Sources")
    lines.append("  • Reddit: r/[relevant_subreddit] — [title] (X upvotes)")
    lines.append("  • X: @[handle] — [tweet excerpt]")
    lines.append("  • YouTube: [channel] — [video title]")
    lines.append("  • HN: [title] — [points] points, [comments] comments")
    lines.append("  • Polymarket: [question] — [odds]% odds")
    lines.append("  • GitHub: [repo] — [stars] stars, [activity] activity")
    lines.append("")
    lines.append("─" * 60)
    lines.append("")
    lines.append("💡 Best Takes")
    lines.append('  • "This is the most significant development in [field] this month."')
    lines.append('  • "[Witty one-liner from top Reddit comment]"')
    lines.append("")

    return "\n".join(lines)


def save_markdown(topic: str, content: str, save_dir: Path) -> Path:
    """Save synthesis to markdown file."""
    slug = topic.lower().replace(" ", "-").replace("vs", "vs").replace("?", "")[:50]
    filename = f"{slug}-raw.md"
    filepath = save_dir / filename
    filepath.write_text(content, encoding="utf-8")
    return filepath


def save_html(topic: str, content: str, save_dir: Path) -> Path:
    """Save synthesis as shareable HTML brief."""
    slug = topic.lower().replace(" ", "-").replace("vs", "vs").replace("?", "")[:50]
    filename = f"{slug}-brief.html"
    filepath = save_dir / filename

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>last30days Brief: {topic}</title>
  <style>
    :root {{
      --bg: #0d1117;
      --bg-secondary: #161b22;
      --border: #30363d;
      --text: #e6edf3;
      --text-secondary: #8b949e;
      --accent: #a371f7;
      --accent-bg: #1f2937;
      --code-bg: #1c2128;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
      line-height: 1.6;
    }}
    @media (prefers-color-scheme: light) {{
      :root {{
        --bg: #ffffff;
        --bg-secondary: #f6f8fa;
        --border: #d0d7de;
        --text: #1f2328;
        --text-secondary: #656d76;
        --accent: #8250df;
        --accent-bg: #f6f8fa;
        --code-bg: #f6f8fa;
      }}
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ background: var(--bg); color: var(--text); max-width: 800px; margin: 0 auto; padding: 2rem 1.5rem; }}
    .badge {{ display: inline-block; background: var(--accent-bg); color: var(--accent); border: 1px solid var(--border); padding: 0.25rem 0.75rem; border-radius: 2rem; font-size: 0.75rem; font-weight: 600; margin-bottom: 1rem; }}
    h1 {{ font-size: 1.75rem; margin-bottom: 0.25rem; }}
    .meta {{ color: var(--text-secondary); font-size: 0.875rem; margin-bottom: 1.5rem; }}
    .section {{ margin-bottom: 1.5rem; }}
    .section-title {{ font-size: 0.875rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-secondary); margin-bottom: 0.5rem; }}
    .source-block {{ background: var(--bg-secondary); border: 1px solid var(--border); border-radius: 6px; padding: 1rem; margin-bottom: 0.75rem; }}
    .source-block .platform {{ font-size: 0.75rem; font-weight: 700; color: var(--accent); text-transform: uppercase; margin-bottom: 0.25rem; }}
    .source-block .title {{ font-weight: 600; margin-bottom: 0.25rem; }}
    .source-block .meta {{ font-size: 0.8rem; color: var(--text-secondary); margin: 0; }}
    code {{ background: var(--code-bg); padding: 0.1rem 0.4rem; border-radius: 4px; font-family: 'JetBrains Mono', 'Fira Code', monospace; font-size: 0.875em; }}
    pre {{ background: var(--code-bg); border: 1px solid var(--border); border-radius: 6px; padding: 1rem; overflow-x: auto; font-size: 0.875rem; }}
    .footer {{ margin-top: 3rem; padding-top: 1rem; border-top: 1px solid var(--border); font-size: 0.75rem; color: var(--text-secondary); text-align: center; }}
    hr {{ border: none; border-top: 1px solid var(--border); margin: 1.5rem 0; }}
  </style>
</head>
<body>
  <span class="badge">🔍 last30days Research Brief</span>
  <h1>{topic}</h1>
  <p class="meta">Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} · Last 30 days · Multi-source synthesis</p>

  <div class="section">
    <div class="section-title">📌 Summary</div>
    <p>'{topic}' is a trending topic with significant community discussion across multiple platforms in the last 30 days.</p>
  </div>

  <div class="section">
    <div class="section-title">🔬 Key Findings</div>
    <div class="source-block">
      <div class="platform">Reddit</div>
      <div class="title">Multiple threads with 500-1500+ upvotes</div>
      <div class="meta">r/[relevant_subreddit] · High engagement community discussion</div>
    </div>
    <div class="source-block">
      <div class="platform">X / Twitter</div>
      <div class="title">Hot takes, expert threads, breaking reactions</div>
      <div class="meta">@[handle] · First to know, first to argue</div>
    </div>
    <div class="source-block">
      <div class="platform">YouTube</div>
      <div class="title">Deep dives and reaction videos with full transcripts</div>
      <div class="meta">[channel] · 45-minute deep dives distilled to key quotes</div>
    </div>
    <div class="source-block">
      <div class="platform">Hacker News</div>
      <div class="title">Technical discussions</div>
      <div class="meta">500+ points, active comment threads</div>
    </div>
    <div class="source-block">
      <div class="platform">Polymarket</div>
      <div class="title">Prediction markets with real-money sentiment</div>
      <div class="meta">[question] · [odds]% odds backed by $66K+ volume</div>
    </div>
    <div class="source-block">
      <div class="platform">GitHub</div>
      <div class="title">Active development and release activity</div>
      <div class="meta">[stars] stars · [PRs] PRs merged this month</div>
    </div>
  </div>

  <div class="section">
    <div class="section-title">💡 Best Takes</div>
    <div class="source-block">
      <div class="title">"This is the most significant development in [field] this month."</div>
      <div class="meta">— [platform] · [upvotes] upvotes</div>
    </div>
    <div class="source-block">
      <div class="title">"[Witty one-liner from top comment]"</div>
      <div class="meta">— [platform] · [engagement]</div>
    </div>
  </div>

  <div class="section">
    <div class="section-title">📚 Sources</div>
    <p style="color: var(--text-secondary); font-size: 0.875rem;">
      Reddit · X/Twitter · YouTube · Hacker News · Polymarket · GitHub · Web
    </p>
  </div>

  <div class="footer">
    <p>🔍 <strong>last30days</strong> · Research powered by community signals, not editors</p>
    <p>Topic: {topic} · Generated {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} · <a href="#" style="color: var(--accent);">Re-run research →</a></p>
  </div>
</body>
</html>"""

    filepath.write_text(html, encoding="utf-8")
    return filepath


def main():
    parser = argparse.ArgumentParser(
        description="last30days-skill-wrap Demo — AI research across Reddit, X, YouTube, HN, Polymarket, and the full web.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python demo.py "Peter Steinberger"
  python demo.py "OpenAI vs Anthropic" --emit html
  python demo.py "Universal Epic Universe" --save-dir ~/research/
  python demo.py "Nano Banana Pro" --eli5
  python demo.py "steipete" --github-user steipete

Environment variables (optional):
  SCRAPECREATORS_API_KEY   TikTok/Instagram/Threads/Pinterest API
  OPENROUTER_API_KEY        Perplexity Sonar API
  BRAVE_SEARCH_KEY          Brave Search API (2000 free/month)
  XAI_API_KEY               x-ai.com API
"""
    )
    parser.add_argument("topic", nargs="+", help="Research topic (person, company, product, 'X vs Y')")
    parser.add_argument("--emit", choices=["markdown", "html"], default="markdown", help="Output format (default: markdown)")
    parser.add_argument("--save-dir", type=Path, default=DEFAULT_SAVE_DIR, help=f"Directory to save research files (default: {DEFAULT_SAVE_DIR})")
    parser.add_argument("--save-suffix", type=str, default="", help="Suffix to append to saved filename")
    parser.add_argument("--eli5", action="store_true", help="Also output ELI5 (plain language) summary")
    parser.add_argument("--github-user", type=str, default=None, help="GitHub username for person-mode research")
    parser.add_argument("--competitors", action="store_true", help="Auto-discover and compare competitors")
    parser.add_argument("--open", action="store_true", help="Open the saved file in browser")
    parser.add_argument("--list-sources", action="store_true", help="List configured sources and exit")
    parser.add_argument("--version", action="version", version="last30days-skill-wrap v1.0.0")

    args = parser.parse_args()
    topic = " ".join(args.topic)

    print_banner()

    if args.list_sources:
        print_configured_sources()
        return

    print(f"🔍 Researching: {topic}")
    if args.github_user:
        print(f"   GitHub user: {args.github_user}")
    if args.eli5:
        print("   Mode: ELI5 (plain language)")
    print()

    # Build synthesis (demo mode — shows structure)
    content = build_synthesis(topic, args.github_user, args.eli5)

    # Save file
    args.save_dir.mkdir(parents=True, exist_ok=True)

    if args.emit == "html":
        output_path = save_html(topic, content, args.save_dir)
        print(f"✅ HTML brief saved to: {output_path}")
    else:
        output_path = save_markdown(topic, content, args.save_dir)
        print(f"✅ Markdown brief saved to: {output_path}")

    # Print to console
    print()
    print(content)

    if args.open:
        webbrowser.open(f"file://{output_path.resolve()}")

    print()
    print_configured_sources()


if __name__ == "__main__":
    main()