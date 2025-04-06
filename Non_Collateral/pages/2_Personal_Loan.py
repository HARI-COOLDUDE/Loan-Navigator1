import streamlit as st
from loan_form_handler import handle_loan_submission

st.title("👤 Personal Loan")

if "user_email" not in st.session_state:
    st.error("You must be logged in to apply.")
    st.stop()


with st.form("prsl_form"):
    Objective= st.text_input("Course Name")
    amount = st.number_input("Loan Amount", min_value=100000)
    tenure = st.selectbox("Loan Tenure (years)", [1, 2, 3, 4, 5])
    submitted = st.form_submit_button("Submit Application")

    if submitted:
        fields = {
            "Objective":Objective,
            "Amount": amount,
            "Tenure": tenure
        }

        handle_loan_submission("Personal", fields, st.session_state["user_email"])
        st.success("🎉 Personal loan application submitted successfully!")
