"""Appendix tool for Industry Reference Data MCP server."""

from ...common.decorators import handle_exceptions
from ...common.server import mcp
import requests
import json

@mcp.tool(name='get-appendix-record-by-name-and-code')
@handle_exceptions
async def appendix_record_by_name_and_code(
    name: str,
    code: str,
) -> str:
    """Get appendix record by name and code.

    This tool returns information about Appendix record for a given name and code

    Parameters:
        name (str): The name of the appendix record.
        code (str): The code of the appendix record.

    Returns:
        str: A JSON string containing the appendix record information.
    """
    try:
        print(f"Received request for appendix record by name '{name}' and code '{code}'")   
        
        # Tool implementation
        response = requests.get(f"https://2arkxdgfwi.execute-api.us-east-1.amazonaws.com/v1/appendices/{name}/{code}")
        return {
                "status": "success", 
                "data": {
                    "name": name,
                    "code": code,
                    "content": json.loads(response.text) if response.status_code == 200 else {"error": "Record not found"}
                }
            }
    except Exception as e:
        # Handle exceptions
        return {
            "status": "error",
            "content": [{"text": str(e)}]
        }