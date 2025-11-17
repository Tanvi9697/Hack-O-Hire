import os
import pandas as pd
import joblib
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

# Define file paths
DATA_PATH = os.path.join("data", "api_logs.csv")
MODELS_DIR = "models"

# Ensure models directory exists
os.makedirs(MODELS_DIR, exist_ok=True)

# Load dataset
print(f"Looking for file at: {os.path.abspath(DATA_PATH)}")
if not os.path.exists(DATA_PATH):
    print("❌ File not found! Make sure 'api_logs.csv' exists in the data folder.")
    exit()

df = pd.read_csv(DATA_PATH)

# Convert timestamp column to datetime (if applicable)
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Select features for anomaly detection
X = df[["response_time", "status_code"]]

# Standardize data for DBSCAN
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train Isolation Forest
iso_forest = IsolationForest(contamination=0.1, random_state=42)
iso_forest.fit(X)

# Train DBSCAN
dbscan = DBSCAN(eps=1.5, min_samples=2)
dbscan.fit(X_scaled)

# Save models
joblib.dump(iso_forest, os.path.join(MODELS_DIR, "isolation_forest.pkl"))
joblib.dump(dbscan, os.path.join(MODELS_DIR, "dbscan.pkl"))

print("✅ Models trained and saved successfully!")
