import yfinance as yf

# download stock data
df = yf.download("AAPL", period="1mo")

print(df.head())
print("Data loaded successfully!")


import yfinance as yf
import pandas as pd

# download data
df = yf.download("AAPL", period="6mo")

# basic features
df['MA_5'] = df['Close'].rolling(5).mean()
df['MA_20'] = df['Close'].rolling(20).mean()

# summary stats
print("Dataset shape:", df.shape)
print(df.describe())

# save output (VERY important for CV)
df.to_csv("output_stock_data.csv")

print("Pipeline completed successfully ✔")
