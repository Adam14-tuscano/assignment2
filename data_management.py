import pandas as pd
import gzip
import shutil
import os

# Step 1: Load data
df = pd.read_csv("sample_logs.csv")
print("Original :\n", df.head())

# Step 2: Deduplication
df = df.drop_duplicates()
print("\nAfter Deduplication:\n", df.head())

# Step 3: Extract only the date part from timestamp
df["date"] = pd.to_datetime(df["timestamp"]).dt.date

# Step 4: Summarize by date (average of numeric columns)
summary = df.groupby("date").mean(numeric_only=True)
print("\nSummarized :\n", summary.head())

summary.to_csv("summary.csv", index=True)


with open("summary.csv", 'rb') as f_in:
    with gzip.open("summary.csv.gz", 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

print("\n Files generated:")
print(" - summary.csv")
print(" - summary.csv.gz")

print("\nOriginal file size:", os.path.getsize("sample_logs.csv"), "bytes")
print("Summarized file size:", os.path.getsize("summary.csv"), "bytes")
print("Compressed file size:", os.path.getsize("summary.csv.gz"), "bytes")

