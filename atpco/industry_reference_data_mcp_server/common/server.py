"""Common MCP server configuration."""

from fastmcp import FastMCP

mcp = FastMCP(
    'atpco.industry-reference-data-mcp-server',
    instructions="""Industry Reference Data Server provides tools and resources for managing industry reference data.
    These tools allow you to create, read, update, and delete industry reference data records.
    You can also search for specific records based on various criteria.
    """,
    dependencies=[
        'pydantic',
        'requests',
        'loguru',
    ],
)