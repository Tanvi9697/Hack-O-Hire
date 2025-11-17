import pandas as pd #type:ignore
import joblib #type:ignore
import numpy as np #type:ignore

# Load pre-trained models
isolation_forest = joblib.load("../models/isolation_forest.pkl")
dbscan = joblib.load("../models/dbscan.pkl")

def detect_anomalies(df):
    """
    Detects anomalies in API logs using Isolation Forest & DBSCAN.
    Returns a DataFrame of anomalies.
    """

    # Ensure required columns exist
    required_columns = {"response_time", "status_code"}
    if not required_columns.issubset(df.columns):
        raise ValueError(f"Missing columns: {required_columns - set(df.columns)}")

    # Feature engineering
    df["error_flag"] = df["status_code"].apply(lambda x: 1 if x >= 400 else 0)
    features = df[["response_time", "error_flag"]]

    # Apply Isolation Forest
    df["isolation_anomaly"] = isolation_forest.predict(features)
    df["isolation_anomaly"] = df["isolation_anomaly"].apply(lambda x: 1 if x == -1 else 0)

    # Apply DBSCAN
    dbscan_labels = dbscan.fit_predict(features)
    df["dbscan_anomaly"] = np.where(dbscan_labels == -1, 1, 0)

    # Final anomaly detection (if flagged by either model)
    df["anomaly"] = df[["isolation_anomaly", "dbscan_anomaly"]].max(axis=1)

    return df[df["anomaly"] == 1]  # Return only anomalies

