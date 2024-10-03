import re
import requests
import streamlit as st

WEBHOOK_URL = st.secrets["WEBHOOK_URL"]

def is_valid_email(email):
    # Basic regex for email validation
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_regex, email) is not None # Boolean

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("First Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button("Submit")
        
        if submit_button:
            if not WEBHOOK_URL:
                st.error("Email service is not set up. Please try again later.", icon="📧")
                st.stop()
                
            if not name:
                st.error("Please provide your name.", icon="👤")
                st.stop()
                
            if not email:
                st.error("Please provide your email.", icon="📨")
                st.stop()
                
            if not is_valid_email(email):
                st.error("Please provide a valid email.", icon="📧")
                st.stop()
                
            if not message:
                st.error("Please provide a message.", icon="💬")
                st.stop()
            
            # Prepare the data payload and send it to the webhook
            data = {
                "name": name,
                "email": email,
                "message": message
            }
            response = requests.post(WEBHOOK_URL, json=data)
            
            if response.status_code == 200:
                st.success("Message sent successfully!", icon="🚀")
            else:
                st.error("Failed to send message. Please try again later.", icon="❌")
            