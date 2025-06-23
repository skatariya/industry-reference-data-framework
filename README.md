# Industry Reference Data MCP

This repository contains an implementation of an ATPCO Model Context Protocol (MCP) server that provides tools for accessing Industry Reference Data.

## Features
- Built on top of **FastMCP** for easy tool creation and HTTP serving.
- Includes a context manager to optionally run the server in read‑only mode.
- Ships with an example appendix tool for retrieving a record by name and code.

## Repository layout
- `atpco/industry_reference_data_mcp_server/common/` &ndash; shared server configuration and decorators.
- `atpco/industry_reference_data_mcp_server/tools/` &ndash; individual MCP tools such as the appendix helper.
- `atpco/industry_reference_data_mcp_server/main.py` &ndash; CLI entry point used to start the server.

## Installation
1. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

## Usage
Run the MCP server with:
```bash
python -m atpco.industry_reference_data_mcp_server.main
```
Add `--readonly` to prevent mutating operations.

The server exposes tools via the MCP interface. The provided appendix tool `get-appendix-record-by-name-and-code` queries a remote API and returns the appendix record in JSON format.
