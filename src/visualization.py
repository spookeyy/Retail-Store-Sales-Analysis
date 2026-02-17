import matplotlib.pyplot as plt
import seaborn as sns
from .utils import ensure_dir


def create_all_plots(df, analysis_results):

    ensure_dir("reports/figures/")

    # Monthly Trend
    monthly_sales = (
        df.groupby(["Year", "Month"])["Total Spent"]
        .sum()
        .reset_index()
        .sort_values(["Year", "Month"])
    )

    plt.figure(figsize=(8, 5))
    plt.plot(monthly_sales["Total Spent"])
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month Index")
    plt.ylabel("Total Sales")
    plt.tight_layout()
    plt.savefig("reports/figures/monthly_sales_trend.png")
    plt.close()

    # Revenue by Category
    plt.figure(figsize=(8, 5))
    analysis_results["sales_per_category"].plot(kind="bar")
    plt.title("Revenue by Category")
    plt.tight_layout()
    plt.savefig("reports/figures/revenue_by_category.png")
    plt.close()

    # Payment Distribution
    plt.figure(figsize=(6, 6))
    df["Payment Method"].value_counts().plot(kind="pie", autopct="%1.1f%%")
    plt.title("Payment Method Distribution")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("reports/figures/payment_distribution.png")
    plt.close()

    # Discount Boxplot
    plt.figure(figsize=(6, 5))
    sns.boxplot(
        x="Discount Applied",
        y="Total Spent",
        data=df
    )
    plt.title("Discount vs Transaction Amount")
    plt.tight_layout()
    plt.savefig("reports/figures/discount_boxplot.png")
    plt.close()
