---
name: crypto-prospect
description: Crypto/Web3 prospect discovery and research - find matching projects using configurable sources
version: 1.0.0
---

# Crypto Prospect Research

## Overview

A modular prospect discovery and research system for crypto/Web3 companies. Uses natural language to discover prospects from multiple sources, then research them in depth.

## Core Components

| Component | Command | Purpose |
|-----------|---------|---------|
| **DISCOVER** | `/crypto-prospect discover <criteria>` | Find prospects matching criteria |
| **RESEARCH** | `/crypto-prospect <company>` | Deep research on a company |

## The Rule

**At least ONE source must be specified** in discover queries. Multiple filters are optional.

```
Valid:   "defillama projects under 5M TVL"
Valid:   "twitter accounts with <5000 followers"
Invalid: "find crypto projects" → AI prompts for source
```

## Sources (10 Total)

### API Sources
| Source | Type | Data | Free |
|--------|------|------|------|
| `defillama` | API | TVL, chains, protocols | ✅ |
| `coingecko` | API | Token prices, market cap | ✅ |
| `debank` | API | On-chain portfolios | ✅ (limited) |
| `dune` | API | Custom queries | ✅ (credits) |

### Browser/Scraper Sources
| Source | Type | Data | Free |
|--------|------|------|------|
| `rootdata` | Browser | Projects, fundraising | ✅ |
| `crypto_fundraising` | Browser | Deal flow, investors | ✅ |
| `crunchbase` | Browser | Funding, stage | ✅ |
| `twitter` | WebSearch | Followers, engagement | ✅ |

### Custom Sources
| Source | Type | Data |
|--------|------|------|
| `custom` | User files | Excel, Sheets, Notion, API |

## Commands

### Discover
```
/crypto-prospect discover <criteria with source>

Examples:
/crypto-prospect discover defillama protocols under 5M TVL on Arbitrum
/crypto-prospect discover coingecko tokens 1M-10M market cap
/crypto-prospect discover twitter accounts 5k-20k followers defi
/crypto-prospect discover rootdata projects raised 2025 series a
/crypto-prospect discover crunchbase series b companies
/crypto-prospect discover crypto_fundraising rounds under 10M this year
/crypto-prospect discover my excel file companies on Ethereum
```

### Research
```
/crypto-prospect <company>     # Deep research
/crypto-prospect compare A B   # Compare two companies
```

## Configuration

Sources are configured in `config/crypto-sources.yaml`. Run `/crypto-prospect setup` to configure.

### Required Dependencies

Users must install these MCPs/tools:
- **Playwright MCP** - For browser scraping (rootdata, crunchbase, crypto_fundraising)
- **DeFiLlama MCP** - For TVL data (optional, can use free API)
- **Dune MCP** - For custom queries (optional)

### API Keys (Optional)

During setup, prompt for these keys (free tiers work without):
- CoinGecko API key
- DeBank API key
- Dune API key
- RootData API key

## Rate Limiting

Rate limiting is automatic based on source type:

| Source Type | Delay |
|-------------|-------|
| API | 500ms |
| WebSearch | 1000ms |
| Browser | 2000ms |

## Research Phases

When researching a company, these phases run:

1. **Company Overview** - Website, about, team
2. **Technical** - GitHub, docs, tech stack
3. **On-Chain** - DeFiLlama, DeBank data
4. **Social** - Twitter, community
5. **Fundraising** - RootData, CryptoFundraising
6. **Verify** - Cross-reference data

## Custom Sources

Users can add their own data sources:

```yaml
custom_sources:
  - name: "event_attendees"
    type: "excel"
    path: "~/events.xlsx"
    schema:
      company: "Company Name"
      website: "URL"
```

See `references/source_templates/` for full templates.
