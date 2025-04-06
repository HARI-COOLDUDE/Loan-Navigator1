import pandas as pd
import pickle
import os

MODEL_PATH = "models/polynomial_model.pkl"
DATA_PATH = "data/loan_selection.csv"

with open(MODEL_PATH, "rb") as f:
    poly, model = pickle.load(f)

def predict_loan_approval(user_email):
    try:
        df = pd.read_csv(DATA_PATH)
        user_data = df[df["Email"] == user_email]

        if user_data.empty:
            return None, "No data found for the provided email."

        X = user_data[["Loan Amount", "Loan Tenure", "Annual Income"]]
        X_poly = poly.transform(X)
        prediction = model.predict(X_poly)
        approved = prediction[0] >= 0.5

        return approved, None
    except Exception as e:
        return None, str(e)
