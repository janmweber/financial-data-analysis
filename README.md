# Financial Data Analysis & Visualization

This project analyzes and visualizes historical performance, volatility, and correlations of a configurable set of stocks using daily market data from Yahoo Finance.

## Current Focus

Default ticker universe (configured in `config/config.json`):

- NVDA, AAPL, MSFT, GOOGL, ORCL, PLTR

Time horizon:

- From 2019-01-01 to the latest available date (daily data).

## High-Level Workflow

1. Configure tickers and date range in `config/config.json`.
2. Acquire data from Yahoo Finance (via `yfinance`) and store it under `data/raw/`.
3. Clean and prepare the data, saving processed datasets under `data/processed/`.
4. Perform exploratory analysis and compute basic statistics.
5. Create visualizations for prices, returns, volatility, and correlations.

## Project Structure

- `data/`
  - `raw/` – original downloaded CSV files
  - `processed/` – cleaned and merged datasets
- `notebooks/` – Jupyter notebooks for cleaning, analysis, and visualization
- `src/` – Python scripts and helper modules (e.g., data download, utilities)
- `config/` – configuration files, including `config.json`
- `PROJECT_SCOPE.md` – more detailed description of goals and questions

## Next Steps

- Set up a Python virtual environment.
- Install core dependencies (`pandas`, `numpy`, `matplotlib`, `seaborn`, `yfinance`, `jupyter`).
- Implement the data acquisition script and initial notebooks.
