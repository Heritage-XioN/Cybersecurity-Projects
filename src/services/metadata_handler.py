from abc import ABC, abstractmethod
from typing import Any, Dict, Optional


class MetadataHandler(ABC):
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.metadata: Dict[str, Any] = {}
        self.processed_metadata: Dict[str, Any] = {}

    @abstractmethod
    def read(self) -> Dict[str, Any]:
        """Extracts metadata into a standard dictionary."""
        pass

    @abstractmethod
    def wipe(self) -> None:
        """Updates internal metadata state."""
        pass

    @abstractmethod
    def save(self, output_path: Optional[str] = None) -> None:
        """Writes the changes to a file."""
        pass
