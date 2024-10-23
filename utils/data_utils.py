


def calculate_daily_returns(data):
    """
    Calculates the daily percentage returns for the stock data.

    Parameters:
    - data (DataFrame): The cleaned stock data containing 'Adj Close'

    Returns:
    - data_with_returns (DataFrame): DataFrame with daily returns added
    """
    data['Daily Return'] = data['Adj Close'].pct_change()
    
    # Drop the first row which will be NaN due to the pct_change() operation
    data_with_returns = data.dropna()
    
    return data_with_returns


def calculate_rolling_statistics(data, window=20):
    """
    Calculates rolling mean and standard deviation of daily returns over a given window.

    Parameters:
    - data (DataFrame): Data with daily returns
    - window (int): The window size for rolling calculations (default is 20)

    Returns:
    - data_with_rolling (DataFrame): DataFrame with rolling mean and std deviation added
    """
    data['Rolling Mean'] = data['Daily Return'].rolling(window).mean()
    data['Rolling Std Dev'] = data['Daily Return'].rolling(window).std()
    
    return data

