from pathlib import Path
from datetime import datetime
import yfinance as yf

from config_loader import load_config

def download_data() -> None:
    '''Download ticker data based on configuration and save to CSV files.'''
    
    tickers, start_date, end_date, frequency = load_config()
    
    output_dir = Path(__file__).resolve().parents[1] / "data" / "raw"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Downloadung {len(tickers)} tickers with frequency '{frequency}' "
          f"from {start_date} to {end_date}")
    
    df = yf.download(
        tickers = tickers, 
        start = start_date, 
        end = end_date, 
        interval = frequency)
    
    download_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        
    if df.empty:
        print("No data downloaded. Please check the configuration.")
        return

    for ticker in tickers:
        try:
            # yfinance with multiple tickers returns a MultiIndex on columns.
            # Here we assume level 1 contains the ticker symbol.
            ticker_df = df.xs(ticker, level=1, axis=1)
            
            output_path = output_dir / f"{ticker}_{download_time}.csv"
            ticker_df = ticker_df.reset_index()
            ticker_df.to_csv(output_path, index=False)
            
            print(f"{ticker} saved to {output_path}")
        except KeyError:
            print(f"No data for {ticker} found. Skipping...")
      
if __name__ == "__main__":
    download_data()