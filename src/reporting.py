from .utils import ensure_dir


def generate_summary_report(df, analysis, rfm):

    ensure_dir("reports/insights/")

    total_revenue = df["Total Spent"].sum()
    avg_transaction = df["Total Spent"].mean()

    summary = f"""
RETAIL STORE SALES ANALYSIS SUMMARY

Total Revenue: ${total_revenue:,.2f}
Average Transaction Value: ${avg_transaction:,.2f}

Top Category: {analysis["sales_per_category"].index[0]}
Top Item: {analysis["top_items"].index[0]}

Top Customer: {analysis["top_customer"]}
Top Customer Spend: ${analysis["top_customer_spend"]:,.2f}

Discount Usage: {analysis["discount_percentage"]:.2f}%

Payment Method Generating Highest Revenue:
{analysis["payment_revenue"].index[0]}

The RFM model identified 3 customer segments.
High-frequency, high-monetary customers should be retained through loyalty programs.
Low-frequency customers should receive targeted reactivation campaigns.
"""

    with open("reports/insights/retail_sales_insights.txt", "w") as f:
        f.write(summary)

    return summary