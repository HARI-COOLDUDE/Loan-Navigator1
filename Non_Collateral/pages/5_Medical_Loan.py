import streamlit as st
from loan_form_handler import handle_loan_submission

st.title("🩺 Medical Loan")

if "user_email" not in st.session_state:
    st.error("You must be logged in to apply.")
    st.stop()


with st.form("med_form"):
    med_problem= st.text_input("Type of Medical Problem")
    hospital= st.text_input("Name of Hospital")
    amount = st.number_input("Loan Amount", min_value=100000)
    tenure = st.selectbox("Loan Tenure (years)", [1, 2, 3, 4, 5])
    submitted = st.form_submit_button("Submit Application")

    if submitted:
        fields = {
            "Medical Problem":med_problem,
            "Hospital": hospital,
            "Amount": amount,
            "Tenure": tenure
        }

        handle_loan_submission("Medical", fields, st.session_state["user_email"])
        st.success("🎉 Medical loan application submitted successfully!")
