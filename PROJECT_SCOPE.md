# Project Scope: Financial Data Analysis & Visualization

## Objective

Analyze and visualize historical performance, volatility, and correlations of a configurable set of large-cap tech and software stocks using daily price data.

## Default Universe

Configured in `config/config.json`:

- NVDA (NVIDIA Corporation)
- AAPL (Apple Inc.)
- MSFT (Microsoft Corporation)
- GOOGL (Alphabet Inc. Class A)
- ORCL (Oracle Corporation)
- PLTR (Palantir Technologies Inc.)

## Time Horizon

- Start date: 2019-01-01
- End date: today (latest available trading day)
- Frequency: Daily data

## Data Source

- Yahoo Finance via the `yfinance` Python library.

## Key Questions

- Which stock delivered the highest average daily and cumulative return over the sample period?
- Which stock is most and least volatile?
- How correlated are these assets over the full period?
- How did they behave during notable stress periods (e.g., 2020 COVID crash, 2022 rate hikes)?

## Project Structure (initial)

- `data/`
  - `raw/` – original downloaded data (e.g., ticker-level CSV files)
  - `processed/` – cleaned and merged datasets
- `notebooks/`
  - Jupyter notebooks for data download, cleaning, EDA, and visualization
- `src/`
  - Python scripts and helper modules for downloading and processing data
- `config/`
  - `config.json` with ticker list, date range, and frequency

## Dynamism

All scripts and notebooks will load tickers, dates, and frequency from `config/config.json`. To change the universe or time range, update that file; analysis code should adapt automatically.
