"""Reusable decorators for the Industry Reference Data MCP server."""

from functools import wraps
from typing import Any, Callable

def handle_exceptions(func: Callable) -> Callable:
    """Return ``func`` wrapped with generic exception handling.

    The decorated function executes inside a ``try``/``except`` block so that
    uncaught exceptions are converted into a standardized error dictionary.

    Parameters
    ----------
    func:
        The asynchronous function to wrap.

    Returns
    -------
    Callable
        The wrapped function that handles exceptions.
    """

    @wraps(func)
    async def wrapper(*args: Any, **kwargs: Any):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            return {'error': str(e)}

    return wrapper