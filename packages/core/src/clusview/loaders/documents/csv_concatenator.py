from typing import List

import pandas as pd

from .base_document_loader import BaseDocumentLoader


class CSVConcatenator(BaseDocumentLoader):
    """A class for loading and concatenating documents from a CSV file."""

    def __init__(self, path_to_csv: str, column_names: List[str] = []) -> None:
        """
        Initialize the CSVConcatenator.

        Args:
            path_to_csv (str): The path to the CSV file.
            column_names (List[str], optional): A list of column names to include in the concatenation.
                Defaults to an empty list, which includes all columns.
        """
        self.path_to_csv = path_to_csv
        self.column_names = column_names

    def load_documents(self) -> List[str]:
        """
        Load and concatenate the documents from the CSV file.

        Returns:
            List[str]: A list of concatenated documents.
        """
        df: pd.DataFrame = pd.read_csv(self.path_to_csv).astype(str)

        if self.column_names:
            self.column_names = [col for col in self.column_names if col in df.columns]
            df = df[self.column_names]

        return df.apply(lambda row: " ".join(row.astype(str)), axis=1).tolist()
