"""
Quick data quality check before analysis
"""
import pandas as pd
import sys
import os

# Construct the path relative to this script's location
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
sys.path.append(project_root)

df = pd.read_csv(os.path.join(project_root, "data/raw/retail_store_sales.csv"))

print("DATA QUALITY REPORT")
print("="*50)
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")
print("\nMissing Values:")
print(df.isnull().sum())
print("\nData Types:")
print(df.dtypes)
print("\nFirst 5 rows:")
print(df.head())