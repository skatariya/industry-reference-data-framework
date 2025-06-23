"""Decorators for Industry Reference Data MCP Server."""

from functools import wraps
from typing import Any, Callable

def handle_exceptions(func: Callable) -> Callable:
    """Decorator to handle exceptions in Industry Reference Data operations.

    Wraps the function in a try-catch block and returns any exceptions
    in a standardized error format.

    Args:
        func: The function to wrap

    Returns:
        The wrapped function that handles exceptions
    """

    @wraps(func)
    async def wrapper(*args: Any, **kwargs: Any):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            return {'error': str(e)}

    return wrapper