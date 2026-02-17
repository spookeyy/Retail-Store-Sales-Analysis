import os
import pandas as pd


def load_data(filepath: str) -> pd.DataFrame:
    """Load CSV dataset."""
    return pd.read_csv(filepath)


def save_processed_data(df: pd.DataFrame, filepath: str) -> None:
    """Save processed dataframe to CSV."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df.to_csv(filepath, index=False)


def ensure_dir(directory: str) -> None:
    """Ensure directory exists."""
    os.makedirs(directory, exist_ok=True)
    print(f"Created directory: {directory}")