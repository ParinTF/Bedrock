import pandas as pd
import polars as pl
import duckdb
import pyarrow as pa

print("Environment Check")
print("-----------------")

print("Pandas:", pd.__version__)
print("Polars:", pl.__version__)
print("DuckDB:", duckdb.__version__)
print("PyArrow:", pa.__version__)

print("-----------------")
print("All libraries imported successfully!")