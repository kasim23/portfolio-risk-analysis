# **Portfolio Risk Analysis with Value at Risk (VaR) and Monte Carlo Simulation**

## **Overview**

This project focuses on performing **risk analysis** on the **S&P 500** index using two fundamental techniques in financial risk management: **Value at Risk (VaR)** and **Monte Carlo Simulations**. The goal is to assess the potential risk and simulate future price movements using historical data. 

The project involves:
1. **Downloading and preprocessing financial data** from Yahoo Finance.
2. **Calculating Value at Risk (VaR)** using both parametric and historical methods.
3. **Simulating future price movements** with a Monte Carlo simulation, which models a range of possible future scenarios based on historical returns.

## **Project Objectives**

1. **Fetch Historical Data**: Retrieve daily price data for the **S&P 500** index and preprocess it by calculating **daily returns**.
2. **Risk Assessment Using VaR**:
   - **Parametric VaR (Variance-Covariance method)**: Estimate risk based on the assumption that asset returns follow a normal distribution.
   - **Historical VaR**: Estimate risk using historical returns without assuming any specific distribution.
3. **Monte Carlo Simulation**: Generate thousands of potential future price paths for the S&P 500 based on its historical returns, offering a dynamic view of risk.

## **Key Concepts**

### **1. Value at Risk (VaR)**

**Value at Risk (VaR)** is a widely used risk measure in finance. It estimates the maximum loss an asset or portfolio might experience over a specified time period at a given confidence level (e.g., 95%). In other words, it answers the question: *“How much could I lose with 95% confidence in a given period?”*

There are two common approaches to calculating VaR in this project:

#### **a. Parametric VaR (Variance-Covariance Method)**

This method assumes that returns follow a **normal distribution**, and VaR is calculated using the **mean** and **standard deviation** of historical returns. It is based on the formula:

\[
VaR = \mu - Z \cdot \sigma
\]

Where:
- \(\mu\) is the mean return.
- \(Z\) is the Z-score corresponding to the desired confidence level (e.g., 1.65 for 95% confidence).
- \(\sigma\) is the standard deviation of historical returns.

#### **b. Historical VaR**

Unlike parametric VaR, **Historical VaR** does not assume a normal distribution for returns. Instead, it directly uses historical data to calculate risk. The returns are ranked, and the **5th percentile** (for 95% confidence) of historical returns is selected as the Value at Risk.

### **2. Monte Carlo Simulation**

**Monte Carlo simulations** are used to model the probability of different outcomes in a process involving random variables. In the context of finance, this technique is used to simulate possible future price paths of an asset based on historical returns.

The steps involved in Monte Carlo simulation are:
1. **Random Sampling**: Based on historical return statistics (mean and standard deviation), we generate random samples of daily returns.
2. **Simulating Price Paths**: Starting from a known initial price (e.g., the last available price of the S&P 500), we simulate future price paths using the randomly generated returns.
3. **Risk Estimation**: By simulating thousands of potential future price paths, we can estimate the range of possible future prices and assess the risk associated with extreme price drops or gains.

Monte Carlo simulation provides a **dynamic view of risk**, as opposed to the **static view** provided by VaR. It generates a variety of potential future scenarios, offering insight into how asset prices might behave under different conditions.

## **Steps of the Project**

### **1. Data Loading and Preprocessing**

We start by downloading historical data for the **S&P 500** index using the `yfinance` library. The data includes daily prices from **1980 to 2024**, which are used to calculate **daily returns**. This preprocessing step is critical, as both the VaR calculations and Monte Carlo simulation depend on the historical returns.

### **2. Value at Risk (VaR) Calculations**

#### **a. Parametric VaR**

The **parametric VaR** calculation involves computing the **mean** and **standard deviation** of the historical daily returns and using these values to calculate the VaR at a specified confidence level (95% in this case).

#### **b. Historical VaR**

The **historical VaR** calculation involves sorting the historical daily returns and finding the 5th percentile (for 95% confidence), giving us the potential maximum loss over a given time period based on historical performance.

### **3. Monte Carlo Simulation**

The Monte Carlo simulation models thousands of possible future price paths for the S&P 500 based on its historical return statistics. The process involves:
- **Generating random daily returns** based on the mean and standard deviation of historical returns.
- **Simulating future prices** based on these returns, starting from the last available price.
- **Visualizing the simulated price paths**, providing insight into the range of possible future outcomes and risks.

## **Dependencies**

The project relies on several Python libraries to handle data processing, statistical analysis, and plotting. These libraries can be installed using the `requirements.txt` file.

### **Dependencies:**
- **`yfinance`**: For fetching historical financial data.
- **`pandas`**: For data manipulation and analysis.
- **`numpy`**: For numerical operations, such as calculating mean, standard deviation, and generating random returns.
- **`matplotlib`**: For plotting simulated price paths and comparing them to actual prices.
- **`scipy`**: For statistical functions like Z-scores used in the parametric VaR calculation.

## **Project Structure**

portfolio-risk-analysis/ │ ├── data/ # Contains downloaded data files │ └── sp500.csv ├── src/ │ ├── data_loader.py # Script to download and preprocess data │ ├── var_calculator.py # VaR calculation scripts │ ├── monte_carlo_simulator.py # Monte Carlo simulation script │ ├── utils/ # Utility functions │ ├── var_calculator_utils.py # Helper functions for VaR │ └── plotting_utils.py # Plotting helper functions │ ├── requirements.txt # Project dependencies └── README.md # Project overview and instructions


## **Usage**

To run the project locally:
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your_username/portfolio-risk-analysis.git
   cd portfolio-risk-analysis
2. ** Install dependencies**:
    ```bash
    pip install -r requirements.txt
3. ** Run the main script**:
    ```bash
    python main.py

This will:

Download the S&P 500 data (if not already downloaded).
Calculate Parametric and Historical VaR.
Run Monte Carlo simulations to project future prices.
Further Improvements

Some future improvements and extensions to the project could include:

Advanced volatility modeling: Use GARCH models to capture time-varying volatility.
Jump diffusion models: Model sudden, large market moves that aren't captured by the normal distribution.
Stochastic volatility models: Use more sophisticated models such as the Heston model for better risk assessment in volatile markets.
Portfolio simulations: Extend the project to simulate the risk of a diversified portfolio instead of a single asset (S&P 500).