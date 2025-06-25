"""Manage runtime context for the Industry Reference Data MCP server."""

class Context:
    """Holds global configuration for the MCP server."""

    _readonly = False

    @classmethod
    def initialize(cls, readonly: bool = False) -> None:
        """Initialize the context.

        Parameters
        ----------
        readonly:
            Indicates whether the server should operate in read-only mode.
        """
        cls._readonly = readonly

    @classmethod
    def readonly_mode(cls) -> bool:
        """Return ``True`` if the server is running in read-only mode."""
        return cls._readonly