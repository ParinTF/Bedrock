from pathlib import Path
import pandas as pd

# 1. Define project root
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# 2. Define file paths
RAW_PATH = PROJECT_ROOT / "data" / "raw" / "2019-Oct.csv.gz"

if not RAW_PATH.exists():
    RAW_PATH = PROJECT_ROOT / "data" / "raw" / "2019-Oct.csv"

SAMPLE_PATH = PROJECT_ROOT / "data" / "samples" / "events_sample.csv"

# 3. Define sample size
SAMPLE_SIZE = 10_000

# 4. Check source file
if not RAW_PATH.exists():
    raise FileNotFoundError(RAW_PATH)

# 5. Create output directory
SAMPLE_PATH.parent.mkdir(
    parents=True,
    exist_ok=True
)

# 6. Read the first 10,000 records
df = pd.read_csv(
    RAW_PATH,
    nrows=SAMPLE_SIZE,
    dtype=str,
    keep_default_na=False
)

# 7. Save sample dataset
df.to_csv(SAMPLE_PATH, index=False)

# 8. Display results
print("Sample created successfully!")
print(f"Source: {RAW_PATH.name}")
print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns)}")
print(f"Output: {SAMPLE_PATH}")