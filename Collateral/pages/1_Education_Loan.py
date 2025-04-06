import streamlit as st
from loan_form_handler import handle_loan_submission

st.title("🎓 Education Loan Application")

if "user_email" not in st.session_state:
    st.error("You must be logged in to apply.")
    st.stop()

with st.form("edu_form"):
    course = st.text_input("Course Name")
    institution = st.text_input("Institution Name")
    amount = st.number_input("Loan Amount", min_value=100000)
    assests = st.number_input("Assests", min_value=200000)
    tenure = st.selectbox("Loan Tenure (years)", [1, 2, 3, 4, 5])
    submitted = st.form_submit_button("Submit Application")

    if submitted:
        fields = {
            "Course": course,
            "Institution": institution,
            "Amount": amount,
            "Assests":assests,
            "Tenure": tenure
        }

        handle_loan_submission("Education", fields, st.session_state["user_email"])
        st.success("🎉 Education loan application submitted successfully!")
