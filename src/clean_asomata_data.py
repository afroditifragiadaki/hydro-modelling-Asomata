import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get paths from .env
data_path = Path(os.getenv("DATA_PATH"))
output_path = Path(os.getenv("DATA_OUTPUT_PATH"))

# Load Excel file
df = pd.read_excel(data_path)

# Convert the first column to numeric
df.iloc[:, 0] = pd.to_numeric(df.iloc[:, 0], errors='coerce')

# Keep only rows where first column is a likely day of month (1-31)
df = df[df.iloc[:, 0].apply(lambda x: isinstance(x, (int, float)) and 1 <= x <= 31)]

# Rename columns
df.columns = [
    "Date",
    "Production Unit I (MWh)",
    "Production Unit II (MWh)",
    "Total HPP",
    "Auxiliaries Consumptions Unit I (MWh)",
    "Auxiliaries Consumptions Unit II (MWh)",
    "Auxiliaries Consumptions Grid (MWh)",
    "Net Production (MWh)",
    "Peak (MW)",
    "Hours of Operation Unit I",
    "Hours of Operation Unit II",
    "Unit I Maintenance Plant",
    "Unit I Maintenance Outside",
    "Unit I Failure Plant",
    "Unit I Failure Outside",
    "Unit II Maintenance Plant",
    "Unit II Maintenance Outside",
    "Unit II Failure Plant",
    "Unit II Failure Outside",
    "Number of Starts Unit I",
    "Number of Starts Unit II",
    "Comments",
    "Date",
    "Asomata Reservoir Water Level (m)",
    "Asomata Reservoir Water Content (m3 x 1000)",
    "Regulating lake Water Level (m)",
    "Regulating lake Water Content (m3 x 1000)",
    "Water saved in lake",
    "Catchment water inflow",
    "Production Water Consumption (m3 x 1000)",
    "Specific Consumption",
    "Turbine Efficiency",
    "HPP Sfikia Water Production (m3  x 1000)",
    "HPP Sfikia Water Pumped upstream (m3  x 1000)",
    "Lake natural inflow (m3  x 1000)",
    "Losses (m3  x 1000)",
    "B",
    "Regulating lake Water flow  (m3/s)",
    "Regulating lake Total Water (m3  x 1000)",
    "Year",
    "Month",
    "SourceFile"
]

# Save cleaned file
df.to_excel(output_path, index=False)

print(f"✅ File cleaned and saved to:\n{output_path}")