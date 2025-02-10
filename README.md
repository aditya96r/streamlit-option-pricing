# Option Pricing with the Black-Scholes Model

## Overview
This project implements the **Black-Scholes model** for European option pricing and includes calculations for the **Greeks**, which measure sensitivities to different parameters. The project features a **Streamlit web application** that allows users to input option parameters and visualize the option price along with a **volatility smile**.

## Black-Scholes Model
The Black-Scholes formula is used to calculate the price of European call and put options. The formula is:

### Call Option Price:
$$
C = S \cdot N(d_1) - K \cdot e^{-rT} \cdot N(d_2)
$$

### Put Option Price:
$$
P = K \cdot e^{-rT} \cdot N(-d_2) - S \cdot N(-d_1)
$$

Where:
- \( S \) = Spot price (current price of the underlying asset)
- \( K \) = Strike price (price at which option is exercised)
- \( T \) = Time to maturity (in years)
- \( r \) = Risk-free interest rate
- \( \sigma \) = Volatility of the asset
- \( N(x) \) = Cumulative standard normal distribution function
- \( d_1 \) and \( d_2 \) are calculated as:

$$
 d_1 = \frac{\ln(S/K) + (r + 0.5\sigma^2)T}{\sigma\sqrt{T}}
$$

$$
 d_2 = d_1 - \sigma\sqrt{T}
$$

### How Parameters Affect Option Pricing
- **Spot Price (S)**: Higher spot price increases call option price and decreases put option price.
- **Strike Price (K)**: Higher strike price decreases call option price and increases put option price.
- **Time to Maturity (T)**: More time generally increases the price of both calls and puts.
- **Risk-Free Rate (r)**: A higher risk-free rate increases call option prices and decreases put option prices.
- **Volatility (\( \sigma \))**: Higher volatility increases both call and put option prices since the potential for extreme price movement increases.

## Option Greeks
Greeks measure the sensitivity of the option price to various factors:
- **Delta (\( \Delta \))**: Measures the rate of change of the option price with respect to the underlying asset price.
- **Gamma (\( \Gamma \))**: Measures how much delta changes when the underlying price moves.
- **Vega (\( \nu \))**: Measures sensitivity to changes in volatility.
- **Theta (\( \Theta \))**: Measures time decay of the option price.
- **Rho (\( \rho \))**: Measures sensitivity to changes in interest rates.

### Greek Formulas
$$
\Delta = N(d_1) \quad \text{(for calls)}, \quad N(d_1) - 1 \quad \text{(for puts)}
$$

$$
\Gamma = \frac{N'(d_1)}{S\sigma\sqrt{T}}
$$

$$
\nu = S N'(d_1) \sqrt{T}
$$

$$
\Theta = -\frac{S N'(d_1) \sigma}{2 \sqrt{T}} - rK e^{-rT} N(d_2)
$$

$$
\rho = K T e^{-rT} N(d_2)
$$

## How to Use This Project
### 1. Run the Streamlit App
Install dependencies:
```sh
pip install streamlit numpy scipy matplotlib
```
Run the app:
```sh
streamlit run streamlit_app.py
```

### 2. Features
- **Interactive Sliders**: Adjust option parameters (Spot price, Strike price, Time to maturity, Risk-free rate, Volatility, and Option type).
- **Option Price Calculation**: Displays real-time option prices.
- **Greek Calculation**: Shows Delta, Gamma, Vega, Theta, and Rho.
- **Volatility Smile Visualization**: Displays implied volatility against strike price.

## Example
To price a **call option** with:
- Spot Price \( S = 100 \)
- Strike Price \( K = 100 \)
- Time to Maturity \( T = 1 \) year
- Risk-Free Rate \( r = 5\% \)
- Volatility \( \sigma = 20\% \)

The price would be:
```python
from black_scholes_module import black_scholes
price = black_scholes(100, 100, 1, 0.05, 0.2, "call")
print(price)  # Output: ~10.45
```

## Conclusion
This project provides an interactive way to understand and calculate option prices and Greeks using the Black-Scholes model. The Streamlit app enables hands-on exploration of how different parameters affect pricing.

