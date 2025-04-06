import streamlit as st
import pandas as pd
import random
import smtplib
from time import sleep


def generate_otp():
    otp = random.randint(100000, 999999)
    return otp

def send_otp_email(email, otp):
    sender_email = "harimilan1203@gmail.com"  
    sender_password = "zzvo cgvd kxbv ubfo"  
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  
        server.starttls()  
        server.login(sender_email, sender_password)
        
        subject = "Loan Application OTP Verification"
        body = f"Your OTP for loan application verification is: {otp}"
        message = f"Subject: {subject}\n\n{body}"
        
        server.sendmail(sender_email, email, message)
        server.quit()
        st.success(f"OTP has been sent to your email: {email}")
    except smtplib.SMTPException as e:
        st.error(f"Failed to send email due to an SMTP error: {str(e)}")
    except Exception as e:
        st.error(f"Failed to send email due to an unexpected error: {str(e)}")

csv_file_path = "data/users.csv"

st.title("OTP Verification for Loan Application")
st.write("Pls check Spam mail Folder for the OTP if not found in Primary Folder")

email_input = st.text_input("Enter your email address to verify")

df = pd.read_csv(csv_file_path)

if st.button("Request OTP"):
    if email_input:
        user_data = df[(df['Email'] == email_input)]
        
        if not user_data.empty:
            otp = generate_otp()
            
            send_otp_email(email_input, otp)
            
            st.session_state.otp = otp
            st.session_state.email_input = email_input
        else:
            st.error("No matching data found for the provided email.")
    else:
        st.error("Please provide an email address.")

otp_input = st.text_input("Enter the OTP sent to your email")

if st.button("Verify OTP"):
    if otp_input and hasattr(st.session_state, 'otp') and str(st.session_state.otp) == otp_input:
        st.success("OTP verified successfully! Your loan application is being processed.")
    else:
        st.error("Invalid OTP or OTP expired. Please try again.")
