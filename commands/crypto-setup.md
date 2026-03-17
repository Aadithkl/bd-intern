# /crypto-prospect setup — Configure Sources

## Purpose

Interactive wizard to configure crypto-prospect sources, API keys, and custom data sources.

## Step 1: Welcome & Overview

```
# Crypto Prospect Setup

This wizard will help you configure your prospect discovery sources.

You'll need:
1. Enable/disable data sources
2. (Optional) Add API keys for premium access
3. (Optional) Add custom data sources

Let's get started.
```

## Step 2: Enable Sources

Ask user to enable/disable each source category:

```
## Data Sources

Please enable the sources you want to use for discovery:

### API Sources
- [ ] DeFiLlama (free, no key needed) - TVL, protocols
- [ ] CoinGecko (free tier available) - token data
- [ ] DeBank (free tier) - on-chain data
- [ ] Dune (2,500 free credits/month) - custom queries

### Browser/Scraper Sources
- [ ] RootData - fundraising data
- [ ] CryptoFundraising - deal flow
- [ ] Crunchbase - funding data

### Web Search Sources  
- [ ] Twitter/X - social data
- [ ] GitHub - code activity
```

## Step 3: API Keys (Optional)

For each enabled source that supports API keys:

```
## API Keys

Some sources offer better access with API keys. 
Keys are optional - free tiers work without them.

### CoinGecko (optional)
Get free key at: https://www.coingecko.com/en/api
Press Enter to skip if you don't have one.

### DeBank (optional)
Get free key at: https://debank.com/

### Dune (optional)
Get key at: https://dune.com/
Free: 2,500 credits/month

### RootData (optional)
Get key at: https://www.rootdata.com/Api
```

## Step 4: Custom Sources (Optional)

```
## Custom Data Sources

Do you have any custom data sources to add?

Examples:
- Excel file with event attendees
- Google Sheet with portfolio companies
- Notion database with leads
- API endpoint with company data

Please describe your data source, or press Enter to skip.
```

If user has custom source, guide them through the appropriate template.

## Step 5: Rate Limiting

```
## Rate Limiting

To avoid getting rate limited, we add delays between requests.

Default: 2000ms (2 seconds)
- Fast (1000ms) - may hit rate limits
- Normal (2000ms) - balanced
- Slow (3000ms) - safe for sensitive sources

Recommended: Normal (2000ms)
```

## Step 6: Save Configuration

Save to `config/crypto-sources.yaml`:

```yaml
sources:
  defillama:
    enabled: true
  # ... etc

api_keys:
  coingecko: "{user_input}"
  # ... etc

custom_sources:
  # ... user sources

rate_limiting:
  enabled: true
  delay_ms: 2000
```

## Step 7: Verify & Test

```
## Setup Complete

Your configuration has been saved to config/crypto-sources.yaml

Let's verify it works. Try:
/crypto-prospect discover defillama protocols under 5M TVL
```

## Required Dependencies

Inform user of required MCPs:

```
## Required Tools

To use all features, you'll need to install these MCPs:

1. Playwright MCP - for browser scraping
   Install: https://github.com/playwright/mcp
   
2. (Optional) DeFiLlama MCP - for TVL data
   Already available in most setups

3. (Optional) Dune MCP - for custom queries
   Install: https://github.com/duneanalytics/mcp
```

## Error Handling

| Scenario | Response |
|----------|----------|
| Config write fails | Show error, offer manual save |
| Invalid API key format | Warn but allow saving |
| MCP not installed | Show installation instructions |
