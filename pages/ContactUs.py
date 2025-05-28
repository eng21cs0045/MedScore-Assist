import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

st.markdown(
    """
    <style>
    /* Hide the sidebar completely */
            .css-1d391kg {
                display: none;
            }
            
            .css-1aumxhk {
                display: none;
            }
            
            /* Hide sidebar in newer Streamlit versions */
            section[data-testid="stSidebar"] {
                display: none !important;
            }
            
            /* Hide the sidebar toggle button */
            button[kind="header"] {
                display: none;
            }
            
            /* Adjust main content to take full width when sidebar is hidden */
            .main .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
                max-width: 100%;
            }
    </style>
    """,
    unsafe_allow_html=True)

st.title("📞 Contact Us")

# User input fields
name = st.text_input("Name", placeholder="Enter your name")
user_email = st.text_input("Your Email", placeholder="Enter your email")
message = st.text_area("Message", placeholder="Enter your message")

# Your email credentials (Use an App Password)
SENDER_EMAIL = "archanabbiradar123@@gmail.com"  # Replace with your Gmail
APP_PASSWORD = "shdj dxft tvwl ybwe"  # Replace with your App Password
RECEIVER_EMAIL = "archanabbiradar123@gmail.com"  # Fixed receiver email

if st.button("Submit"):
    if name and user_email and message:
        try:
            # Create email message using MIME
            msg = MIMEMultipart()
            msg["From"] = SENDER_EMAIL  # Your Gmail (Used for sending)
            msg["To"] = RECEIVER_EMAIL  # Receiver's email
            msg["Subject"] = f"New Contact Form Submission from {name}"
            msg["Reply-To"] = user_email  # Allows replies to go to the user's email

            # Email body (Plain text, no Base64 encoding)
            email_content = f"Name: {name}\nEmail: {user_email}\nMessage: {message}"
            msg.attach(MIMEText(email_content, "plain"))

            # Send email using SMTP
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(SENDER_EMAIL, APP_PASSWORD)
                server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())

            st.success("✅ Message sent successfully! You will be replied to at your email.")
        except Exception as e:
            st.error(f"❌ Error sending message: {e}")
    else:
        st.warning("⚠️ Please fill in all fields before submitting.")
# 🡐 Back Button to go to main_app.py
if st.button("⬅️ Back to Home"):
    st.switch_page(r"C:\Users\My pc\Dropbox\PC\Desktop\MP_authentication_21stMay_Final\pages\02LandingPage.py")
