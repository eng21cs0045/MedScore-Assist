# pages/05ObesityModel.py
import streamlit as st
import numpy as np
from utils.predictions import load_model, predict_score
from utils.preprocessing import load_scaler_obesity
from pages.generate_report import generate_report

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
def run_obesity_risk_prediction():
    st.write("Running the Obesity Risk Prediction model...")
    # Your prediction model code goes here
    st.write("Prediction: Obesity Risk Level")
# Setup session state for navigation
if 'obesity_form_page' not in st.session_state:
    st.session_state.obesity_form_page = "non_tech"

st.title("Obesity Risk Prediction")

if st.session_state.obesity_form_page == "non_tech":
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
    stress_options = {0: "Low", 1: "Medium", 2: "High", 3: "Very High"}
    work_env_options = {0: "Active", 1: "Sedentary"}

    st.selectbox("Smoking Status", list(smoking_options.keys()), format_func=lambda x: smoking_options[x], key="smoking")
    st.selectbox("Alcohol Consumption", list(alcohol_options.keys()), format_func=lambda x: alcohol_options[x], key="alcohol")
    st.selectbox("Stress Levels", list(stress_options.keys()), format_func=lambda x: stress_options[x], key="stress_levels")
    st.selectbox("Work Environment", list(work_env_options.keys()), format_func=lambda x: work_env_options[x], key="work_env")

    col1, col2 = st.columns([0.8, 1.2])
    if col1.button("⬅️ Back to Home"):
        st.switch_page(r"C:\Users\My pc\Dropbox\PC\Desktop\MP_authentication_21stMay_Final\pages\02LandingPage.py")
    if col2.button("Next ➡️"):
        st.session_state.obesity_form_page = "tech"
        st.rerun()

elif st.session_state.obesity_form_page == "tech":
    st.header("Enter Your Technical Parameters")
    systolic_bp = st.number_input("Systolic BP (mmHg)", 50.0, 300.0)
    diastolic_bp = st.number_input("Diastolic BP (mmHg)", 30.0, 150.0)
    sodium = st.number_input("Serum Sodium (mEq/L)", 100.0, 160.0)
    potassium = st.number_input("Serum Potassium (mEq/L)", 2.0, 7.0)
    urea = st.number_input("Blood Urea (mg/dL)", 5.0, 100.0)
    creatinine = st.number_input("Serum Creatinine (mg/dL)", 0.4, 5.0)

    col1, col2 ,col3= st.columns(3)
    if col1.button("⬅️ Back"):
        st.session_state.obesity_form_page = "non_tech"
        st.rerun()

    if col2.button("Calculate Obesity Risk"):
        feature_columns = [
            "Systolic_BP", "Diastolic_BP", "Sodium", "Potassium",
            "Urea", "Creatinine", "Age", "Gender", "BMI",
            "Smoking_Status", "Alcohol_Consumption", "Stress_Levels", "Work_Environment"
        ]

        row = [
            systolic_bp, diastolic_bp, sodium, potassium, urea, creatinine,
            st.session_state.age, st.session_state.gender, st.session_state.bmi,
            st.session_state.smoking, st.session_state.alcohol, st.session_state.stress_levels,
            st.session_state.work_env
        ]

        X_input = np.array(row).reshape(1, -1)
        model = load_model(r"C:\Users\My pc\Dropbox\PC\Desktop\MP_authentication_21stMay_Final\Models\best_xgb_obesity_model_v2.pkl")
        scaler = load_scaler_obesity()
        final_score = predict_score(model, scaler, X_input)

        # Feedback
        if final_score >= 85:
            category = "Excellent: Your weight is well controlled."
        elif 70 <= final_score < 85:
            category = "Good: Monitor occasionally and maintain lifestyle."
        elif 55 <= final_score < 70:
            category = "Moderate Risk: Take preventive steps."
        elif 50 <= final_score < 55:
            category = "High Risk: Consult your physician."
        else:
            category = "Very High Risk: Immediate medical attention needed."

        st.success(f"**Obesity Risk Score**: {final_score:.2f}")
        st.info(category)

        concerning = []
        if st.session_state.smoking == 4:
            concerning.append("Smoking Status")
        if st.session_state.stress_levels == 3:
            concerning.append("High Stress")
        if systolic_bp > 140 or diastolic_bp > 90:
            concerning.append("High Blood Pressure")
        if st.session_state.bmi > 30:
            concerning.append("Obese BMI")
        if sodium < 135 or sodium > 145:
            concerning.append("Abnormal Sodium")
        if potassium < 3.5 or potassium > 5.0:
            concerning.append("Abnormal Potassium")
        if creatinine > 1.2:
            concerning.append("High Creatinine")

        if concerning:
            st.warning(f"Concerning Parameters: {', '.join(concerning)}")
        else:
            st.write("No critical abnormalities detected.")

        params = {
            "Age": st.session_state.age, "Gender": st.session_state.gender, "BMI": st.session_state.bmi,
            "Systolic BP": systolic_bp, "Diastolic BP": diastolic_bp,
            "Sodium": sodium, "Potassium": potassium, "Urea": urea, "Creatinine": creatinine
        }

        generate_report(user_email, "Obesity Model", params, final_score, concerning)
    if col3.button("View My Reports"):
        st.switch_page(r"C:\Users\My pc\Dropbox\PC\Desktop\MP_authentication_21stMay_Final\pages\MyReports.py")
# Prevent accidental reruns when run directly
if __name__ == "__main__":
    st.stop()
