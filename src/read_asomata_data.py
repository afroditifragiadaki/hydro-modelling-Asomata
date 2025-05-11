import os
import pandas as pd
from pathlib import Path
import re

# Environment-safe base path
BASE_PATH = Path(os.environ.get("HYDRO_DATA_BASE", "data/raw"))
OUTPUT_PATH = BASE_PATH.parent / "processed"

# Initialize list to store all data
combined_df = []

# Loop through each year folder (2014 to 2023)
for year in range(2014, 2024):
    year_path = BASE_PATH / str(year) / "Data In English"
    if not year_path.exists():
        print(f"⚠️ Skipping missing folder: {year_path}")
        continue

    for file in sorted(year_path.glob("*_Asomata_english.xlsx")):
        match = re.search(r"(\d{4})_(\d{2})_Asomata", file.stem)
        if not match:
            print(f"Skipping {file.name} — no date found.")
            continue

        year, month = match.groups()
        try:
            df = pd.read_excel(file, engine="openpyxl")
        except Exception as e:
            print(f"❌ Error reading {file.name}: {e}")
            continue

        df["Year"] = int(year)
        df["Month"] = int(month)
        df["SourceFile"] = file.name
        combined_df.append(df)
        print(f"📂 Read file: {file.name}")

# Concatenate and save
if combined_df:
    final_df = pd.concat(combined_df, ignore_index=True)
    
    # Convert problematic columns to string
    for col in final_df.select_dtypes(include="object").columns:
        final_df[col] = final_df[col].astype(str)

    OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

    final_df.to_parquet(OUTPUT_PATH / "asomata_all_years.parquet", index=False)
    final_df.to_excel(OUTPUT_PATH / "asomata_all_years.xlsx", index=False)

    print(f"✅ Saved combined dataset to:\n📁 {OUTPUT_PATH / 'asomata_all_years.parquet'}\n📁 {OUTPUT_PATH / 'asomata_all_years.xlsx'}")
else:
    print("❌ No data found in any folder.")


