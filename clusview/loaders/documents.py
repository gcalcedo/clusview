from typing import List
import pandas as pd


def docs_from_csv(path_to_csv: str, column_names: List[str] = []) -> List[str]:
    """
    Creates a series of documents by concatenating the values of CSV columns.

    ### Args:
        - `path_to_csv : str`: Filesystem path to the CSV file.
        - `column_names : List[str]`: List of column names to create the documents from.
        By default, or if left empty, it will use all of the columns of the CSV.
        If a column name does not exist in the CSV, it is ignored.

    ### Returns:
        - `List[str]`: List of documents.
    """
    df: pd.DataFrame = pd.read_csv(path_to_csv).astype(str)

    if column_names:
        column_names = [col for col in column_names if col in df.columns]
        df = df[column_names]

    return df.apply(lambda row: " ".join(row.astype(str)), axis=1).tolist()
