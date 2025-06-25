"""Tool for retrieving appendix records by name and code."""

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
    """Return the appendix record identified by ``name`` and ``code``.

    Parameters
    ----------
    name:
        The name of the appendix record.
    code:
        The appendix code to retrieve.

    Returns
    -------
    str
        A JSON string containing the appendix record information.
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