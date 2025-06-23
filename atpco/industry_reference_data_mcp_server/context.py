"""Context management for Industry Reference Data MCP Server."""

class Context:
    """Context class for Industry Reference Data MCP Server."""

    _readonly = False

    @classmethod
    def initialize(cls, readonly: bool = False):
        """Initialize the context.

        Args:
            readonly: Whether to run in readonly mode
        """
        cls._readonly = readonly

    @classmethod
    def readonly_mode(cls) -> bool:
        """Check if the server is running in readonly mode.

        Returns:
            True if readonly mode is enabled, False otherwise
        """
        return cls._readonly