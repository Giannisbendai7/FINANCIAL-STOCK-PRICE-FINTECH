import yfinance as yf
import pandas as pd

# download data
df = yf.download("AAPL", period="6mo")

# features
df['MA_5'] = df['Close'].rolling(5).mean()
df['MA_20'] = df['Close'].rolling(20).mean()
df['Return'] = df['Close'].pct_change()

# target (up/down next day)
df['Target'] = (df['Close'].shift(-1) > df['Close']).astype(int)

# clean
df.dropna(inplace=True)

# ML
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

X = df[['Close', 'MA_5', 'MA_20', 'Return']]
y = df['Target']

X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False)

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Model trained ✔")
print(classification_report(y_test, y_pred))

# save model
import joblib
joblib.dump(model, "stock_model.pkl")

print("Pipeline completed successfully ✔")

import joblib
joblib.dump(model, "stock_model.pkl")
