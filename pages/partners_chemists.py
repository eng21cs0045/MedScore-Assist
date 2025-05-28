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

st.markdown("<h2 style='text-align: center;'>💊 Chemist Partners</h2>", unsafe_allow_html=True)

# Intro
st.markdown("""
<div style="text-align: center; font-size: 30px; margin-bottom: 40px;">
    Medscore Assist partners with leading chemists and pharmacies to bring AI-powered health solutions directly to consumers.
</div>
""", unsafe_allow_html=True)

# Collaborations Header
st.markdown("<h3 style='color: #00ae99;'>Our Collaborations Include:</h3>", unsafe_allow_html=True)

# Define client data for chemists
chemists = [
    {
        "name": "💊 ChemistCare Pharmacy",
        "address": "123 Med Street, Pharma City",
        "phone": "+1-800-234-5678",
        "desc": "Offers personalized health assessments and medication tracking."
    },
    {
        "name": "💊 LifePharm Chemists",
        "address": "56 Health Ave, Mediville",
        "phone": "+1-800-345-6789",
        "desc": "Specializes in chronic condition management through pharmacy."
    },
    {
        "name": "💊 Wellness Pharmacies",
        "address": "78 Remedy Blvd, Healton",
        "phone": "+1-800-456-7890",
        "desc": "Focused on integrating preventive care with pharmacy services."
    }
]

# Render chemists in rows of 3 using columns
for i in range(0, len(chemists), 3):
    cols = st.columns(3)
    for col, chemist in zip(cols, chemists[i:i+3]):
        col.markdown(f"""
        <div style='background-color: #f1fdfc; padding: 20px; border-radius: 10px; height: 280px;'>
            <h4 style='font-size: 24px;'>{chemist['name']}</h4>
            <p style='font-size: 20px;'>📍 {chemist['address']}</p>
            <p style='font-size: 20px;'>📞 {chemist['phone']}</p>
            <p style='font-size: 18px;'>{chemist['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

# Optional footer to fill page
st.markdown("""
    <br><br>
    <div style='background-color: #e0f7f4; padding: 30px; border-radius: 10px; text-align: center;'>
        <h4 style='color: #00796b;'>Partner with Medscore Assist</h4>
        <p style='font-size: 18px;'>Expand your pharmacy's health offerings with personalized AI insights for your customers.</p>
        <p style='font-size: 18px;'>📧 contact@medscoreassist.com | 📞 +1-800-999-9999</p>
    </div>
""", unsafe_allow_html=True)
