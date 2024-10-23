import matplotlib.pyplot as plt

def plot_monte_carlo_simulations(simulations, title="Monte Carlo Simulation of S&P 500 Future Prices (1 Year)", xlabel="Days", ylabel="Simulated Prices"):
    """
    Plots the simulated price paths generated from the Monte Carlo simulation.
    
    Parameters:
    - simulations (ndarray): Array of simulated price paths
    - title (str): Title of the plot (default is set for S&P 500 simulation)
    - xlabel (str): Label for the x-axis (default is "Days")
    - ylabel (str): Label for the y-axis (default is "Simulated Prices")
    """
    plt.figure(figsize=(10, 6))
    plt.plot(simulations.T, lw=1)  # Transpose simulations for plotting
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
