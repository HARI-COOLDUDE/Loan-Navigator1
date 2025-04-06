import streamlit as st
from loan_form_handler import handle_loan_submission

st.title("🚗 Vehicle Loan")

if "user_email" not in st.session_state:
    st.error("You must be logged in to apply.")
    st.stop()


with st.form("veh_form"):
    vehicle= st.text_input("Type of Vehicle")
    amount = st.number_input("Loan Amount", min_value=10000)
    tenure = st.selectbox("Loan Tenure (years)", [1, 2, 3, 4, 5])
    submitted = st.form_submit_button("Submit Application")

    if submitted:
        fields = {
            "Vehicle":vehicle,
            "Amount": amount,
            "Tenure": tenure
        }

        handle_loan_submission("Vehicle", fields, st.session_state["user_email"])
        st.success("🎉 Vehicle loan application submitted successfully!")
