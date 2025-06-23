"""ATPCO Industry Reference Data MCP Server implementation."""

import argparse
from .common.server import mcp
from .context import Context
from loguru import logger
from .tools import (  
    appendix,
)

def main():
    """Run the MCP server with CLI argument support."""
    parser = argparse.ArgumentParser(
        description='An ATPCOs Model Context Protocol (MCP) server for interacting with Industry Reference Data'
    )
    parser.add_argument(
        '--readonly',
        action=argparse.BooleanOptionalAction,
        help='Prevents the MCP server from performing mutating operations',
    )

    args = parser.parse_args()
    Context.initialize(args.readonly)

    logger.info('Industry Reference Data MCP Server Started...')
    mcp.run(transport="streamable-http", host="127.0.0.1", port=9009)

if __name__ == '__main__':
    main()