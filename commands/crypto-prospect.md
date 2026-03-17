# /crypto-prospect — Crypto Prospect Discovery

Integrated into bd-intern. Routes to discover or research.

## Routing

| Input | Route to |
|-------|----------|
| `/crypto-prospect discover <criteria>` | `commands/crypto-discover.md` |
| `/crypto-prospect setup` | `commands/crypto-setup.md` |
| `/crypto-prospect <company>` | `skills/prospect-research/SKILL.md` |

## Quick Access via bd-intern

You can also access this via:
- `/bd-intern discover <criteria>`
- `/bd-intern crypto`

## Sources

10 sources available:
- defillama, coingecko, debank, dune (API)
- rootdata, crypto_fundraising, crunchbase (Browser)
- twitter, github (WebSearch)
- custom (Excel, Sheets, Notion)

## Examples

```
/crypto-prospect discover defillama protocols under 5M TVL
/crypto-prospect discover twitter accounts 5k-20k followers defi
/crypto-prospect discover rootdata projects raised 2025 series a
```