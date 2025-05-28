# clients_rwa.py
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
            
            /* Adjust main content to take full width when sidebar is hidden */
            .main .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
                max-width: 100%;
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
    </style>
    """,
    unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 4, 1])
with col1:
    logo = Image.open("mda.jpg")
    st.image(logo, width=180)
with col2:
    st.markdown("<h1 style='text-align: center; font-weight: bold;'>MEDSCORE ASSIST</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>🏘️ RWA Partners</h2>", unsafe_allow_html=True)
st.write("We collaborate with Resident Welfare Associations (RWAs) to promote healthy living environments through proactive health services.")

st.markdown("<h3 style='color: #00ae99;'>Active RWAs:</h3>", unsafe_allow_html=True)

rwa_data = [
    {"name": "Green Meadows RWA", "emoji": "🌳", "address": "101 Eco Road, Greenville", "phone": "+1-800-456-1001", "info": "Organizes annual wellness expos and green drives."},
    {"name": "Sunrise Towers RWA", "emoji": "🌅", "address": "202 Dawn St, Sunview", "phone": "+1-800-456-1002", "info": "Hosts monthly yoga sessions and doctor talks."},
    {"name": "Lakefront Residency", "emoji": "🏞️", "address": "303 Lake Ave, Watercity", "phone": "+1-800-456-1003", "info": "Facilitates weekly checkups for elderly residents."},
    {"name": "Skyline Heights RWA", "emoji": "🏙️", "address": "404 Skyline Blvd, Urbanspace", "phone": "+1-800-456-1004", "info": "Runs digital health awareness campaigns."},
    {"name": "Oakridge Villas", "emoji": "🌲", "address": "505 Nature Way, Greenhill", "phone": "+1-800-456-1005", "info": "Free BMI and heart checkups every quarter."},
    {"name": "Crystal Bay Homes", "emoji": "🏖️", "address": "606 Beachfront Blvd, Crystal City", "phone": "+1-800-456-1006", "info": "Water aerobics and nutrition coaching for residents."},
]

cols = st.columns(2)
for i, rwa in enumerate(rwa_data):
    with cols[i % 2]:
        st.markdown(
            f"""
            <div style='background-color: #f1fdfc; padding: 25px; border-radius: 15px; margin-bottom: 20px;'>
                <h3 style='font-size: 24px;'>{rwa["emoji"]} <strong>{rwa["name"]}</strong></h3>
                <p style='font-size: 18px;'>📍 <strong>Address:</strong> {rwa["address"]}<br>
                📞 <strong>Phone:</strong> {rwa["phone"]}<br>
                📝 <strong>Info:</strong> {rwa["info"]}</p>
            </div>
            """, unsafe_allow_html=True
        )

st.markdown("""
    <br><br>
    <div style='background-color: #e0f7f4; padding: 30px; border-radius: 10px; text-align: center;'>
        <h3 style='color: #00796b;'>Partner with Medscore Assist</h3>
        <p style='font-size: 18px;'>Bring wellness to your residential community with proactive screenings, awareness sessions, and tech-powered tools.</p>
        <p style='font-size: 18px;'>📧 contact@medscoreassist.com | 📞 +1-800-999-9999</p>
    </div>
""", unsafe_allow_html=True)
