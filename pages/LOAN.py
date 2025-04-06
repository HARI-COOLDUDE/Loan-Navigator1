import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.title("Loan Applications")
st.subheader("Please fill out the form to apply for a loan")

name = st.text_input("Full Name")
aadhar_number = st.text_input("Aadhar Number (12 digits)", max_chars=12)
pan_number = st.text_input("PAN Number (in CAPITALS)")
email = st.text_input("Email Address")
phone_number = st.text_input("Phone Number (10 digits)", max_chars=10)
annual_income = st.number_input("Annual Income (in INR)", min_value=0)
loan_amount = st.number_input("Loan Amount Requested (in INR)", min_value=0)
loan_tenure = st.selectbox("Loan Tenure", options=["12 months", "24 months", "36 months", "48 months", "60 months"])

submit_button = st.button("Submit Application")

csv_file_path = "Loan_selection.csv"

def save_data_to_csv(data):
    if os.path.exists(csv_file_path):
        df = pd.read_csv(csv_file_path)
        df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    else:
        df = pd.DataFrame([data], columns=["Name", "Aadhar Number", "PAN Number", "Email", "Phone Number", "Annual Income", "Loan Amount", "Loan Tenure", "Timestamp"])
    df.to_csv(csv_file_path, index=False)

if submit_button:
    if name and aadhar_number and pan_number and email and phone_number and annual_income > 0 and loan_amount > 0:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = {
            "Name": name,
            "Aadhar Number": aadhar_number,
            "PAN Number": pan_number.upper(),  
            "Phone Number": phone_number,
            "Annual Income": annual_income,
            "Loan Amount": loan_amount,
            "Loan Tenure": loan_tenure,
            "Timestamp": timestamp
        }

        save_data_to_csv(data)

        st.success(f"Thank you, {name}! Your loan application has been submitted.")
        st.write(f"Loan Amount: ₹{loan_amount} for a {loan_tenure} term.")
        st.write("We will review your application and get back to you soon.")
    else:
        st.error("Please fill out all the fields correctly.")
