# /crypto-prospect discover — Find Prospects

## Purpose

Discover potential prospects using natural language with at least one source.

## Step 0: Load Config

Read `config/crypto-sources.yaml` from the plugin directory. Load:
- Enabled sources
- API keys
- Rate limiting settings
- Custom sources

If config is missing, run `/crypto-prospect setup` first.

## Step 1: Parse User Input

User must specify at least ONE source. Extract:
1. **Source(s)** - Required (defillama, coingecko, twitter, rootdata, etc.)
2. **Filters** - Optional (TVL, followers, category, chain, etc.)

If no source specified:
```
"Please specify a source. For example: 'defillama projects under 5M TVL' or 
'twitter accounts 5k-20k followers in DeFi'. Available sources: defillama, 
coingecko, debank, dune, rootdata, crypto_fundraising, twitter, github, 
crunchbase, or your custom source."
```

## Step 2: Execute Discovery

Use whichever web search/fetch tool is available on your platform:

### Available Web Tools (Use whichever is available)

| Platform | Tool | Use For |
|----------|------|---------|
| Claude/Cline | `WebFetch` | Direct API calls, fetching URLs |
| Claude/Cline | `WebSearch` | Web searches |
| Gemini | `google_web_search` | Web searches (primary) |
| Gemini | `web_fetch` | Fetching specific URLs (if available) |

### For defillama source:

**If you have WebFetch (Claude):**
```
1. Use WebFetch to get: https://api.llama.fi/protocols
2. Parse the JSON response
3. Apply filters from user input
4. Return filtered results
```

**If you have google_web_search (Gemini):**
```
1. Use google_web_search to find: "defillama protocols TVL [filters]"
2. Example: "defillama protocols over 50 million TVL"
3. Parse the search results
4. Return filtered results
```

**If you have web_fetch (Gemini):**
```
1. Use web_fetch to get: https://api.llama.fi/protocols
2. Parse the JSON response
3. Apply filters
4. Return filtered results
```

### For twitter source:

**If you have WebSearch (Claude):**
```
1. Use WebSearch to find: "site:twitter.com [company] OR [protocol]"
2. Or search for "[protocol] twitter followers"
```

**If you have google_web_search (Gemini):**
```
1. Use google_web_search to find: "[protocol] twitter followers defi"
2. Parse the search results for follower counts
```

### For rootdata source:

**If you have WebFetch (Claude):**
```
1. Use WebFetch on specific rootdata pages
2. Example: https://www.rootdata.com/project/[name]
```

**If you have google_web_search (Gemini):**
```
1. Use google_web_search to find: "site:rootdata.com [filters]"
2. Example: "site:rootdata.com Series A 2025"
```

## Step 3: Parse and Filter Results

Apply these common filters:
- TVL: tvl_min, tvl_max (parse "100M", "5K", etc.)
- Chain: ethereum, arbitrum, optimism, base, solana, etc.
- Category: defi, lending, nft, gaming, infrastructure
- Followers: followers_min, followers_max
- Stage: seed, series_a, series_b, series_c

## Step 4: Output Results

Format:

```
# Discover Results: "<user criteria>"
# Source: <source> | Filters: <matched filters>

| # | Project | [Key Data 1] | [Key Data 2] | Matched Filters |
|---|---------|--------------|--------------|----------------|
| 1 | Project A | $4.2M | Arbitrum | TVL ✓, Chain ✓ |
| 2 | Project B | $2.1M | Arbitrum | TVL ✓, Chain ✓ |

# X results found (showed all X)
# Matched on: <list of filters that matched>
```

## Step 5: Offer Next Steps

After results:
- "Type a number or name to research any project in depth"
- "Use /crypto-prospect discover to find more prospects"

## Error Handling

| Scenario | Response |
|----------|----------|
| No source specified | Prompt for source |
| Source disabled in config | Offer to enable or skip |
| No results found | Suggest relaxing filters |
| Rate limited | Wait and retry |
| API error | Try alternative source, report error |

## Rate Limiting

- WebFetch (Claude): 2 second delay between requests
- WebSearch (Claude): 1 second delay
- google_web_search (Gemini): 1 second delay
- web_fetch (Gemini): 2 second delay
- Use delays to avoid rate limiting

## Platform-Specific Notes

### Claude/Cline
- Use `WebFetch` for direct API calls
- Use `WebSearch` for web searches

### Gemini
- Use `google_web_search` for all web queries (primary)
- Use `web_fetch` for fetching specific URLs if available
- Gemini has built-in web search capabilities
- No additional setup required
