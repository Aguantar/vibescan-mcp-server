# vibescan-mcp-server

mcp-name: io.github.Aguantar/vibescan-mcp-server

MCP server for [VibeScan](https://github.com/Aguantar/vibescan) — scan projects for leaked secrets and security issues directly from Claude Code.

## Features

- **`vibescan_scan`** — Scan a project for secrets, dangerous patterns, and git hygiene issues
- **`vibescan_rules`** — List all 17 detection rules

### What VibeScan detects

- **14 secret categories**: env files, config hardcodes, cloud credentials, Docker/infra, CI/CD pipelines, IDE settings, SSH keys, hardcoded patterns, frontend env vars, data files, doc secrets, mobile files, system configs, editor remnants
- **Dangerous code patterns**: eval(), exec(), shell injection, SQL injection, pickle, innerHTML
- **Git hygiene**: missing .gitignore, unignored .env/.pem/.key files

All scanning runs locally — your code never leaves your machine.

## Installation

```bash
pip install vibescan-mcp-server
```

## Usage with Claude Code

Add to your `.mcp.json`:

```json
{
  "mcpServers": {
    "vibescan": {
      "command": "vibescan-mcp-server"
    }
  }
}
```

Then ask Claude: "scan this project for security issues" or "check for leaked secrets".

## License

MIT
