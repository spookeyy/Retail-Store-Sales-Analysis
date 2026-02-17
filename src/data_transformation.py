import pandas as pd


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Perform Q4–Q5 Feature Engineering"""

    # Revenue Category
    def categorize_revenue(amount):
        if amount < 100:
            return "Low (< 100)"
        elif amount <= 300:
            return "Medium (100–300)"
        else:
            return "High (> 300)"

    df["Revenue Category"] = df["Total Spent"].apply(categorize_revenue)

    # Is_Online
    df["Is_Online"] = df["Location"].apply(
        lambda x: 1 if str(x).strip().lower() == "online" else 0
    )

    return df
