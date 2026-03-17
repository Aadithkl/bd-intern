# Requirements & External Services

This document lists all external services, APIs, and tools required for BD Intern to function fully.

## Table of Contents

1. [MCPs Required](#mcp-server)
2. [API Keys](#api-keys)
3. [Free Services](#free-services)
4. [Installation Guide](#installation-guide)

---

## MCP Server

| Service | Purpose | Required | Signup |
|---------|---------|----------|--------|
| **AgentCash** | Twitter/X search, people/company search, LinkedIn scraping, Google Maps, web scraping | Recommended | [agentcash.ai](https://agentcash.ai) |
| **Linear MCP** | Pipeline/CRM integration | Yes | Via OAuth (automatic) |
| **Playwright MCP** | Browser automation for scraping | Recommended | [github.com/playwright/mcp](https://github.com/playwright/mcp) |
| **DeFiLlama MCP** | TVL data | Optional | Optional |
| **Dune MCP** | Custom on-chain queries | Optional | [dune.com](https://dune.com) |

---

## API Keys

| Service | Purpose | Free Tier | Signup |
|---------|---------|-----------|--------|
| **CoinGecko** | Token prices, market cap | ✅ Free (30 calls/min) | [coingecko.com/api](https://www.coingecko.com/en/api) |
| **DeBank** | On-chain portfolios | ✅ Limited | [debank.com](https://debank.com) |
| **Dune Analytics** | Custom on-chain queries | 2,500 credits/mo | [dune.com](https://dune.com) |
| **RootData** | Fundraising data | ✅ Limited | [rootdata.com/Api](https://www.rootdata.com/Api) |
| **Crunchbase** | Funding stage | Limited | [crunchbase.com](https://crunchbase.com) |

---

## Free Services

These services work without API keys:

| Service | Purpose | Notes |
|---------|---------|-------|
| **DeFiLlama API** | TVL, protocol data | [defillama.com](https://defillama.com) |
| **crypto-fundraising.info** | Deal flow | Browser-based |
| **WebFetch** | Direct API calls | Built into Claude/Cline |
| **WebSearch / google_web_search** | Web searches | Built into platform |

---

## Installation Guide

### 1. AgentCash (Recommended)

```bash
# Sign up at https://agentcash.ai
# Get your API key from the dashboard

# Install via npx (for Claude/Cline):
npx agentcash@latest discover <origin>
```

Used for:
- Twitter/X search and scraping
- People/company search
- LinkedIn data
- Google Maps data
- Web scraping

### 2. Linear MCP

Automatically configured via OAuth when you first use pipeline commands. No manual setup required.

### 3. Playwright MCP

```bash
# Install via npx
npx playwright-mcp

# Or see: https://github.com/playwright/mcp
```

Used for:
- RootData scraping
- Crunchbase data
- crypto-fundraising.info browsing

### 4. Dune MCP (Optional)

```bash
# Sign up at https://dune.com
# Get API key from settings

# Install: https://github.com/duneanalytics/mcp
```

### 5. API Keys Configuration

Add keys to `config/crypto-sources.yaml`:

```yaml
api_keys:
  coingecko: "your-key-here"      # Optional
  debank: "your-key-here"         # Optional
  dune: "your-key-here"           # Required for Dune
  rootdata: "your-key-here"       # Optional
```

---

## Quick Reference

| Feature | Required Service |
|---------|------------------|
| Pipeline/CRM | Linear MCP |
| Twitter metrics | AgentCash |
| TVL data | DeFiLlama (free) |
| Token prices | CoinGecko (free) |
| Fundraising | RootData / crypto-fundraising.info |
| Browser scraping | Playwright MCP |
| Custom analytics | Dune |

---

## Notes

- **Free tiers work for most use cases** - CoinGecko, DeFiLlama, and crypto-fundraising.info have generous free tiers
- **AgentCash is pay-per-call** - Only charged when you use it, reasonable pricing
- **API keys are optional** - Everything works without them, just with lower rate limits
