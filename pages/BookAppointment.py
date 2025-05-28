import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

# Set light blue background color
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
            
    body {
        background-color: #a8e5d2;
    }
    .stApp {
        background-color: #a8e5d2;
    }
    </style>
    """,
    unsafe_allow_html=True)

st.title("📅 Book an Appointment")

# Input fields
name = st.text_input("Name", placeholder="Enter your full name")
phone = st.text_input("Phone Number", placeholder="Enter your phone number")
appointment_date = st.date_input("Date of Appointment")
appointment_time = st.time_input("Time of Appointment")

# Doctor selection dropdown
doctors = {
    "Dr. A. Mehta – Cardiologist",
    "Dr. B. Sharma – Endocrinologist",
    "Dr. C. Reddy – General Physician",
    "Dr. D. Iyer – Neurologist",
    "Dr. E. Singh – Orthopedic Surgeon",
    "Dr. F. Gupta – Pulmonologist",
    "Dr. G. Desai – Psychiatrist",
    "Dr. H. Khan – Dermatologist"
}
selected_doctor = st.selectbox("Select Doctor", sorted(doctors))

# Email credentials
SENDER_EMAIL = "archanabbiradar123@@gmail.com"  # Use your email
APP_PASSWORD = "shdj dxft tvwl ybwe"  # App password
RECEIVER_EMAIL = "archanabbiradar123@gmail.com"  # Destination email

# Submit button
if st.button("Submit"):
    if name and phone and selected_doctor and appointment_date and appointment_time:
        try:
            # Email construction
            msg = MIMEMultipart()
            msg["From"] = SENDER_EMAIL
            msg["To"] = RECEIVER_EMAIL
            msg["Subject"] = f"🩺 New Appointment Booking: {name}"
            
            email_content = (
                f"Name: {name}\n"
                f"Phone: {phone}\n"
                f"Doctor: {selected_doctor}\n"
                f"Date: {appointment_date.strftime('%Y-%m-%d')}\n"
                f"Time: {appointment_time.strftime('%H:%M')}"
            )
            msg.attach(MIMEText(email_content, "plain"))

            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(SENDER_EMAIL, APP_PASSWORD)
                server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())

            st.success("✅ Appointment booked successfully! We will contact you soon.")
        except Exception as e:
            st.error(f"❌ Error sending appointment request: {e}")
    else:
        st.warning("⚠️ Please fill in all fields before submitting.")

# Back button
if st.button("⬅️ Back to Home"):
    st.switch_page(r"C:\Users\My pc\Dropbox\PC\Desktop\MP_authentication_21stMay_Final\pages\02LandingPage.py")
