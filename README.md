# selenium-mcp-python

A minimal Python project scaffold for building your own Selenium MCP.

## Getting started

1. Create and activate a virtual environment
   - macOS/Linux:
     - `python3 -m venv .venv`
     - `source .venv/bin/activate`
2. Install dependencies
   - `pip install -e .` (or `pip install -r requirements.txt`)
3. Configure environment
   - Copy `.env.example` to `.env` and adjust values as needed
4. Run tests
   - `pytest`

## Usage

- Run the MCP server in stdio mode (default):
  - `python src/selenium_mcp-server.py`
  - For HTTP (Server-Sent Events) mode: `python src/selenium_mcp-server.py --http`

## Project layout

- `src/selenium_mcp/`: package source
- `tests/`: test suite
- `pyproject.toml`: build and package metadata
- `requirements.txt`: runtime/dev dependencies (mirrors `pyproject.toml` deps)

## Notes
- Target Python: 3.10+


---

