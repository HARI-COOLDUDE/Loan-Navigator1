import pandas as pd
import os

def handle_loan_submission(loan_type, fields, user_email, data_path="data/loan_data.csv"):
    entry = {"Loan Type": loan_type, "Email": user_email}
    entry.update(fields)

    if os.path.exists(data_path):
        df = pd.read_csv(data_path)
    else:
        df = pd.DataFrame()

    df = pd.concat([df, pd.DataFrame([entry])], ignore_index=True)
    df.to_csv(data_path, index=False)
