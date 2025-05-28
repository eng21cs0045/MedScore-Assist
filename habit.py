import streamlit as st
from PIL import Image
# CSS styles for the habit cards and model cards
st.markdown("""
    <style>
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
            max-width: 290px;
            height: 270px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: transform 0.2s;
            margin: auto;
        }
        .habit-card:hover, .model-card:hover {
            transform: translateY(-5px);
        }
        .habit-title, .model-title {
            font-size: 20px;
            color: #00ae99;
            margin: 0.5rem 0;
        }
        .habit-desc, .model-desc {
            font-size: 14px;
            color: #333;
            flex-grow: 1;
            overflow: hidden;
            line-height: 1.4;
            margin: 0.5rem 0;
        }
        .heart-line-img {
            width: 60%;
            margin: 0.25rem auto;
        }
        .row-gap {
            margin-top: 60px;
        }

        /* Button styling */
        .stButton > button {
            background-color: #197268; /* Set background color */
            color: white;              /* Set text color to white */
            font-weight: bold;         /* Make the text bold */
            padding: 12px 24px;        /* Add padding to the button */
            border-radius: 5px;        /* Rounded corners */
            border: none;              /* Remove border */
            cursor: pointer;          /* Pointer cursor on hover */
            transition: background-color 0.3s ease; /* Smooth transition for hover effect */
        }
        .stButton > button:hover {
            background-color: #155d4e; /* Darker shade of the button color on hover */
        }
    </style>
""", unsafe_allow_html=True)
col1, col2, col3 = st.columns([2, 4, 1])  # Adjust columns to center text
with col1:
        logo = Image.open("mda.jpg")  # Replace with actual path
        st.image(logo, width=180)
with col2:
        st.markdown("<h1 style='text-align: center; font-weight: bold;font-size:50px;margin-top: 20px;'> MEDSCORE ASSIST</h1>", unsafe_allow_html=True)
with col3:
    # Text-based button with an icon (using an emoji as an example)
        st.markdown('<a href="/LoginRegister" class="login-button"> 👤 Logout</a>', unsafe_allow_html=True) 
st.markdown("<br><br>", unsafe_allow_html=True) 
# --- Features section using Streamlit columns ---
col1, col2, col3 = st.columns(3)

with col1:
    st.image("safe.png", width=60)
    st.markdown("<p style='text-align:justify; color:#007c74; font-weight:600;'>100% Safe</p>", unsafe_allow_html=True)

with col2:
    st.image("desktop.png", width=60)
    st.markdown("<p style='text-align:justify; color:#007c74; font-weight:600;'>View Reports Online</p>", unsafe_allow_html=True)

with col3:
    st.image("doc.png", width=60)
    st.markdown("<p style='text-align:left; color:#007c74; font-weight:600;'>Best Doctor Consultation</p>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True) 
# --- Health Risk Prediction Models section ---
st.markdown('<h2 style="text-align: center; color: #00ae99;">Health Risk Prediction Models</h2>', unsafe_allow_html=True)

# Model data with links to respective models
models = {
    "Heart Disease Prediction": (
        "This model analyzes your medical history, cholesterol levels, blood pressure, and lifestyle habits to assess your risk of heart disease.",
        "HeartModel.py"
    ),
    "Hypertension Risk Prediction": (
        "By examining factors like sodium intake, stress levels, and existing medical conditions, this model predicts your likelihood of developing hypertension.",
        "HypertensionModel.py"
    ),
    "Obesity Risk Prediction": (
        "Using BMI, dietary patterns, and physical activity, this model evaluates your risk of obesity and provides personalized advice.",
        "ObesityModel.py"
    ),
}

# Show models as cards with a button outside the card
cols = st.columns(3)
for col, (title, (desc, link)) in zip(cols, models.items()):
    with col:
        st.markdown(f"""
            <div class="model-card">
                <div class="model-title">{title}</div>
                <div class="model-desc">{desc}</div>
            </div>
        """, unsafe_allow_html=True)  # Card content (without the button inside)

        # Button outside the card (that will open the respective model)
        if st.button(f"View {title} Model"):
            if title == "Heart Disease Prediction":
                # Call the renamed model script
                from pages.HeartModel import run_heart_disease_prediction
                # Updated import statement
                

            elif title == "Hypertension Risk Prediction":
                import HypertensionModel  # Updated import statement
                HypertensionModel.run_hypertension_risk_prediction()

            elif title == "Obesity Risk Prediction":
                import ObesityModel  # Updated import statement
                ObesityModel.run_obesity_risk_prediction()
st.markdown("<br><br>", unsafe_allow_html=True) 
# --- Unhealthy Habits section ---
st.markdown('<h2 style="text-align: center; color: #00ae99;">Unhealthy Habits</h2>', unsafe_allow_html=True)

habits = [
    {"title": "Alcoholism", "desc": "Excessive consumption of alcohol can lead to liver damage, addiction, and accidents."},
    {"title": "Anger", "desc": "Uncontrolled anger can cause emotional or physical harm to self or others."},
    {"title": "Poor Nutrition", "desc": "Low-nutrient diets can lead to malnutrition, chronic disease, and weakened immunity."},
    {"title": "Heartburn", "desc": "A burning sensation from acid reflux, possibly due to GERD."},
    {"title": "Stress", "desc": "Unmanaged stress may affect both physical and mental well-being."},
    {"title": "Low Iron Diet", "desc": "Lack of iron can cause anemia, fatigue, and reduced immunity."},
    {"title": "Zero Exercise", "desc": "No activity can lead to obesity, poor heart health, and reduced fitness."}
]

# Render rows of 3 unhealthy habit cards with spacing
for i in range(0, len(habits), 3):
    if i > 0:
        st.markdown('<div class="row-gap"></div>', unsafe_allow_html=True)
    cols = st.columns(3)
    for col, habit in zip(cols, habits[i:i+3]):
        with col:
            st.markdown(f"""
                <div class="habit-card">
                    <img src="https://www.docopd.com/images/heart-line.png" class="heart-line-img" alt="divider">
                    <div class="habit-title">{habit['title']}</div>
                    <div class="habit-desc">{habit['desc']}</div>
                </div>
            """, unsafe_allow_html=True)
