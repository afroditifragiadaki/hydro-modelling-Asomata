# Asomata Hydropower Plant Modelling

Forecasting production for the Asomata hydropower plant using historical generation records and weather data.

## Data
- Plant production records: per-unit generation (MWh), auxiliary consumption, hours of operation, maintenance/failure logs — see `data_columns.txt` for the full schema
- Weather data pulled via API (`src/get_historical_weather_API.py`)

## Pipeline
- `src/read_asomata_data.py` — parses raw plant records
- `src/clean_asomata_data.py` — cleans and merges with weather data

## Models
- `models/data_analysis_Prophet.ipynb` — Prophet-based production forecasting
- `models/data_analysis_TFT.ipynb` — Temporal Fusion Transformer forecasting model
