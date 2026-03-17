# Source Manager
# Handles loading and querying all data sources

from typing import Dict, List, Any, Optional
import asyncio
import re
import time


class SourceManager:
    """Manages all data sources for prospect discovery"""

    def __init__(self, config: Dict):
        self.config = config
        self.sources = config.get("sources", {})
        self.custom_sources = config.get("custom_sources", [])
        self.rate_limiter = RateLimiter(
            delay_ms=config.get("rate_limiting", {}).get("delay_ms", 2000)
        )

    def get_enabled_sources(self) -> List[str]:
        """Return list of enabled source names"""
        return [
            name
            for name, settings in self.sources.items()
            if settings.get("enabled", False)
        ]

    def is_source_enabled(self, source_name: str) -> bool:
        """Check if a specific source is enabled"""
        return self.sources.get(source_name, {}).get("enabled", False)

    def get_source_type(self, source_name: str) -> str:
        """Get the query type for a source (api, websearch, browser, custom)"""
        source_types = {
            "defillama": "api",
            "coingecko": "api",
            "debank": "api",
            "dune": "api",
            "twitter": "websearch",
            "github": "websearch",
            "rootdata": "browser",
            "crypto_fundraising": "browser",
            "crunchbase": "browser",
        }
        return source_types.get(source_name, "custom")

    def get_rate_delay(self, source_name: str) -> int:
        """Get rate limit delay for source"""
        source_type = self.get_source_type(source_name)
        delays = {"api": 500, "websearch": 1000, "browser": 2000, "custom": 0}
        return delays.get(source_type, 1000)

    async def query_source(self, source_name: str, filters: Dict) -> List[Dict]:
        """Query a single source with filters"""
        if not self.is_source_enabled(source_name):
            return []

        delay = self.get_rate_delay(source_name)
        await asyncio.sleep(delay / 1000)  # Rate limiting

        source_type = self.get_source_type(source_name)

        if source_type == "api":
            return await self._query_api_source(source_name, filters)
        elif source_type == "websearch":
            return await self._query_websearch_source(source_name, filters)
        elif source_type == "browser":
            return await self._query_browser_source(source_name, filters)
        elif source_type == "custom":
            return await self._query_custom_source(source_name, filters)

        return []

    async def _query_api_source(self, source: str, filters: Dict) -> List[Dict]:
        """Query API-based sources"""
        if source == "defillama":
            return await self._query_defillama(filters)
        elif source == "coingecko":
            return await self._query_coingecko(filters)
        elif source == "debank":
            return await self._query_debank(filters)
        elif source == "dune":
            return await self._query_dune(filters)
        return []

    async def _query_defillama(self, filters: Dict) -> List[Dict]:
        """
        Query DeFiLlama for protocols.

        This method is designed to be called by an AI agent using WebFetch tool.
        The agent should:
        1. Use WebFetch to get https://api.llama.fi/protocols
        2. Parse the JSON response
        3. Apply filters (tvl_min, tvl_max, chain, category)
        4. Return filtered results

        Returns instructions for the AI agent to execute.
        """
        # Return the query parameters for AI to execute
        return {
            "query_type": "defillama_protocols",
            "url": "https://api.llama.fi/protocols",
            "filters": filters,
            "instructions": """
            Please execute this query:
            1. Use WebFetch to get: https://api.llama.fi/protocols
            2. Parse the JSON response
            3. Filter for protocols where:
               - tvl >= {tvl_min} (if specified)
               - tvl <= {tvl_max} (if specified)
               - chain contains '{chain}' (if specified)
               - category contains '{category}' (if specified)
            4. Return the matching protocols with: name, tvl, chain, category, url, twitter
            """.format(
                tvl_min=filters.get("tvl_min", 0),
                tvl_max=filters.get("tvl_max", "unlimited"),
                chain=filters.get("chain", ""),
                category=filters.get("category", ""),
            ),
        }

    async def _query_coingecko(self, filters: Dict) -> List[Dict]:
        """Query CoinGecko for tokens"""
        # TODO: Implement CoinGecko API integration
        # Free tier works without key, 30 calls/min
        return []

    async def _query_debank(self, filters: Dict) -> List[Dict]:
        """Query DeBank for portfolios"""
        # TODO: Implement DeBank API integration
        # Free tier limited
        return []

    async def _query_dune(self, filters: Dict) -> List[Dict]:
        """Query Dune for custom queries"""
        # TODO: Implement Dune API integration
        # Requires API key and credits
        return []

    async def _query_websearch_source(self, source: str, filters: Dict) -> List[Dict]:
        """Query web search sources (Twitter, GitHub)"""
        # Use WebSearch tool
        return []

    async def _query_browser_source(self, source: str, filters: Dict) -> List[Dict]:
        """Query browser-based sources (RootData, Crunchbase, etc.)"""
        # Use WebFetch or Playwright MCP
        return []

    async def _query_custom_source(self, source: str, filters: Dict) -> List[Dict]:
        """Query custom user sources (Excel, Sheets, etc.)"""
        # Parse user files
        return []

    async def discover(self, source: str, filters: Dict) -> List[Dict]:
        """Main discovery method"""
        return await self.query_source(source, filters)


class RateLimiter:
    """Rate limiter for API/web requests"""

    def __init__(self, delay_ms: int = 2000):
        self.delay_ms = delay_ms
        self.last_request = 0

    async def wait(self):
        """Wait if necessary to respect rate limits"""
        elapsed = time.time() - self.last_request
        if elapsed < self.delay_ms / 1000:
            await asyncio.sleep(self.delay_ms / 1000 - elapsed)
        self.last_request = time.time()


class QueryInterpreter:
    """Interprets natural language into source queries"""

    # Source keywords
    SOURCE_KEYWORDS = {
        "defillama": ["defillama", "tvl", "protocol"],
        "coingecko": ["coingecko", "token", "market cap", "coin"],
        "debank": ["debank", "on-chain", "portfolio", "holdings"],
        "dune": ["dune", "analytics", "query"],
        "twitter": ["twitter", "x.com", "followers", "tweet"],
        "github": ["github", "code", "repo", "commit"],
        "rootdata": ["rootdata", "fundraising", "raised"],
        "crypto_fundraising": ["fundraising", "deal", "round", "investors"],
        "crunchbase": ["crunchbase", "funding", "series"],
    }

    def __init__(self):
        pass

    def parse_input(self, user_input: str) -> Dict[str, Any]:
        """Parse natural language input into source and filters"""
        input_lower = user_input.lower()

        # Find source
        source = self._find_source(input_lower)

        # Extract filters
        filters = self._extract_filters(input_lower, source)

        return {"source": source, "filters": filters, "original_input": user_input}

    def _find_source(self, text: str) -> Optional[str]:
        """Find the primary source from input"""
        for source, keywords in self.SOURCE_KEYWORDS.items():
            for keyword in keywords:
                if keyword in text:
                    return source
        return None

    def _extract_filters(self, text: str, source: str) -> Dict:
        """Extract filter values from text"""
        filters = {}

        # TVL filters
        if "tvl" in text:
            # Handle "over" or ">" for minimum TVL
            if ">" in text or "over" in text or "more than" in text:
                match = re.search(r">\s*(\d+\.?\d*)([mkM])?", text)
                if match:
                    value = match.group(1)
                    multiplier = match.group(2).lower() if match.group(2) else ""
                    if multiplier == "m":
                        value = float(value) * 1000000
                    elif multiplier == "k":
                        value = float(value) * 1000
                    filters["tvl_min"] = float(value)

            # Handle "under" or "<" for maximum TVL
            if "under" in text or "<" in text:
                match = re.search(r"<\s*(\d+\.?\d*)([mkM])?", text)
                if match:
                    value = match.group(1)
                    multiplier = match.group(2).lower() if match.group(2) else ""
                    if multiplier == "m":
                        value = float(value) * 1000000
                    elif multiplier == "k":
                        value = float(value) * 1000
                    filters["tvl_max"] = float(value)

        # Chain filters
        chains = [
            "ethereum",
            "arbitrum",
            "optimism",
            "base",
            "solana",
            "avalanche",
            "polygon",
            "bsc",
            "avax",
        ]
        for chain in chains:
            if chain in text:
                filters["chain"] = chain
                break

        # Follower filters (twitter)
        if "followers" in text:
            if "<" in text or "under" in text or "less than" in text:
                match = re.search(r"(\d+\.?\d*)([kK])?", text)
                if match:
                    value = match.group(1)
                    if match.group(2):
                        value = float(value) * 1000
                    filters["followers_max"] = float(value)
            elif ">" in text or "over" in text or "more than" in text:
                match = re.search(r"(\d+\.?\d*)([kK])?", text)
                if match:
                    value = match.group(1)
                    if match.group(2):
                        value = float(value) * 1000
                    filters["followers_min"] = float(value)

        # Stage filters
        stages = ["seed", "series a", "series b", "series c"]
        for stage in stages:
            if stage in text:
                filters["stage"] = stage

        # Category filters
        categories = [
            "defi",
            "lending",
            "dex",
            "nft",
            "gaming",
            "infrastructure",
            "yield",
            "derivatives",
            "stablecoin",
        ]
        for cat in categories:
            if cat in text:
                filters["category"] = cat
                break

        return filters


class ResultMerger:
    """Merges and scores results from multiple sources"""

    def __init__(self):
        pass

    def merge_results(
        self, results_by_source: Dict[str, List[Dict]], filters: Dict
    ) -> List[Dict]:
        """Merge results from multiple sources"""
        all_results = []

        for source, results in results_by_source.items():
            for result in results:
                result["source"] = source
                all_results.append(result)

        # Score by matching filters
        for result in all_results:
            result["match_score"] = self._calculate_score(result, filters)

        # Sort by score
        all_results.sort(key=lambda x: x.get("match_score", 0), reverse=True)

        return all_results

    def _calculate_score(self, result: Dict, filters: Dict) -> float:
        """Calculate match score based on filters"""
        score = 0
        matched_filters = []

        for filter_name, filter_value in filters.items():
            if filter_name in result:
                if filter_name == "tvl_max":
                    if result.get("tvl", 0) <= filter_value:
                        score += 1
                        matched_filters.append(filter_name)
                elif filter_name == "followers_max":
                    if result.get("followers", float("inf")) <= filter_value:
                        score += 1
                        matched_filters.append(filter_name)
                elif result.get(filter_name) == filter_value:
                    score += 1
                    matched_filters.append(filter_name)

        result["matched_filters"] = matched_filters
        return score
