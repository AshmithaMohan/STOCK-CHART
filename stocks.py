import yfinance as yf
import matplotlib.pyplot as plt

# Fetch stock data for a company (e.g., Apple)
stock_symbol = 'AAPL'  # Apple Inc.
data = yf.download(stock_symbol, start="2020-01-01", end="2025-01-01")

# Plot the closing price
plt.figure(figsize=(10,6))
plt.plot(data['Close'], label=f'{stock_symbol} Closing Price is')

max_price = data['Close'].max()
max_date = data['Close'].idxmax()
plt.scatter(max_date, max_price, color='red', label=f'Max Price: {max_price:.2f}')

plt.title(f'{stock_symbol} Stock Price Over Time is')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()