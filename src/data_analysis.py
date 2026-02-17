import pandas as pd


def analyze_data(df: pd.DataFrame) -> dict:
    """Perform Q6–Q8 Analysis"""

    results = {}

    # Q6: Sales Trends
    results["sales_per_year"] = (
        df.groupby("Year")["Total Spent"].sum().round(2)
    )

    results["sales_per_month"] = (
        df.groupby("Month_Name")["Total Spent"].sum().round(2)
    )

    results["sales_per_category"] = (
        df.groupby("Category")["Total Spent"]
        .sum()
        .sort_values(ascending=False)
        .round(2)
    )

    results["top_items"] = (
        df.groupby("Item")["Total Spent"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .round(2)
    )

    # Q7: Customer Insights
    customer_total = df.groupby("Customer ID")["Total Spent"].sum()
    customer_avg = df.groupby("Customer ID")["Total Spent"].mean()

    results["avg_customer_spend"] = customer_avg.mean().round(2)
    results["top_customer"] = customer_total.idxmax()
    results["top_customer_spend"] = customer_total.max().round(2)
    results["discount_percentage"] = (
        df["Discount Applied"].sum() / len(df) * 100
    )

    # Q8: Payment & Channel
    results["payment_revenue"] = (
        df.groupby("Payment Method")["Total Spent"]
        .sum()
        .sort_values(ascending=False)
        .round(2)
    )

    results["channel_analysis"] = (
        df.groupby("Location")["Total Spent"]
        .agg(["sum", "mean", "count"])
        .round(2)
    )

    return results
