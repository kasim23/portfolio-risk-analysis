import numpy as np

def monte_carlo_simulation(returns, initial_price, num_simulations=1000, days=252):
    """
    Perform a Monte Carlo simulation to project future stock prices based on historical returns.
    
    Parameters:
    - returns (Series): A pandas Series of daily returns
    - initial_price (float): The initial stock price (e.g., the last known adjusted close price)
    - num_simulations (int): Number of simulations to run (default is 1000)
    - days (int): Number of days to simulate into the future (default is 252 for 1 year)
    
    Returns:
    - simulations (ndarray): An array of simulated price paths
    """
    mean_return = np.mean(returns)
    std_dev = np.std(returns)
    
    simulations = np.zeros((num_simulations, days))
    
    # Run the simulations
    for i in range(num_simulations):
        random_returns = np.random.normal(mean_return, std_dev, days)
        price_path = [initial_price]
        for r in random_returns:
            price_path.append(price_path[-1] * (1 + r))
        simulations[i] = price_path[1:]  # Exclude the first price, as it's the starting point
    
    return simulations
