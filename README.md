# last30days-skill-wrap

<div align="center">

**[English](#english) · [中文](#中文)**

</div>

---

## English

<h1 align="center">🔍 last30days-skill-wrap</h1>

<p align="center">
  <strong>AI Agent Research Skill — Reddit · X · YouTube · HN · Polymarket · Full Web</strong>
  <br />
  <em>Search what real people actually think, vote on, and bet on — not what editors curate.</em>
</p>

<p align="center">
  <a href="https://github.com/mvanhorn/last30days-skill">
    <img src="https://img.shields.io/badge/Source-mvanhorn/last30days--skill-6f42c1?style=for-the-badge&logo=github" alt="Source Repo" />
  </a>
  <img src="https://img.shields.io/badge/Python-3.12%2B-3776ab?style=for-the-badge&logo=python&logoColor=ffd43b" alt="Python 3.12+" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT License" />
</p>

---

### 🎯 What Is This?

**last30days-skill-wrap** is a Python/CLI wrapper around the [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) AI research engine. It lets you research any topic — person, company, product, technology, "X vs Y" — by aggregating signals from Reddit, X/Twitter, YouTube, Hacker News, Polymarket, GitHub, and the open web, then synthesizing everything into one concise brief.

No more tab-by-tab, thread-by-thread manual research. One command, one brief.

---

### ✨ Features

| Feature | Description |
|---------|-------------|
| 🔍 **Multi-source search** | Reddit, X, YouTube, HN, Polymarket, GitHub, TikTok, Bluesky, Threads, Pinterest, web |
| 📊 **People-scored ranking** | Results ranked by upvotes, likes, engagement — not SEO |
| 💰 **Polymarket odds** | Real-money prediction market signals (96% confidence examples) |
| 🎬 **YouTube transcripts** | Full transcripts searched, not just titles |
| 🤖 **AI synthesis** | One brief combining all sources, cited and ranked |
| 📱 **Shareable HTML** | Export a self-contained, dark-mode, print-friendly HTML brief |
| 👤 **Person mode** | Resolve a person to their GitHub, X handles, subreddits — show what they're shipping |
| ⚖️ **Comparison mode** | Compare tools, companies, products side-by-side in a single run |
| 📈 **Trend monitoring** | SQLite-backed watchlist with scheduled runs and Slack/webhook alerts |
| 📝 **ELI5 mode** | Rewrite synthesis in plain language — no jargon |

---

### 📦 Installation

```bash
# Clone this repo
git clone https://github.com/q15004040209-creator/last30days-skill-wrap.git
cd last30days-skill-wrap

# Install dependencies
pip install -e .

# Or install from source
pip install requests python-dotenv
```

---

### 🚀 Quick Start

```bash
# Basic research
python demo.py "Peter Steinberger"

# Compare two topics
python demo.py "OpenAI vs Anthropic"

# Export as HTML
python demo.py "Universal Epic Universe" --emit html

# Save to custom directory
python demo.py "AI agents" --save-dir ~/research/

# ELI5 mode
python demo.py "Nano Banana Pro prompting" --eli5

# Person mode (GitHub + social)
python demo.py "Peter Steinberger" --github-user steipete

# With API keys (optional)
export SCRAPECREATORS_API_KEY=your_key_here
export XAI_API_KEY=your_key_here
python demo.py "your topic"
```

---

### 🔑 API Keys (Optional)

| Source | Key | Required |
|--------|-----|----------|
| Reddit + HN + Polymarket + GitHub | Nothing | ❌ Free |
| X / Twitter | Browser login | ❌ Free |
| YouTube | `yt-dlp` | ❌ Free |
| TikTok + Instagram + Threads + Pinterest | `SCRAPECREATORS_API_KEY` | ✅ PAYG |
| Perplexity Sonar | `OPENROUTER_API_KEY` | ✅ PAYG |
| Web search | `BRAVE_SEARCH_KEY` | ✅ 2K free/month |

---

### 🗂️ Project Structure

```
last30days-skill-wrap/
├── README.md              # This file (bilingual)
├── demo.py                # CLI demo script
├── requirements.txt       # Python dependencies
├── SKILL.md              # Skill specification
└── docs/
    └── CONFIG.md          # Full configuration guide
```

---

### 🧪 Demo Output Example

```
$ python demo.py "OpenClaw"

=== last30days Research Brief ===
Topic: OpenClaw
Sources: Reddit, X, YouTube, HN, Polymarket, GitHub, Web

Synthesis:
OpenClaw is a cross-device AI agent executor with 351K+ GitHub stars...
- r/ClaudeCode: 569 upvotes debating OpenClaw vs third-party agents
- @steipete: Building "LobsterOS" for cross-device agent control
- GitHub: 351K stars, live, 23 PRs merged at 85% merge rate
- Polymarket: "Will OpenClaw release mobile client?" 86% Yes

Sources cited:
- Reddit (r/ClaudeCode, r/openclaw)
- X (@steipete, @IMJustinBrooke)
- GitHub (openclaw/openclaw)
- Polymarket

Saved to: ~/Documents/Last30Days/openclaw-raw.md
```

---

### 📜 License

MIT License — see [LICENSE](LICENSE) for details.

This project wraps [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) (MIT Licensed).

---

<hr />

## 中文

<h1 align="center">🔍 last30days-skill-wrap</h1>

<p align="center">
  <strong>AI 智能研究技能 — Reddit · X · YouTube · HN · Polymarket · 全网搜索</strong>
  <br />
  <em>研究真实人们在点赞、投票、投注的内容，而不是编辑筛选的内容。</em>
</p>

<p align="center">
  <a href="https://github.com/mvanhorn/last30days-skill">
    <img src="https://img.shields.io/badge/来源-mvanhorn/last30days--skill-6f42c1?style=for-the-badge&logo=github" alt="来源仓库" />
  </a>
  <img src="https://img.shields.io/badge/Python-3.12%2B-3776ab?style=for-the-badge&logo=python&logoColor=ffd43b" alt="Python 3.12+" />
  <img src="https://img.shields.io/badge/许可证-MIT-green?style=for-the-badge" alt="MIT 许可证" />
</p>

---

### 🎯 这是什么？

**last30days-skill-wrap** 是 [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) AI 研究引擎的 Python/CLI 封装包。它让你可以研究任何话题——人物、公司、产品、技术、"X vs Y"对比——通过聚合 Reddit、X/Twitter、YouTube、Hacker News、Polymarket、GitHub 和全网的信息，然后综合成一份简洁的研究简报。

不再需要逐个标签页、逐个帖子地手动研究。一条命令，一份简报。

---

### ✨ 功能特点

| 功能 | 描述 |
|------|------|
| 🔍 **多平台搜索** | Reddit、X、YouTube、HN、Polymarket、GitHub、TikTok、Bluesky、Threads、Pinterest、全网 |
| 📊 **民众评分排名** | 按点赞、投票、参与度排名，而非 SEO |
| 💰 **Polymarket 赔率** | 真金白银预测市场信号（96% 置信度示例） |
| 🎬 **YouTube 字幕全文** | 搜索完整字幕，而非仅标题 |
| 🤖 **AI 综合整理** | 融合所有来源、含引用和排名的一份简报 |
| 📱 **可分享 HTML** | 导出自包含、暗色模式、可打印的 HTML 简报 |
| 👤 **人物模式** | 解析人物对应的 GitHub、X 账号、subreddit — 展示他们的最新动态 |
| ⚖️ **对比模式** | 单次运行对比工具、公司、产品 |
| 📈 **趋势监控** | SQLite 支持的观察列表，支持定时运行和 Slack/webhook 提醒 |
| 📝 **ELI5 模式** | 用通俗语言重写综合报告 — 无行话 |

---

### 📦 安装

```bash
# 克隆本仓库
git clone https://github.com/q15004040209-creator/last30days-skill-wrap.git
cd last30days-skill-wrap

# 安装依赖
pip install -e .

# 或从源码安装
pip install requests python-dotenv
```

---

### 🚀 快速开始

```bash
# 基础研究
python demo.py "Peter Steinberger"

# 对比两个话题
python demo.py "OpenAI vs Anthropic"

# 导出为 HTML
python demo.py "Universal Epic Universe" --emit html

# 保存到自定义目录
python demo.py "AI agents" --save-dir ~/research/

# ELI5 模式
python demo.py "Nano Banana Pro prompting" --eli5

# 人物模式（GitHub + 社交）
python demo.py "Peter Steinberger" --github-user steipete

# 使用 API key（可选）
export SCRAPECREATORS_API_KEY=your_key_here
export XAI_API_KEY=your_key_here
python demo.py "your topic"
```

---

### 🔑 API 密钥（可选）

| 来源 | 密钥 | 必须 |
|------|------|------|
| Reddit + HN + Polymarket + GitHub | 无 | ❌ 免费 |
| X / Twitter | 浏览器登录 | ❌ 免费 |
| YouTube | `yt-dlp` | ❌ 免费 |
| TikTok + Instagram + Threads + Pinterest | `SCRAPECREATORS_API_KEY` | ✅ 按量付费 |
| Perplexity Sonar | `OPENROUTER_API_KEY` | ✅ 按量付费 |
| 网页搜索 | `BRAVE_SEARCH_KEY` | ✅ 每月 2000 次免费 |

---

### 🗂️ 项目结构

```
last30days-skill-wrap/
├── README.md              # 本文件（双语）
├── demo.py                # CLI 示例脚本
├── requirements.txt       # Python 依赖
├── SKILL.md              # 技能规格说明
└── docs/
    └── CONFIG.md          # 完整配置指南
```

---

### 🧪 示例输出

```
$ python demo.py "OpenClaw"

=== last30days 研究简报 ===
主题: OpenClaw
来源: Reddit, X, YouTube, HN, Polymarket, GitHub, Web

综合分析:
OpenClaw 是一个跨设备 AI agent 执行器，GitHub 星标 351K+...
- r/ClaudeCode: 569 票讨论 OpenClaw 与第三方 agent 的争议
- @steipete: 正在开发 "LobsterOS" 实现跨设备 agent 控制
- GitHub: 351K 星标，23 个 PR 已合并，合并率 85%
- Polymarket: "OpenClaw 会发布移动端吗？" 86% 是

引用来源:
- Reddit (r/ClaudeCode, r/openclaw)
- X (@steipete, @IMJustinBrooke)
- GitHub (openclaw/openclaw)
- Polymarket

已保存至: ~/Documents/Last30Days/openclaw-raw.md
```

---

### 📜 许可证

MIT 许可证 — 详见 [LICENSE](LICENSE)。

本项目是对 [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)（MIT 许可证）的封装。

---

<p align="center">
  <strong>⭐ Star 本项目 · 关注 AI 研究自动化</strong>
</p>