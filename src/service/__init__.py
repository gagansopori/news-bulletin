from typing import Protocol, Any


class JsonSource(Protocol):
    def get(self, key: str) -> Any | None:
        """Returns the configs"""
