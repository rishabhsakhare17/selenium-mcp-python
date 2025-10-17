# selenium-mcp-python

A minimal Python project scaffold for building your own Selenium MCP.

## Getting started

1. Create and activate a virtual environment
   - macOS/Linux:
     - `python3 -m venv .venv`
     - `source .venv/bin/activate`
2. Install dependencies
   - `pip install -e .` (or `pip install -r requirements.txt`)
3. Run tests
   - `pytest`

## Usage

- Run the MCP server in stdio mode (default):
  - `python src/selenium_mcp_server.py`
  - For HTTP (Server-Sent Events) mode: `python src/selenium_mcp_server.py --http`

## Configure with Claude Desktop (MCP)

1. Make sure this project works locally (see Getting started above). Optional: set up `.env`.
2. Open Claude Desktop → Settings → Model Context Protocol (MCP) → Add Server.
3. Configure a new server:
   - Command: `python`
   - Args: `src/selenium_mcp_server.py`
   - Transport: `stdio` (default)
   - Working directory: repository root of this project
4. Save. You should now see tools like `open_browser`, `go_to_url`, `click_element`, `get_page_text`, `screenshot`, `close_browser` available in Claude's Tools panel.

Notes:
- If Chrome/Chromedriver is not found, install Chrome and ensure a compatible driver (Selenium Manager usually handles this automatically in recent Selenium versions).
- If you prefer HTTP/SSE instead of stdio, run the server with `--http` and point Claude to your HTTP endpoint if/when Claude supports HTTP transports for MCP. Stdio is recommended today.

### Claude Desktop mcpServers JSON

Paste this into your Claude Desktop MCP configuration:

```json
{
  "mcpServers": {
    "selenium-mcp": {
      "command": "python",
      "args": ["src/selenium_mcp_server.py"],
      "env": {
        "MCP_HEADLESS": "1",
        "MCP_HTTP_PORT": "5003"
      }
    }
  }
}
```

If your repository is not the current working directory when Claude launches, specify an absolute working directory:

```json
"workingDirectory": "/absolute/path/to/selenium-mcp-python"
```

## Project layout

- `src/selenium_mcp/`: package source
- `tests/`: test suite
- `pyproject.toml`: build and package metadata
- `requirements.txt`: runtime/dev dependencies (mirrors `pyproject.toml` deps)

## Notes
- Target Python: 3.10+


---

