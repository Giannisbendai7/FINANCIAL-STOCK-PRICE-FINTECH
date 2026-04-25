from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("stock_model.pkl")

@app.get("/")
def home():
    return {"message": "Stock Prediction API running"}

@app.post("/predict")
def predict(data: dict):

    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]

    return {"prediction": int(prediction)}
