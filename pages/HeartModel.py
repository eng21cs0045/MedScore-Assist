# pages/03HeartModel.py
import streamlit as st
import numpy as np
from utils.predictions import load_model, predict_score
from utils.preprocessing import load_scaler_heart
from pages.generate_report import generate_report
#from streamlit_extras.stx_cookie_manager.stx_cookie_manager import CookieManager

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
    </style>
    """,
    unsafe_allow_html=True)


# Ensure user is logged in
if 'user' not in st.session_state:
    st.warning("Please log in to view this page.")
    st.stop()


user_email = st.session_state["user"]["email"]

user_email = st.session_state["user"]["email"]
def run_heart_disease_prediction():
    if 'user' not in st.session_state:
        st.warning("Please log in to view this page.")
        st.stop()
# Setup session state for navigation
if 'heart_form_page' not in st.session_state:
    st.session_state.heart_form_page = "non_tech"

st.title("Heart Disease Prediction")

if st.session_state.heart_form_page == "non_tech":
    st.header("Enter Your Non-Technical Parameters")

    age = st.number_input("Age (20 - 120)", min_value=20, max_value=120, key="age")
    gender_options = {0: "Male", 1: "Female"}
    gender = st.selectbox("Gender", options=list(gender_options.keys()), format_func=lambda x: gender_options[x], key="gender")

    weight = st.number_input("Weight (kg)", min_value=20.0, max_value=300.0, key="weight")
    height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, key="height")
    bmi = round(weight / ((height / 100) ** 2), 1)
    st.session_state.bmi = bmi
    st.write(f"**Calculated BMI**: {bmi}")

    smoking_options = {0: "Never", 1: "Occasional", 2: "Regular", 3: "Heavy", 4: "Chain-Smoker"}
    alcohol_options = {0: "None", 1: "Social", 2: "Moderate", 3: "Frequent", 4: "Alcoholic"}
    physical_activity_options = {1: "Low", 2: "Medium", 3: "High"}
    diet_options = {0: "High Sodium", 1: "Low Potassium", 2: "Balanced", 3: "Other"}
    stress_options = {0: "Low", 1: "Medium", 2: "High", 3: "Very High"}
    family_history_options = {0: "No", 1: "Yes"}
    work_env_options = {0: "Active", 1: "Sedentary"}

    st.selectbox("Smoking Status", list(smoking_options.keys()), format_func=lambda x: smoking_options[x], key="smoking")
    st.selectbox("Alcohol Consumption", list(alcohol_options.keys()), format_func=lambda x: alcohol_options[x], key="alcohol")
    st.selectbox("Physical Activity Level", list(physical_activity_options.keys()), format_func=lambda x: physical_activity_options[x], key="physical_activity")
    st.selectbox("Diet Type", list(diet_options.keys()), format_func=lambda x: diet_options[x], key="diet_type")
    st.selectbox("Stress Levels", list(stress_options.keys()), format_func=lambda x: stress_options[x], key="stress_levels")
    st.selectbox("Family History of Heart Risk", list(family_history_options.keys()), format_func=lambda x: family_history_options[x], key="family_history")
    st.selectbox("Work Environment", list(work_env_options.keys()), format_func=lambda x: work_env_options[x], key="work_env")

    # Navigation Buttons
    col1, col2 = st.columns([0.8, 1.2])
    if col1.button("⬅️ Back to Home"):
        st.switch_page(r"pages/02LandingPage.py")
    if col2.button("Next ➡️"):
        st.session_state.heart_form_page = "tech"
        st.rerun()

elif st.session_state.heart_form_page == "tech":
    st.header("Enter Your Technical Parameters")
    col1, col2, _ = st.columns([1.5, 1.5, 1]) 
    total_chol = st.number_input("Total Cholesterol (mg/dL)", 100.0, 500.0)
    ldl_chol = st.number_input("LDL Cholesterol (mg/dL)", 25.0, 250.0)
    hdl_chol = st.number_input("HDL Cholesterol (mg/dL)", 20.0, 120.0)
    triglycerides = st.number_input("Triglycerides (mg/dL)", 20.0, 550.0)
    systolic_bp = st.number_input("Systolic BP (mmHg)", 50.0, 300.0)
    diastolic_bp = st.number_input("Diastolic BP (mmHg)", 30.0, 150.0)
    hs_crp = st.number_input("hs-CRP (mg/L)", 0.0, 10.0)
    fasting_sugar = st.number_input("Fasting Blood Sugar (mg/dL)", 40.0, 200.0)

    col1, col2,col3 = st.columns(3)
    if col1.button("⬅️ Back"):
        st.session_state.heart_form_page = "non_tech"
        st.rerun()

    if col2.button("Calculate Heart Score"):
        # Collect all inputs
        feature_columns = [
            "Total_Cholesterol", "LDL_Cholesterol", "HDL_Cholesterol", "Triglycerides",
            "Systolic_BP", "Diastolic_BP", "hs_CRP", "Fasting_Blood_Sugar",
            "Age", "Gender", "BMI", "Smoking_Status", "Alcohol_Consumption",
            "Physical_Activity_Level", "Diet_Type", "Stress_Levels", "Family_History",
            "Work_Environment"
        ]

        row = [
            total_chol, ldl_chol, hdl_chol, triglycerides, systolic_bp, diastolic_bp, hs_crp, fasting_sugar,
            st.session_state.age, st.session_state.gender, st.session_state.bmi,
            st.session_state.smoking, st.session_state.alcohol, st.session_state.physical_activity,
            st.session_state.diet_type, st.session_state.stress_levels,
            st.session_state.family_history, st.session_state.work_env
        ]

        X_input = np.array(row).reshape(1, -1)
        model = load_model(r"Models/heart_v2.pkl")
        scaler = load_scaler_heart()
        final_score = predict_score(model, scaler, X_input)
    
        # Feedback
        if final_score >= 85:
            category = "Excellent: Keep up the good work!"
        elif 70 <= final_score < 85:
            category = "Good: Maintain your current lifestyle."
        elif 55 <= final_score < 70:
            category = "Fair: Some improvements are needed."
        elif 50 <= final_score < 55:
            category = "Poor: Need to focus on many things..."
        else:
            category = "Very Poor: Please consult a healthcare professional."

        st.success(f"**Heart Health Score**: {final_score:.2f}")
        st.info(category)

        # Concerning checks
        concerning = []
        if st.session_state.smoking == 4:
            concerning.append("Smoking Status")
        if st.session_state.stress_levels == 3:
            concerning.append("High Stress Levels")
        if systolic_bp > 140 or diastolic_bp > 90:
            concerning.append("High Blood Pressure")
        if st.session_state.bmi < 18.5 or st.session_state.bmi > 24.9:
            concerning.append("BMI Outside Normal Range")
        if total_chol > 200:
            concerning.append("High Total Cholesterol")
        if ldl_chol > 130:
            concerning.append("High LDL Cholesterol")
        if hdl_chol < 40:
            concerning.append("Low HDL Cholesterol")
        if triglycerides > 150:
            concerning.append("High Triglycerides")
        if hs_crp > 3:
            concerning.append("High hs-CRP")
        if fasting_sugar > 126:
            concerning.append("High Fasting Blood Sugar")

        if concerning:
            st.warning(f"Concerning parameters: {', '.join(concerning)}")
        else:
            st.write("No major concerning inputs identified at this time.")
    
        # Report generation
        params = {
            "Age": st.session_state.age, "Gender": st.session_state.gender, "BMI": st.session_state.bmi,
            "Total Cholesterol": total_chol, "LDL Cholesterol": ldl_chol, "HDL Cholesterol": hdl_chol,
            "Triglycerides": triglycerides, "Systolic BP": systolic_bp, "Diastolic BP": diastolic_bp,
            "hs-CRP": hs_crp, "Fasting Blood Sugar": fasting_sugar
        }
    
        generate_report(user_email, "Heart Model", params, final_score, concerning)
    if col3.button("View My Reports"):
            st.switch_page(r"pages/MyReports.py")

# Prevent accidental reruns when not needed
if __name__ == "__main__":
    st.stop()
