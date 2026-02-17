import pandas as pd
import numpy as np


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Perform Q1–Q3 Data Cleaning"""

    # ----------------------------
    # Q1: Missing & Incorrect Values
    # ----------------------------

    # Standardize Discount Applied
    def standardize_boolean(val):
        if pd.isna(val):
            return False
        if isinstance(val, str):
            return val.strip().upper() == "TRUE"
        return bool(val)

    df["Discount Applied"] = df["Discount Applied"].apply(standardize_boolean)

    # Fix negative numeric values
    if "Price Per Unit" in df.columns:
        df["Price Per Unit"] = df["Price Per Unit"].abs()

    if "Quantity" in df.columns:
        df["Quantity"] = df["Quantity"].abs()

    # ----------------------------
    # Q2: Date Conversion
    # ----------------------------

    df["Transaction Date"] = pd.to_datetime(
        df["Transaction Date"], errors="coerce"
    )

    df["Year"] = df["Transaction Date"].dt.year
    df["Month"] = df["Transaction Date"].dt.month
    df["Month_Name"] = df["Transaction Date"].dt.month_name()
    df["Day_of_Week"] = df["Transaction Date"].dt.day_name()
    df["Quarter"] = df["Transaction Date"].dt.quarter

    # ----------------------------
    # Q3: Logical Accuracy Check
    # ----------------------------

    df["Calculated_Total"] = df["Price Per Unit"] * df["Quantity"]

    df["Total_Mismatch"] = ~np.isclose(
        df["Total Spent"],
        df["Calculated_Total"],
        rtol=0.01
    )

    # Fix mismatches
    df.loc[df["Total_Mismatch"], "Total Spent"] = df["Calculated_Total"]

    # Drop helper columns
    df.drop(["Calculated_Total", "Total_Mismatch"], axis=1, inplace=True)

    return df
