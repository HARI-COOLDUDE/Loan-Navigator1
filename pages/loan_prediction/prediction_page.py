import streamlit as st
from backend.predict_backend import predict_loan_approval

st.set_page_config(page_title="Loan Application Prediction", layout="centered")
st.title("🔮 Loan Application Approval Result")

if "user_email" not in st.session_state:
    st.error("You must be logged in to access this page.")
    st.stop()

email = st.session_state["user_email"]

st.markdown("Checking your loan eligibility...")

approved, error = predict_loan_approval(email)

if error:
    st.error(f"Error: {error}")
elif approved is None:
    st.warning("No application found. Please apply for a loan first.")
elif approved:
    st.success("✅ Loan Application Approved")
else:
    st.error("❌ Loan Application Not Approved")
