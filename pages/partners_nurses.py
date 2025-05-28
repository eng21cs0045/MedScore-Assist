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

st.markdown("<h2 style='text-align: center;'>👩‍⚕️ Nurse Partners</h2>", unsafe_allow_html=True)

# Intro
st.markdown("""
<div style="text-align: center; font-size: 30px; margin-bottom: 40px;">
    Medscore Assist partners with nurses to help provide preventative care and real-time health monitoring for patients.
</div>
""", unsafe_allow_html=True)

# Collaborations Header
st.markdown("<h3 style='color: #00ae99;'>Our Collaborations Include:</h3>", unsafe_allow_html=True)

# Define client data for nurses
nurses = [
    {
        "name": "👩‍⚕️ HealthPro Nurses",
        "address": "123 Care Ave, Healthtown",
        "phone": "+1-800-234-5678",
        "desc": "Provides home healthcare services for elderly and chronic patients."
    },
    {
        "name": "👩‍⚕️ VitalCare Nursing",
        "address": "56 Wellness Rd, Vitality City",
        "phone": "+1-800-345-6789",
        "desc": "Offers nursing care services for pre- and post-operative patients."
    },
    {
        "name": "👩‍⚕️ NurseLink Health",
        "address": "789 Recovery Blvd, Heal City",
        "phone": "+1-800-456-7890",
        "desc": "Focuses on patient education and chronic disease management."
    }
]

# Render nurses in rows of 3 using columns
for i in range(0, len(nurses), 3):
    cols = st.columns(3)
    for col, nurse in zip(cols, nurses[i:i+3]):
        col.markdown(f"""
        <div style='background-color: #f1fdfc; padding: 20px; border-radius: 10px; height: 280px;'>
            <h4 style='font-size: 24px;'>{nurse['name']}</h4>
            <p style='font-size: 20px;'>📍 {nurse['address']}</p>
            <p style='font-size: 20px;'>📞 {nurse['phone']}</p>
            <p style='font-size: 18px;'>{nurse['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

# Optional footer to fill page
st.markdown("""
    <br><br>
    <div style='background-color: #e0f7f4; padding: 30px; border-radius: 10px; text-align: center;'>
        <h4 style='color: #00796b;'>Partner with Medscore Assist</h4>
        <p style='font-size: 18px;'>Join us in improving patient care with AI-driven solutions and personalized health assessments.</p>
        <p style='font-size: 18px;'>📧 contact@medscoreassist.com | 📞 +1-800-999-9999</p>
    </div>
""", unsafe_allow_html=True)
