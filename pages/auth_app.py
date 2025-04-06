import streamlit as st
import pandas as pd
import os
import hashlib

DATA_FILE = "data/users.csv"

if not os.path.exists("data"):
    os.makedirs("data")
if not os.path.exists(DATA_FILE):
    pd.DataFrame(columns=["Name", "Email", "Password"]).to_csv(DATA_FILE, index=False)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    return pd.read_csv(DATA_FILE)

def save_user(name, email, password):
    df = load_users()
    new_user = {"Name": name, "Email": email, "Password": hash_password(password)}
    df = pd.concat([df, pd.DataFrame([new_user])], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)

def check_login(email, password):
    df = load_users()
    hashed_pw = hash_password(password)
    user = df[(df["Email"] == email) & (df["Password"] == hashed_pw)]
    return not user.empty

def email_exists(email):
    df = load_users()
    return email in df["Email"].values

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_email" not in st.session_state:
    st.session_state.user_email = ""
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

st.set_page_config(page_title="Auth System", layout="centered")
st.title("🔐 Welcome to Loan Portal - Register/Login")

tabs = st.tabs(["Register", "Login"])

with tabs[0]:
    st.subheader("📝 Create Account")
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Register"):
        if not name or not email or not password:
            st.error("All fields are required.")
        elif password != confirm_password:
            st.error("Passwords do not match.")
        elif email_exists(email):
            st.error("Email already registered.")
        else:
            save_user(name, email, password)
            st.success("Registration successful! Please log in.")

with tabs[1]:
    st.subheader("🔑 Login")
    login_email = st.text_input("Login Email")
    login_password = st.text_input("Login Password", type="password")

    if st.button("Login"):
        if check_login(login_email, login_password):
            st.session_state.logged_in = True
            st.session_state.user_email = login_email
            st.session_state.user_name = load_users().query("Email == @login_email")["Name"].values[0]
            st.success(f"Welcome, {st.session_state.user_name}!")
            st.balloons()
        else:
            st.error("Invalid credentials.")

# Display session
if st.session_state.logged_in:
    st.success(f"✅ Logged in as {st.session_state.user_name} ({st.session_state.user_email})")
