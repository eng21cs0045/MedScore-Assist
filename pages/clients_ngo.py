# clients_ngo.py
import streamlit as st
from PIL import Image


st.set_page_config(layout="wide")

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

            .main {
                padding: 0rem 1rem;
            }
            header, footer {
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
            
            /* Adjust main content to take full width when sidebar is hidden */
            .main .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
                max-width: 100%;

            }
    </style>
    """,
    unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 4, 1])
with col1:
    logo = Image.open("mda.jpg")
    st.image(logo, width=180)
with col2:
    st.markdown("<h1 style='text-align: center; font-weight: bold;'>MEDSCORE ASSIST</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>🤝 NGO Collaborations</h2>", unsafe_allow_html=True)

# Intro
st.markdown("""
<div style="text-align: center; font-size: 30px; margin-bottom: 40px;">
    Medscore Assist is honored to work with NGOs promoting preventive healthcare and wellness in underserved communities.
</div>
""", unsafe_allow_html=True)

st.markdown("<h3 style='color: #00ae99;'>Our NGO Partners:</h3>", unsafe_allow_html=True)

ngo_data = [
    {"name": "HealthAid Foundation", "emoji": "❤️", "address": "12 Care Lane, Welltown", "phone": "+1-888-123-0001", "info": "Focused on rural health outreach in tribal areas with mobile units and volunteer doctors."},
    {"name": "WellBeing Alliance", "emoji": "🌿", "address": "34 Harmony Blvd, KindCity", "phone": "+1-888-123-0002", "info": "Runs mental health helplines and awareness drives across cities."},
    {"name": "HopeMed Trust", "emoji": "🕊️", "address": "98 Trust Road, Peaceville", "phone": "+1-888-123-0003", "info": "Operates mobile vans for free medical checkups in conflict zones."},
    {"name": "CareBridge NGO", "emoji": "🌉", "address": "56 Unity Ave, Helpburg", "phone": "+1-888-123-0004", "info": "Organizes mass vaccination and hygiene education events."},
    {"name": "BrightCare Foundation", "emoji": "🌞", "address": "78 Bright Road, Healview", "phone": "+1-888-123-0005", "info": "Supports women’s health with gynecology camps and prenatal guidance."},
    {"name": "CompassionAid", "emoji": "🤗", "address": "88 Mercy Blvd, Goodwill Town", "phone": "+1-888-123-0006", "info": "Delivers nutrition packs and runs anemia detection campaigns."},
]

cols = st.columns(2)
for i, ngo in enumerate(ngo_data):
    with cols[i % 2]:
        st.markdown(
            f"""
            <div style='background-color: #f1fdfc; padding: 25px; border-radius: 15px; margin-bottom: 20px;'>
                <h3 style='font-size: 24px;'>{ngo["emoji"]} <strong>{ngo["name"]}</strong></h3>
                <p style='font-size: 18px;'>📍 <strong>Address:</strong> {ngo["address"]}<br>
                📞 <strong>Phone:</strong> {ngo["phone"]}<br>
                📝 <strong>Info:</strong> {ngo["info"]}</p>
            </div>
            """, unsafe_allow_html=True
        )

st.markdown("""
    <br><br>
    <div style='background-color: #e0f7f4; padding: 30px; border-radius: 10px; text-align: center;'>
        <h3 style='color: #00796b;'>Partner with Medscore Assist</h3>
        <p style='font-size: 18px;'>Enhance your NGO’s outreach with AI-powered health screening and real-time analytics for communities in need.</p>
        <p style='font-size: 18px;'>📧 contact@medscoreassist.com | 📞 +1-800-999-9999</p>
    </div>
""", unsafe_allow_html=True)
