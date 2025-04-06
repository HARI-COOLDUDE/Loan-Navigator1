import streamlit as st
from loan_form_handler import handle_loan_submission

st.title("🏠 Home Loan")

if "user_email" not in st.session_state:
    st.error("You must be logged in to apply.")
    st.stop()

with st.form("home_form"):
    type_of_home= st.text_input("Type of Home")
    amount = st.number_input("Loan Amount", min_value=1000000)
    tenure = st.selectbox("Loan Tenure (years)", [1, 2, 3, 4, 5])
    submitted = st.form_submit_button("Submit Application")

    if submitted:
        fields = {
            "Type of Home":type_of_home,
            "Amount": amount,
            "Tenure": tenure
        }

        handle_loan_submission("Home", fields, st.session_state["user_email"])
        st.success("🎉 Home loan application submitted successfully!")
