"""VibeScan MCP Server — scan projects for leaked secrets and security issues."""

from mcp.server.fastmcp import FastMCP

from .tools import rules, scan

mcp = FastMCP(
    "vibescan-mcp-server",
    instructions=(
        "MCP server for VibeScan — a local code security scanner. "
        "Detects leaked secrets, dangerous code patterns, and git hygiene issues. "
        "17 detection rules, 14 secret categories. All scanning runs locally."
    ),
)


@mcp.tool()
def vibescan_scan(path: str = ".", min_severity: str = "info") -> str:
    """Scan a project directory for leaked secrets and security issues.

    Detects:
    - Leaked secrets: API keys, passwords, tokens in code/config/docs
    - Dangerous patterns: eval(), shell injection, SQL injection, pickle
    - Git hygiene: missing .gitignore, unignored sensitive files
    - 14 secret categories: env files, cloud credentials, Docker, CI/CD, SSH keys, etc.

    Returns issues with severity, file location, description, and fix suggestion.
    All scanning runs locally — your code never leaves your machine.

    Args:
        path: Project directory to scan (default: current directory)
        min_severity: Minimum severity to report — critical, high, medium, low, info (default: info)
    """
    return scan.run(path, min_severity)


@mcp.tool()
def vibescan_rules() -> str:
    """List all available VibeScan detection rules.

    Returns the full list of 17 detection rules with their IDs, names, and descriptions.
    Useful for understanding what VibeScan checks for.
    """
    return rules.run()


def main():
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
