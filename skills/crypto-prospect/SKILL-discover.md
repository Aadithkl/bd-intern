---
name: crypto-prospect-discover
description: Discover crypto/Web3 prospects using natural language with configurable sources
version: 1.0.0
---

# Crypto Prospect Discover

## Purpose

Find potential crypto/Web3 prospects using natural language. Must specify at least one source.

## Step 0: Load Configuration

Read `config/crypto-sources.yaml` from the plugin directory. If missing, run `/crypto-prospect setup`.

Load:
- Enabled sources
- API keys
- Custom sources
- Rate limiting settings

## Step 1: Parse Input

Extract from user input:
1. **Source** (required) - defillama, coingecko, twitter, rootdata, etc.
2. **Filters** (optional) - TVL, followers, chain, category, etc.

If no source found:
```
"Please specify a source. Examples:
- 'defillama protocols under 5M TVL on Arbitrum'
- 'twitter accounts 5k-20k followers in DeFi'
- 'rootdata projects raised series a this year'

Available sources: defillama, coingecko, debank, dune, twitter, github, 
rootdata, crypto_fundraising, crunchbase, or your custom source."
```

## Step 2: Identify Sources

Map input to source types:

| Source | Type | Data Retrieved |
|--------|------|----------------|
| defillama | API | TVL, chains, categories |
| coingecko | API | Market cap, token data |
| debank | API | On-chain portfolios |
| dune | API | Custom queries |
| twitter | WebSearch | Followers, activity |
| github | WebSearch | Code activity |
| rootdata | Browser | Projects, fundraising |
| crypto_fundraising | Browser | Deals, rounds |
| crunchbase | Browser | Funding, stage |
| custom_* | File | User data |

## Step 3: Build & Execute Queries

### MANDATORY: Source-First Execution
**NEVER** start with a general Google Web Search for discovery. Always lead with the primary domain:
1. **RootData**: Navigate to `https://www.rootdata.com/` for project lists and funding details.
2. **Crypto-Fundraising**: Navigate to `https://crypto-fundraising.info/deal-flow/` for the latest rounds.
3. **AgentCash (twit.sh)**: Use for **EXACT** real-time social metrics. Do not report "ranges" from search snippets.

### For API Sources (defillama, coingecko, debank)
```
Query: GET /api/protocols?chain={chain}&tvl_max={tvl_max}
Delay: 500ms between requests
```

### For Social Metrics (twitter, github)
**High-Signal Path**: Use AgentCash `twit.sh` endpoint `/users/by/username`.
**Fallback Path**: Only use WebSearch if API fails, and clearly label as "Estimated from Search."

### For Browser Sources (rootdata, crunchbase, crypto_fundraising)
```
Method: WebFetch or Playwright MCP
URL: https://rootdata.com/project/{name}
Delay: 2000ms between pages
```

### For Custom Sources

```
Excel: Read file, filter by columns
Sheets: API call to Google Sheets
```

## Step 4: Rate Limiting

Automatic delays based on source type:

| Source Type | Delay |
|-------------|-------|
| API | 500ms |
| WebSearch | 1000ms |
| Browser | 2000ms |
| Custom File | 0ms |

## Step 5: Process Results

### Single Source
Return results directly with matched filters.

### Multiple Sources
1. Query each source
2. Match by project name
3. Score by number of matching filters
4. Merge and rank

## Step 6: Output Format

```
# Discover Results: "<user input>"
# Source: <source> | Filters: <matched filters>

| # | Project | [Data 1] | [Data 2] | Matched Filters |
|---|---------|----------|----------|------------------|
| 1 | Project A | $4.2M | Arbitrum | TVL ✓, Chain ✓ |
| 2 | Project B | $2.1M | Arbitrum | TVL ✓, Chain ✓ |
| 3 | Protocol C | $1.5M | Ethereum | TVL ✓ |

# 3 results found
# Matched on: TVL < $5M, Chain = Arbitrum
```

## Step 7: Next Steps

Offer:
- "Type a number or name to research any project in depth"
- "Use /crypto-prospect discover to find more prospects"

## Error Handling

| Error | Response |
|-------|----------|
| No source specified | Prompt for source with examples |
| Source disabled | Offer to enable or skip |
| No results | Suggest relaxing filters |
| Rate limited | Wait, retry |
| API error | Try alternative, report |

## Custom Source Support

Users can add custom sources in config:

```yaml
custom_sources:
  - name: "event_attendees"
    type: "excel"
    path: "~/events.xlsx"
    schema:
      company: "Company Name"
      website: "URL"
```

Query custom sources:
```
/crypto-prospect discover my excel file companies on Ethereum
/crypto-prospect discover my sheets companies
```
