from src.data_loader import get_data
from src.var_calculator import parametric_var, historical_var
from utils.var_calculator_utils import print_var_results
from src.monte_carlo_simulator import monte_carlo_simulation
from utils.monte_carlo_utils import plot_monte_carlo_simulations

if __name__ == "__main__":
    sp500_data = get_data()
    print(sp500_data.head())
    
    # Calculate daily returns
    sp500_data['Daily Return'] = sp500_data['Adj Close'].pct_change().dropna()
    
    # Get daily returns as a pandas Series for VaR calculations
    daily_returns = sp500_data['Daily Return'].dropna()
    
    param_var_value = parametric_var(daily_returns, confidence_level=0.95)
    hist_var_value = historical_var(daily_returns, confidence_level=0.95)
    
    print_var_results(param_var_value, hist_var_value, confidence_level=0.95)
    
    # Run Monte Carlo simulation using the last available Adjusted Close price
    initial_price = sp500_data['Adj Close'].iloc[-1]  # Last known price
    simulations = monte_carlo_simulation(daily_returns, initial_price, num_simulations=1000, days=252)
    
    plot_monte_carlo_simulations(simulations)
    