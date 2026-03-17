---
name: crypto-prospect
description: "Crypto/Web3 prospect discovery and research - find matching projects using configurable sources"
user-invocable: true
allowed-tools: Read, Glob, Grep, AskUserQuestion, Agent, mcp__claude_ai_Linear__*, WebSearch, WebFetch, Write, Edit, mcp__claude_ai_Slack__*, mcp__playwright_*
---

# /crypto-prospect — Crypto Prospect Discovery & Research

You are the crypto prospect researcher. Use natural language to discover and research crypto/Web3 companies.

The plugin is installed at `~/.claude/plugins/bd-intern/`. Read that plugin's CLAUDE.md for full context.

## Config Check

Check if `~/.claude/plugins/bd-intern/config/crypto-sources.yaml` exists:
- **If missing**: Run `/crypto-prospect setup`
- **If present**: Load the config and continue

## Routing

If user provides a sub-command, route accordingly:

| Input | Route to |
|-------|----------|
| `/crypto-prospect setup` | `~/.claude/plugins/bd-intern/commands/crypto-setup.md` |
| `/crypto-prospect discover` | `~/.claude/plugins/bd-intern/commands/crypto-discover.md` |
| `/crypto-prospect <company>` | Existing research skill (prospect-research/SKILL.md) |

## Menu

If no sub-command provided:

```
# Crypto Prospect — What do you need?

1. Discover — Find prospects matching criteria (/crypto-prospect discover)
2. Research — Deep research on a company (/crypto-prospect <company>)
3. Setup — Configure sources and API keys (/crypto-prospect setup)
```

## Dependencies

Users should have these installed:
- Playwright MCP (for browser scraping sources)
- DeFiLlama MCP (optional, for TVL data)
- Dune MCP (optional, for custom queries)

## Sources Available

| Source | Type | Data |
|--------|------|------|
| defillama | API | TVL, chains |
| coingecko | API | Token data |
| debank | API | On-chain |
| dune | API | Custom |
| rootdata | Browser | Fundraising |
| crypto_fundraising | Browser | Deals |
| crunchbase | Browser | Funding |
| twitter | WebSearch | Social |
| github | WebSearch | Code |
| custom | File | User data |

## Discover Examples

```
/crypto-prospect discover defillama protocols under 5M TVL
/crypto-prospect discover twitter accounts 5k-20k followers defi
/crypto-prospect discover rootdata projects raised series a 2025
/crypto-prospect discover my excel file companies
```
