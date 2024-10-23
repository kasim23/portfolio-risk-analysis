import numpy as np
import pandas as pd
import yfinance as yf
import os


file_path = 'data/'

def get_data(ticker='^GSPC', fts_name='sp500', start_date='1980-01-01', end_date='2024-01-01'):
     """
    Fetches historical stock data for the specified ticker symbol from Yahoo Finance.
    Saves the data as a CSV file for offline use.

    Parameters:
    - ticker (str): Stock ticker symbol (default is '^GSPC' for S&P 500)
    - fts_name (str): The name to save the CSV file as (default is 'sp500')
    - start_date (str): Start date for historical data (default is '1980-01-01')
    - end_date (str): End date for historical data (default is '2024-01-01')
    
    Returns:
    - data (DataFrame): A pandas DataFrame containing the historical data.
    """
    # Check if the data folder exists, create it if not
     if not os.path.exists('data'):
        os.makedirs('data')

    # File path for storing the data
     file_path = f"data/{fts_name}.csv"

    # Check if the file already exists to avoid repeated downloads
     if os.path.exists(file_path):
        print(f"File {file_path} already exists. Reading data from CSV.")
        data = pd.read_csv(file_path, index_col='Date', parse_dates=True)
     else:
        # Download the historical data using yfinance
        print(f"Downloading data for {ticker} from Yahoo Finance...")
        data = yf.download(ticker, start=start_date, end=end_date)
        
        # Save the downloaded data to CSV for future use
        data.to_csv(file_path)
        print(f"Data saved to {file_path}.")

     return data
