import pandas as pd
from typing import Optional

def parse_csv(file_path: str) -> Optional[pd.DataFrame]:
    """
    Loads and parses a CSV file.

    Returns:
        DataFrame if successful, None otherwise.
    """
    try:
        df = pd.read_csv(file_path)

        # Basic cleanup: drop fully empty columns
        df.dropna(axis=1, how='all', inplace=True)

        # Optional: limit preview to reasonable size
        if df.shape[0] > 1000:
            df = df.head(1000)

        return df
    except Exception as e:
        print(f"[parse_csv] Error: {e}")
        return None