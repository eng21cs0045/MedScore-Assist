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

st.markdown("<h2 style='text-align: center;'>👨‍⚕️ Doctor Partners</h2>", unsafe_allow_html=True)

# Intro
st.markdown("""
<div style="text-align: center; font-size: 30px; margin-bottom: 40px;">
    Medscore Assist partners with doctors to integrate AI solutions in healthcare for more accurate and timely diagnosis.
</div>
""", unsafe_allow_html=True)

# Collaborations Header
st.markdown("<h3 style='color: #00ae99;'>Our Collaborations Include:</h3>", unsafe_allow_html=True)

# Define client data for doctors
doctors = [
    {
        "name": "👨‍⚕️ HealthFirst Clinic",
        "address": "123 Wellness Rd, Medicity",
        "phone": "+1-800-234-5678",
        "desc": "Experts in primary healthcare with a focus on disease prevention."
    },
    {
        "name": "👨‍⚕️ MedPlus Care",
        "address": "45 Cure Ave, Healthville",
        "phone": "+1-800-345-6789",
        "desc": "Leading healthcare provider with AI-driven patient management."
    },
    {
        "name": "👨‍⚕️ VitalMed Specialists",
        "address": "89 Treatment Blvd, Vitality City",
        "phone": "+1-800-456-7890",
        "desc": "Specializes in high-tech diagnostics and personalized treatment plans."
    }
]

# Render doctors in rows of 3 using columns
for i in range(0, len(doctors), 3):
    cols = st.columns(3)
    for col, doctor in zip(cols, doctors[i:i+3]):
        col.markdown(f"""
        <div style='background-color: #f1fdfc; padding: 20px; border-radius: 10px; height: 280px;'>
            <h4 style='font-size: 24px;'>{doctor['name']}</h4>
            <p style='font-size: 20px;'>📍 {doctor['address']}</p>
            <p style='font-size: 20px;'>📞 {doctor['phone']}</p>
            <p style='font-size: 18px;'>{doctor['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

# Optional footer to fill page
st.markdown("""
    <br><br>
    <div style='background-color: #e0f7f4; padding: 30px; border-radius: 10px; text-align: center;'>
        <h4 style='color: #00796b;'>Partner with Medscore Assist</h4>
        <p style='font-size: 18px;'>Help enhance patient outcomes with personalized AI solutions and healthcare innovations.</p>
        <p style='font-size: 18px;'>📧 contact@medscoreassist.com | 📞 +1-800-999-9999</p>
    </div>
""", unsafe_allow_html=True)
