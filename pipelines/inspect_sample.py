from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_PATH = (
    PROJECT_ROOT / "data" / "samples" / "events_sample.csv"
)

df = pd.read_csv(
    DATA_PATH,
    dtype=str,
    keep_default_na=False
)

print("===== DATA PREVIEW =====")
print(df.head())

print("\n===== DATA SHAPE =====")
print(df.shape)

print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== EVENT DISTRIBUTION =====")
print(df["event_type"].value_counts())

print("\n===== EMPTY FIELDS =====")
print(df.eq("").sum())