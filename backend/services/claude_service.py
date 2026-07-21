class ClaudeService:
    """TODO: wrap Anthropic API calls used by agents. Never fabricate output on failure."""

    async def complete(self, prompt: str) -> str:
        """TODO"""
