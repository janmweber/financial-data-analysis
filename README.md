# Financial Data Analysis Project

Small project to download, clean, and explore stock price data.

## What this project does

- Downloads daily price data from Yahoo Finance for a set of tickers.
- Cleans and combines the data into one table.
- Prepares basic features like daily returns and simple rolling stats.
- Sets things up for simple analysis and plots.

Default tickers (in `config/config.json`): NVDA, AAPL, MSFT, GOOGL, ORCL, PLTR.

## How to use it (high level)

1. Edit `config/config.json` to choose tickers and dates.
2. Run `src/download_data.py` to fetch and save raw CSVs to `data/raw/`.
3. Open `notebooks/02_data_cleaning.ipynb` to load, clean, and save processed data to `data/processed/`.
4. Use additional notebooks for analysis and plots (work in progress).

## Folders

- `data/` – raw and processed CSV files.
- `notebooks/` – Jupyter notebooks.
- `src/` – Python scripts (download and helpers).
- `config/` – project config (`config.json`).
