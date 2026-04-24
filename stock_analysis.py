import yfinance as yf

# download stock data
df = yf.download("AAPL", period="1mo")

print(df.head())
print("Data loaded successfully!")
