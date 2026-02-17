import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils import load_data, save_processed_data
from src.data_cleaning import clean_data
from src.data_transformation import transform_data
from src.data_analysis import analyze_data
from src.visualization import create_all_plots
from src.advanced_analysis import perform_rfm_analysis
from src.reporting import generate_summary_report


def main():

    raw_path = "data/raw/retail_store_sales.csv"
    processed_path = "data/processed/cleaned_sales_data.csv"

    # Load
    df = load_data(raw_path)

    # Clean
    df = clean_data(df)
    save_processed_data(df, processed_path)

    # Transform
    df = transform_data(df)

    # Analyze
    analysis_results = analyze_data(df)

    # Visualize
    create_all_plots(df, analysis_results)

    # Advanced
    rfm_results = perform_rfm_analysis(df)

    # Report
    generate_summary_report(df, analysis_results, rfm_results)

    print("Analysis complete. Check reports/ folder.")


if __name__ == "__main__":
    main()





















# #!/usr/bin/env python
# """
# Master script to run the complete retail sales analysis
# """
# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# from src.data_cleaning import clean_data
# from src.data_transformation import transform_data
# from src.data_analysis import analyze_data
# from src.visualization import create_all_plots
# from src.advanced_analysis import perform_rfm_analysis
# from src.utils import load_data, save_processed_data, ensure_dir
# import pandas as pd

# def main():
#     print("="*60)
#     print("RETAIL STORE SALES ANALYSIS")
#     print("="*60)
    
#     # Setup paths
#     raw_data_path = "data/raw/retail_store_sales.csv"
#     cleaned_data_path = "data/processed/cleaned_sales_data.csv"
    
#     # Load data
#     print("\n1. Loading data...")
#     df = load_data(raw_data_path)
#     print(f"   Loaded {len(df)} transactions")
    
#     # Section A: Data Cleaning
#     print("\n2. Cleaning data (Section A)...")
#     df_cleaned = clean_data(df)
#     save_processed_data(df_cleaned, cleaned_data_path)
    
#     # Section B: Data Transformation
#     print("\n3. Transforming data (Section B)...")
#     df_transformed = transform_data(df_cleaned)
    
#     # Section C: Data Analysis
#     print("\n4. Analyzing data (Section C)...")
#     analysis_results = analyze_data(df_transformed)
    
#     # Section D: Visualization
#     print("\n5. Creating visualizations (Section D)...")
#     ensure_dir("reports/figures/")
#     create_all_plots(df_transformed, analysis_results)
    
#     # Section E: Advanced Analysis
#     print("\n6. Performing advanced analysis - RFM (Section E)...")
#     rfm_results = perform_rfm_analysis(df_transformed)
    
#     # Section F: Generate Summary Report
#     print("\n7. Generating insight report (Section F)...")
#     generate_summary_report(df_transformed, analysis_results, rfm_results)
    
#     print("\n" + "="*60)
#     print("ANALYSIS COMPLETE!")
#     print("="*60)
#     print("\nOutput files:")
#     print("  - Cleaned data: data/processed/cleaned_sales_data.csv")
#     print("  - Visualizations: reports/figures/")
#     print("  - Insights: reports/insights/retail_sales_insights.txt")

# def generate_summary_report(df, analysis, rfm):
#     """Generate the final summary report"""
#     # This would compile all insights into the final report
#     # You can use the summary from Q11 here
#     pass

# if __name__ == "__main__":
#     main()