import streamlit as st
import base64
from pathlib import Path
'''
from bg import set_background
set_background("loan_background.png")
'''
def set_background(image_file):
    """
    Sets a semi-transparent background image for a Streamlit app.
    """
    img_path = Path(image_file)
    with img_path.open("rb") as img_file:
        img_bytes = img_file.read()
    encoded_img = base64.b64encode(img_bytes).decode()

    st.markdown(f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(255,255,255,0.5), rgba(255,255,255,0.5)), 
                          url("data:image/jpeg;base64,{encoded_img}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """, unsafe_allow_html=True)
