import streamlit as st

st.set_page_config(page_title="Loan Application Portal", layout="centered")
st.title("🏦 Welcome to the Loan Application Portal")
st.write("Please register or login to continue.")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "email_verified" not in st.session_state:
    st.session_state.email_verified = False

col1, col2 = st.columns(2)
with col1:
    if st.button("Register"):
        st.switch_page("pages/auth_app.py")

with col2:
    if st.button("Login"):
        st.switch_page("pages/verification.py")  


st.button("Collateral Loan", on_click=lambda: st.page_link("Collateral/main.py"))
st.button("Non Collateral Loan", on_click=lambda: st.page_link("Non_Collateral/main.py"))