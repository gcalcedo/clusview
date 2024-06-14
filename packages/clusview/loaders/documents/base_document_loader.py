from abc import ABC, abstractmethod
from typing import List


class BaseDocumentLoader(ABC):
    """
    Base class for document loaders.
    """

    @abstractmethod
    def load_documents(self) -> List[str]:
        """
        Loads the documents with this component's specific implementation.
        """
        pass
