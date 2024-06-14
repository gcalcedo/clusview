from typing import List

import pandas as pd

from clusview.loaders.documents.base_document_loader import BaseDocumentLoader


class CSVConcatenator(BaseDocumentLoader):
    """
    Creates a list of documents by concatenating the values of CSV columns.

    ### Args:
        - `path_to_csv : str`: Filesystem path to the CSV file.
        - `column_names : List[str]`: List of column names to create the documents from.
        By default, or if left empty, it will use all of the columns of the CSV.
        If a column name does not exist in the CSV, it is ignored.

    ### Returns:
        - `List[str]`: List of documents.
    """

    def __init__(self, path_to_csv: str, column_names: List[str] = []) -> None:
        self.path_to_csv = path_to_csv
        self.column_names = column_names

    def load_documents(self) -> List[str]:
        df: pd.DataFrame = pd.read_csv(self.path_to_csv).astype(str)

        if self.column_names:
            self.column_names = [col for col in self.column_names if col in df.columns]
            df = df[self.column_names]

        return df.apply(lambda row: " ".join(row.astype(str)), axis=1).tolist()
