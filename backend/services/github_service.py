class GitHubService:
    """TODO: verify webhook signatures, fetch commit/file diffs via GitHub API."""

    async def verify_signature(self, payload: bytes, signature: str) -> bool:
        """TODO"""

    async def get_commit_diff(self, owner: str, repo: str, sha: str) -> str:
        """TODO"""
