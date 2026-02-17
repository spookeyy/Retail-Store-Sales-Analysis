import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from .utils import ensure_dir


def perform_rfm_analysis(df: pd.DataFrame) -> dict:

    ensure_dir("reports/figures/")

    current_date = df["Transaction Date"].max() + pd.Timedelta(days=1)

    rfm = df.groupby("Customer ID").agg({
        "Transaction Date": lambda x: (current_date - x.max()).days,
        "Transaction ID": "count",
        "Total Spent": "sum"
    }).reset_index()

    rfm.columns = ["Customer ID", "Recency", "Frequency", "Monetary"]

    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(
        rfm[["Recency", "Frequency", "Monetary"]]
    )

    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    rfm["Cluster"] = kmeans.fit_predict(rfm_scaled)

    # 2D Plot
    plt.figure(figsize=(6, 5))
    plt.scatter(
        rfm["Frequency"],
        rfm["Monetary"],
        c=rfm["Cluster"]
    )
    plt.xlabel("Frequency")
    plt.ylabel("Monetary")
    plt.title("RFM Clusters")
    plt.tight_layout()
    plt.savefig("reports/figures/rfm_clusters.png")
    plt.close()

    return {"rfm_data": rfm}
