import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from black_scholes_module import black_scholes, calculate_greeks

#building streamlit App 

st.title('Option Pricing')

st.sidebar.header('Options Parameters')
spot_price = st.sidebar.slider('Spot Price(S)', 50,250,100)
strike_price = st.sidebar.slider('Strike Price(K)', 50,250,100)
time_to_maturity = st.sidebar.slider('Time to maturity(T, Years)', 0.1,5.0,1.0,0.1)
risk_free_rate = st.sidebar.slider("Risk-Free Rate(r)",0.0,1.0,0.05,0.01)
volatility = st.sidebar.slider("volatility(σ))",0.0,1.0,0.05,0.01)
option_type = st.sidebar.radio("Option Type", ['Call', 'put'])

#calculate option price
price = black_scholes(spot_price,strike_price,time_to_maturity,risk_free_rate,volatility,option_type.lower())
st.write (f'###{option_type} option price: ${price:.2f}')

#calculating greeks

delta, gamma, vega, theta, rho = calculate_greeks(spot_price,strike_price,time_to_maturity,risk_free_rate,volatility)
st.write('### Greeks')
st.write(f'**Delta**: {delta:.2f}')
st.write(f'**Gamma**: {gamma:.2f}')
st.write(f'**Vega**: {vega:.2f}')
st.write(f'**Theta**: {theta:.2f}')
st.write(f'**Rho**: {rho:.2f}')

#volatilty Smile

# Title
st.write('### Volatility Smile')

# Generate strike prices
strike_price = np.linspace(50, 150, 100)

# Define implied volatility (example: dummy smile curve)
volatility = 0.2  # Base volatility
implied_vols = [volatility + 0.1 * np.exp(-(x - 100)**2 / (2 * 300)) for x in strike_price]

# Plot the volatility smile
plt.figure(figsize=(10, 5))
plt.plot(strike_price, implied_vols, label="Implied Volatility")
plt.xlabel('Strike Price')
plt.ylabel('Implied Volatility')
plt.title('Volatility Smile')
plt.legend()
st.pyplot(plt)
