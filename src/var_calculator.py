import numpy as np
import pandas as pd
from scipy.stats import norm
# from utils.data_utils import validate_returns, confidence_to_zscore


def validate_returns(returns):
    """
    Validates that the input is a pandas Series and has enough data points.
    
    Parameters:
    - returns (Series): A pandas Series of daily returns
    
    Returns:
    - None: Raises an error if validation fails
    """
    if not isinstance(returns, pd.Series):
        raise ValueError("The input returns should be a pandas Series.")
    if len(returns) < 2:
        raise ValueError("Insufficient data points to calculate VaR.")
    



def confidence_to_zscore(confidence_level):
    """
    Converts a confidence level to a Z-score for parametric VaR calculation.
    
    Parameters:
    - confidence_level (float): The confidence level (e.g., 0.95 for 95%)
    
    Returns:
    - z_score (float): Corresponding Z-score for the confidence level
    """
    return norm.ppf(confidence_level)




def print_var_results(param_var, hist_var, confidence_level=0.95):
    """
    Prints the calculated parametric and historical VaR.
    
    Parameters:
    - param_var (float): Calculated parametric VaR
    - hist_var (float): Calculated historical VaR
    - confidence_level (float): Confidence level used in calculations
    """
    print(f"Value at Risk (VaR) at {confidence_level * 100}% confidence level:")
    print(f"Parametric VaR: {param_var}")
    print(f"Historical VaR: {hist_var}")


def parametric_var(returns, confidence_level=0.95):
    validate_returns(returns)
    
    mean_return = np.mean(returns)
    std_dev = np.std(returns)
    
    z_score = confidence_to_zscore(confidence_level)
    
    # Parametric VaR
    var = mean_return - z_score * std_dev
    return var

def historical_var(returns, confidence_level=0.95):
    validate_returns(returns)
    
    # Sort the returns
    sorted_returns = np.sort(returns)
    
    # Calculate the index for the given confidence level
    var_index = int((1 - confidence_level) * len(sorted_returns))
    
    # Return the historical VaR
    var = sorted_returns[var_index]
    return var
