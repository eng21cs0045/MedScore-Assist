import streamlit as st
from PIL import Image

# Set wide layout
st.set_page_config(layout="wide")

# Custom CSS to remove Streamlit padding and style client boxes
st.markdown("""
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
            
        .main {
            padding: 0rem 1rem;
        }
        footer {
            visibility: hidden;
        }
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }
        .client-box {
            background-color: #f1fdfc;
            padding: 20px;
            margin-bottom: 10px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([2, 4, 1])
with col1:
    logo = Image.open("mda.jpg")
    st.image(logo, width=180)
with col2:
    st.markdown("<h1 style='text-align: center; font-weight: bold;'>WELCOME TO MEDSCORE ASSIST</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>🏥 Hospital Partners</h2>", unsafe_allow_html=True)

# Intro
st.markdown("""
<div style="text-align: center; font-size: 30px; margin-bottom: 40px;">
    Welcome to our Hospital Partner hub. Medscore Assist collaborates with top healthcare institutions to enhance patient outcomes with predictive health insights.
</div>
""", unsafe_allow_html=True)

# Collaborations Header
st.markdown("<h3 style='color: #00ae99;'>Our Collaborations Include:</h3>", unsafe_allow_html=True)

# Define client data for hospitals
hospitals = [
    {
        "name": "🏥 HeartCare Hospital",
        "address": "123 Cardiology St, Heart City",
        "phone": "+1-800-123-4567",
        "desc": "Specializes in heart disease prevention and treatment."
    },
    {
        "name": "🏥 VitalMed Clinic",
        "address": "45 Wellness Ave, Meditown",
        "phone": "+1-800-234-5678",
        "desc": "Comprehensive medical services with focus on preventative care."
    },
    {
        "name": "🏥 Lifecare Medical Center",
        "address": "789 Healthy Blvd, Life City",
        "phone": "+1-800-345-6789",
        "desc": "Innovative healthcare solutions for early detection and prevention."
    }
]

# Render hospitals in rows of 3 using columns
for i in range(0, len(hospitals), 3):
    cols = st.columns(3)
    for col, hospital in zip(cols, hospitals[i:i+3]):
        col.markdown(f"""
        <div style='background-color: #f1fdfc; padding: 20px; border-radius: 10px; height: 280px;'>
            <h4 style='font-size: 24px;'>{hospital['name']}</h4>
            <p style='font-size: 20px;'>📍 {hospital['address']}</p>
            <p style='font-size: 20px;'>📞 {hospital['phone']}</p>
            <p style='font-size: 18px;'>{hospital['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

# Optional footer to fill page
st.markdown("""
    <br><br>
    <div style='background-color: #e0f7f4; padding: 30px; border-radius: 10px; text-align: center;'>
        <h4 style='color: #00796b;'>Partner with Medscore Assist</h4>
        <p style='font-size: 18px;'>Elevate your hospital's health strategy with AI-driven solutions and personalized care plans.</p>
        <p style='font-size: 18px;'>📧 contact@medscoreassist.com | 📞 +1-800-999-9999</p>
    </div>
""", unsafe_allow_html=True)
