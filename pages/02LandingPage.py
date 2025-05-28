import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
import base64
from streamlit.runtime.scriptrunner import RerunData, RerunException
# from streamlit.source_util import get_pages
import os

def switch_page(page_name: str):
    # Standardize the page name (lowercase, no spaces/underscores)
    page_name = page_name.lower().replace("_", " ")
    
    # Get all pages from the main app file (usually "streamlit_app.py")
    pages = get_pages("streamlit_app.py")  # Replace if your main file has a different name
    
    # Find the matching page
    for page_hash, config in pages.items():
        if config["page_name"].lower().replace("_", " ") == page_name:
            raise RerunException(
                RerunData(
                    page_script_hash=page_hash,
                    page_name=page_name,
                )
            )
    
    # If page not found, show error
    available_pages = [p["page_name"] for p in pages.values()]
    st.error(f"Page '{page_name}' not found. Available pages: {available_pages}")

# Set page config for wide layout
st.set_page_config(layout="wide")

# CSS styles
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
        
        /* Hide the sidebar arrow/chevron - comprehensive targeting */
        .css-1vencpc {
            display: none !important;
        }
        
        /* Hide sidebar arrow in newer versions */
        button[data-testid="collapsedControl"] {
            display: none !important;
        }
        
        /* Hide any sidebar collapse/expand controls */
        .sidebar .sidebar-collapse {
            display: none !important;
        }
        
        /* Additional selectors for sidebar arrows */
        .css-1rs6os, .css-1vencpc, .css-17lntkn {
            display: none !important;
        }
        
        /* More comprehensive arrow hiding */
        [data-testid="stSidebarNav"] {
            display: none !important;
        }
        
        /* Hide all possible sidebar control elements */
        .css-1cypcdb, .css-1d391kg, .css-1aumxhk {
            display: none !important;
        }
        
        /* Target the sidebar chevron/arrow button specifically */
        button[title="Show sidebar navigation"] {
            display: none !important;
        }
        
        button[title="Hide sidebar navigation"] {
            display: none !important;
        }
        
        /* Hide any remaining sidebar navigation elements */
        .stSidebar, .css-1lcbmhc, .css-1outpf7 {
            display: none !important;
        }
        
        /* Universal sidebar element hiding */
        [class*="sidebar"], [class*="Sidebar"] {
            display: none !important;
        }
        
        /* Hide elements with chevron or arrow icons */
        button svg[data-testid="chevron-left"],
        button svg[data-testid="chevron-right"] {
            display: none !important;
        }
        
        /* Hide parent button if it contains chevron */
        button:has(svg[data-testid="chevron-left"]),
        button:has(svg[data-testid="chevron-right"]) {
            display: none !important;
        }
        
        /* Adjust main content to take full width when sidebar is hidden */
        .main .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
            max-width: 100%;
        }
        
        .medscore-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #eee;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }
        .medscore-logo {
            height: 60px;
        }
        .login-button {
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 16px;
            font-weight: bold;
            padding: 10px 20px;
            background-color: #00ae99;
            color: white;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            text-decoration: none;
            width: 200px;
            height: 50px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .login-button:hover {
            background-color: #008f7a;
        }
        .login-button img {
            margin-right: 10px;
            width: 20px;
            height: 20px;
        }
        .habit-card, .model-card {
            background-color: #ddf4f2;
            border-radius: 16px;
            box-shadow: 0 6px 16px rgba(0,0,0,0.1);
            padding: 1.5rem;
            text-align: center;
            width: 100%;
            min-height: 270px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: transform 0.2s;
            margin: 10px 0 20px 0;
            box-sizing: border-box;
        }
        .habit-card:hover, .model-card:hover {
            transform: translateY(-5px);
        }
        .habit-title, .model-title {
            font-size: 20px;
            color: #00ae99;
            margin: 0.5rem 0;
            font-weight: 600;
        }
        .habit-desc, .model-desc {
            font-size: 14px;
            color: #333;
            flex-grow: 1;
            overflow: hidden;
            line-height: 1.4;
            margin: 0.5rem 0;
            text-align: center;
        }
        .heart-line-img {
            width: 60%;
            margin: 0.25rem auto;
        }
        .row-gap {
            margin-top: 60px;
        }
        .stButton > button {
            background-color: #197268;
            color: white;
            font-weight: bold;
            padding: 12px 24px;
            border-radius: 5px;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s ease;
            width: 100%;
        }
        .stButton > button:hover {
            background-color: #155d4e;
        }
        
        /* Ensure full-width containers */
        .main .block-container {
            max-width: 95%;
            padding-left: 2rem;
            padding-right: 2rem;
        }
        
        /* Model Card Styles - Updated for full width */
        .model-card {
            background-color: #ddf4f2;
            border-radius: 16px;
            box-shadow: 0 6px 16px rgba(0,0,0,0.1);
            padding: 1.5rem;
            text-align: center;
            min-height: 300px;
            width: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: transform 0.2s;
            margin-bottom: 20px;
            box-sizing: border-box;
        }


        .model-card:hover {
            transform: translateY(-5px);
        }

        .model-title {
            font-size: 20px;
            color: #00ae99;
            font-weight: 600;
            margin-bottom: 15px;
            line-height: 1.3;
        }

        .model-desc {
            font-size: 14px;
            color: #333;
            line-height: 1.5;
            flex-grow: 1;
            display: flex;
            align-items: center;
            text-align: center;
            justify-content: center;
        }
        
        /* Footer Container Grid */
        .footer-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            gap: 20px;
            margin-top: 40px;
        }

        /* Each Block */
        .footer-block {
            flex: 1 1 200px;
            min-width: 200px;
            background-color: #f9f9f9;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        .footer-block h3 {
            font-size: 20px;
            color: #2c3e50;
            margin-bottom: 0.5em;
            border-bottom: 2px solid #4CAF50;
            display: inline-block;
            padding-bottom: 0.2em;
        }
        
        /* Footer Links */
        .footer-link {
            display: block;
            margin: 0.5em 0;
            padding: 0.5em;
            border-radius: 8px;
            background-color: #e8f5e9;
            color: #2c3e50 !important;
            text-decoration: none;
            font-weight: 500;
            transition: all 0.2s ease;
        }

        .footer-link:hover {
            background-color: #c8e6c9;
            transform: scale(1.05);
            text-decoration: none;
            color: #000000 !important;
        }

        /* Social Icons */
        .footer-block a img {
            vertical-align: middle;
            margin-right: 8px;
        }

    </style>
""", unsafe_allow_html=True)


# ============ Header ============
col1, col2, col3 = st.columns([1, 3, 1])
with col1:
    logo = Image.open("mda.jpg")
    st.image(logo, width=180)
with col2:
    st.markdown(
        "<h1 style='text-align: center; font-weight: bold; font-size:50px; margin-top: 20px;'>"
        "MEDSCORE ASSIST</h1>",
        unsafe_allow_html=True
    )
with col3:
    if st.button("👤 Logout", key="logout"):
        st.switch_page(r"C:\Users\My pc\Dropbox\PC\Desktop\MP_authentication_21stMay_Final\pages\06_LogOut.py")
st.markdown("<br><br>", unsafe_allow_html=True)

# ============ Top Icons ============
def get_base64_img(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img_reports = get_base64_img("desktop.png")
img_contact = get_base64_img("safe.png")
img_book   = get_base64_img("doc.png")

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f"""
        <a href="/MyReports" class="footer-link">
            <img src="data:image/png;base64,{img_reports}" width="60"><br>
            <span style='font-weight:600; color:#007c74;'>View Reports Online</span>
        </a>
    """, unsafe_allow_html=True)
with c2:
    st.markdown(f"""
        <a href="/ContactUs" class="footer-link">
            <img src="data:image/png;base64,{img_contact}" width="60"><br>
            <span style='font-weight:600; color:#007c74;'>Contact Us</span>
        </a>
    """, unsafe_allow_html=True)
with c3:
    st.markdown(f"""
        <a href="/BookAppointment" class="footer-link">
            <img src="data:image/png;base64,{img_book}" width="60"><br>
            <span style='font-weight:600; color:#007c74;'>Book an Appointment</span>
        </a>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ============ Health Risk Prediction Models ============
st.markdown(
    '<h2 style="text-align: center; color: #00ae99; margin-bottom: 30px;">Health Risk Prediction Models</h2>',
    unsafe_allow_html=True
)

# Models data
models_data = [
    {
        "title": "Heart Disease Prediction",
        "description": "This model analyzes your medical history, cholesterol levels, blood pressure, and lifestyle habits to assess your risk of heart disease.",
        "page_name": "HeartModel"
    },
    {
        "title": "Hypertension Risk Prediction", 
        "description": "By examining factors like sodium intake, stress levels, and existing medical conditions, this model predicts your likelihood of developing hypertension.",
        "page_name": "HypertensionModel"
    },
    {
        "title": "Obesity Risk Prediction",
        "description": "Using BMI, dietary patterns, and physical activity, this model evaluates your risk of obesity and provides personalized advice.",
        "page_name": "ObesityModel"
    }
]

# Create three columns with equal spacing
col1, col2, col3 = st.columns([1, 1, 1], gap="large")
columns = [col1, col2, col3]

# Define the base directory
BASE_DIR = r"C:\Users\My pc\Dropbox\PC\Desktop\MP_authentication_21stMay_Final"

# Display each model in its column
for i, model in enumerate(models_data):
    with columns[i]:
        # Display the card
        st.markdown(f"""
            <div class="model-card">
                <div class="model-title">{model['title']}</div>
                <div class="model-desc">{model['description']}</div>
            </div>
        """, unsafe_allow_html=True)
        
        # Add the button with full width
        if st.button(f"View {model['title']}", key=f"model_btn_{i}", use_container_width=True):
            try:
                page_path = os.path.join(BASE_DIR, "pages", f"{model['page_name']}.py")
                st.switch_page(page_path)
            except Exception as e:
                st.error(f"Error navigating to {model['title']}: {str(e)}")

st.markdown("<br><br>", unsafe_allow_html=True)

# ============ Unhealthy Habits ============
st.markdown(
    '<h2 style="text-align: center; color: #00ae99;">Unhealthy Habits</h2>',
    unsafe_allow_html=True
)

habits = [
    {"title": "Alcoholism",     "desc": "Excessive alcohol can lead to liver damage, addiction, and accidents."},
    {"title": "Anger",          "desc": "Uncontrolled anger can cause emotional or physical harm."},
    {"title": "Poor Nutrition", "desc": "Low-nutrient diets can lead to chronic disease and weakness."},
    {"title": "Heartburn",      "desc": "A burning sensation from acid reflux, possibly due to GERD."},
    {"title": "Stress",         "desc": "Unmanaged stress affects both physical and mental health."},
    {"title": "Low Iron Diet",  "desc": "Lack of iron can cause anemia, fatigue, and reduced immunity."},
    {"title": "Zero Exercise",  "desc": "No activity leads to obesity, poor heart health, and low fitness."},
]

for i in range(0, len(habits), 3):
    row = habits[i : i + 3]
    cols = st.columns([1, 1, 1], gap="large")
    for habit, col in zip(row, cols):
        with col:
            st.markdown(f"""
                <div class="habit-card">
                    <img src="https://www.docopd.com/images/heart-line.png"
                         class="heart-line-img" alt="divider">
                    <div class="habit-title">{habit['title']}</div>
                    <div class="habit-desc">{habit['desc']}</div>
                </div>
            """, unsafe_allow_html=True)

# ============ Footer: Locations, Clients, Partners, Follow Us ============
st.markdown("""
<div class="footer-container">

  <div class="footer-block">
    <h3>📍 Locations</h3>
    <a href="https://www.google.com/maps/place/Bangalore" target="_blank" class="footer-link">Bangalore</a>
    <a href="https://www.google.com/maps/place/Chennai"   target="_blank" class="footer-link">Chennai</a>
    <a href="https://www.google.com/maps/place/Delhi"     target="_blank" class="footer-link">Delhi</a>
  </div>

  <div class="footer-block">
    <h3>🤝 Clients</h3>
    <a href="/clients_corporate" class="footer-link">Corporate</a>
    <a href="/clients_ngo"       class="footer-link">NGO</a>
    <a href="/clients_rwa"       class="footer-link">RWA</a>
  </div>

  <div class="footer-block">
    <h3>🏥 Partners</h3>
    <a href="/partners_hospitals" class="footer-link">Hospitals</a>
    <a href="/partners_chemists"  class="footer-link">Chemists</a>
    <a href="/partners_nurses"    class="footer-link">Nurses</a>
    <a href="/partners_doctors"   class="footer-link">Doctors</a>
  </div>

  <div class="footer-block">
    <h3>Follow us on</h3>
    <a href="https://www.instagram.com" target="_blank" class="footer-link">
      <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" width="20" style="vertical-align:middle;"> Instagram
    </a>
    <a href="https://www.linkedin.com/in/yourprofile" target="_blank" class="footer-link">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" width="20" style="vertical-align:middle;"> LinkedIn
    </a>
    <a href="https://twitter.com/yourprofile" target="_blank" class="footer-link">
      <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/x.svg" width="20" style="vertical-align:middle;"> X
    </a>
    <div style="margin-top:1rem; font-size:14px; color:#555;">
      &copy; 2025 Medscore Assist
    </div>
  </div>

</div>
""", unsafe_allow_html=True)