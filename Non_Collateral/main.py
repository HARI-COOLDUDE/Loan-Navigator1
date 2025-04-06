import streamlit as st

st.set_page_config(page_title="Non-Collateral Loan", layout="centered")

if "user_email" not in st.session_state:
    st.error("Please login to continue.")
    st.stop()

st.title("🏦 Welcome to the Non-Collateral Loan Portal")
st.markdown(f"Hello **{st.session_state.get('user_name', 'User')}**, please select a loan category:")

st.button("🎓 Education Loan", on_click=lambda: st.switch_page("Non Collateral/pages/1_Education_Loan.py"))
st.button("👤 Personal Loan", on_click=lambda: st.switch_page("Non Collateral/pages/2_Personal_Loan.py"))
st.button("🏠 Home Loan", on_click=lambda: st.switch_page("Non Collateral/pages/3_Home_Loan.py"))
st.button("🚗 Vehicle Loan", on_click=lambda: st.switch_page("Non Collateral/pages/4_Vehicle_Loan.py"))
st.button("🩺 Medical Loan", on_click=lambda: st.switch_page("Non Collateral/pages/5_Medical_Loan.py"))
