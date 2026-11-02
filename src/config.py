from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DATA_URL = "https://archive.ics.uci.edu/static/public/601/ai4i+2020+predictive+maintenance+dataset.zip"
RAW_PATH = ROOT / "data" / "raw" / "ai4i2020.csv"
MODEL_PATH = ROOT / "models" / "random_forest.joblib"

TARGET = "machine_failure"
RANDOM_STATE = 42