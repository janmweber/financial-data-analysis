import json
from pathlib import Path
from datetime import date, datetime
from typing import List, Tuple    

def load_config(config_path: str | Path = None) -> tuple[list[str], str, str, str]:
    """Load tickers, dates and frequency from config.json.

    Return a tuple of (tickers, start_date, end_date, frequency).
    """ 
    
    if config_path is None:
        config_path = Path(__file__).resolve().parents[1] / "config" / "config.json"
    else:
        config_path = Path(config_path)
        
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
    
    tickers: List[str] = config.get("tickers")
    start_date: str = config.get("start_date")
    end_date: str = config.get("end_date")
    frequency: str = config.get("frequency")
    
    
    if start_date == "today":
        start_date = date.today().isoformat()
    if end_date == "today":
        end_date = date.today().isoformat()
        
    return tickers, start_date, end_date, frequency

if __name__ == "__main__":  # simple manual test hook
    print(load_config())
