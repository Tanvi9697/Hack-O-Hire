# Hack-O-Hire

A small repository for anomaly detection and monitoring on API logs. Contains simple scripts for training models, detecting anomalies, and monitoring alerts.

## Repository structure

- `data/`
  - `api_logs.csv` — sample API logs used by the scripts
- `models/` — saved model artifacts (empty by default)
- `src/`
  - `train_models.py` — train models on `data/api_logs.csv`
  - `detect_anomalies.py` — run anomaly detection using trained models
  - `monitor_alerts.py` — simple alerting/monitoring wrapper

## Quickstart (Windows PowerShell)

1. Create a virtual environment and activate it:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies (if you add `requirements.txt`):

```powershell
pip install -r requirements.txt
```

3. Run training (creates artifacts in `models/`):

```powershell
python src\train_models.py
```

4. Run anomaly detection on logs:

```powershell
python src\detect_anomalies.py
```

5. Run monitoring/alerting loop (may require configuration):

```powershell
python src\monitor_alerts.py
```

## Data

Place your CSV or log files in the `data/` directory. The repository currently includes `data/api_logs.csv` as an example input.

