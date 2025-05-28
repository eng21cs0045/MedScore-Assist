import streamlit as st
from PIL import Image

# Set wide layout
st.set_page_config(layout="wide")

# Custom CSS to remove Streamlit padding and style client boxes
st.markdown("""
    <style>
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
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 3, 1])
with col1:
    logo = Image.open("mda.jpg")
    st.image(logo, width=180)
with col2:
    st.markdown("<h1 style='text-align: center; font-weight: bold;'>MEDSCORE ASSIST</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>🏢 Corporate Clients</h2>", unsafe_allow_html=True)

# Intro
st.markdown("""
<div style="text-align: center; font-size: 30px; margin-bottom: 40px;">
    Welcome to our Corporate Client hub. Medscore Assist proudly partners with leading organizations to promote preventive healthcare at workplaces.
</div>
""", unsafe_allow_html=True)

# Collaborations Header
st.markdown("<h3 style='color: #00ae99;'>Our Collaborations Include:</h3>", unsafe_allow_html=True)

# Define client data
clients = [
    {
        "name": "🚀 HealthFirst Inc.",
        "address": "123 Wellness St, Health City",
        "phone": "+1-800-123-4567",
        "desc": "Leads in workplace wellness checkups and preventive diagnostics."
    },
    {
        "name": "🏢 Wellbeing Dynamics Ltd.",
        "address": "45 Harmony Ave, Fitville",
        "phone": "+1-800-234-5678",
        "desc": "Specializes in employee mental health and fitness programs."
    },
    {
        "name": "🚀 Lifetech Corporates",
        "address": "789 Vitality Blvd, Lifetown",
        "phone": "+1-800-345-6789",
        "desc": "Provides cutting-edge AI health trackers for corporates."
    },
    {
        "name": "💼 Zenith Analytics",
        "address": "321 Insight Loop, Data City",
        "phone": "+1-800-456-7890",
        "desc": "Delivers predictive analytics for organizational health trends."
    },
    {
        "name": "📋 SmartHealth Group",
        "address": "99 Prevention Road, Caretopia",
        "phone": "+1-800-567-8901",
        "desc": "Experts in health scoring and chronic condition prevention."
    },
    {
        "name": "💡 VitalEdge Solutions",
        "address": "67 Boost Lane, Energize Bay",
        "phone": "+1-800-678-9012",
        "desc": "Focuses on nutritional programs and corporate vitality."
    }
]

# Render clients in rows of 3 using columns
for i in range(0, len(clients), 3):
    cols = st.columns(3)
    for col, client in zip(cols, clients[i:i+3]):
        col.markdown(f"""
        <div style='background-color: #f1fdfc; padding: 20px; border-radius: 10px; height: 280px;'>
            <h4 style='font-size: 24px;'>{client['name']}</h4>
            <p style='font-size: 20px;'>📍 {client['address']}</p>
            <p style='font-size: 20px;'>📞 {client['phone']}</p>
            <p style='font-size: 18px;'>{client['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

# Optional footer to fill page
st.markdown("""
    <br><br>
    <div style='background-color: #e0f7f4; padding: 30px; border-radius: 10px; text-align: center;'>
        <h4 style='color: #00796b;'>Partner with Medscore Assist</h4>
        <p style='font-size: 18px;'>Enhance your organization’s wellness strategy with AI-powered solutions and personalized assessments.</p>
        <p style='font-size: 18px;'>📧 contact@medscoreassist.com | 📞 +1-800-999-9999</p>
    </div>
""", unsafe_allow_html=True)
