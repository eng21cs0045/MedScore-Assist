
import os
import hashlib
from fpdf import FPDF
import streamlit as st

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

# Reports folder path
REPORTS_FOLDER = r"reports"
os.makedirs(REPORTS_FOLDER, exist_ok=True)


MEDSCORE_INFO = {
    "logo": r"mda.jpg",
    "email": "contact@medscore.com",
    "phone": "+91 8136092576",
    "address": "#45, Wellness Street, Bangalore-560045"
}

PARAMETER_UNITS = {
    "Heart Model": {
        "Age": "years",
        "BMI": "kg/m²",
        "Total Cholesterol": "mg/dL",
        "LDL Cholesterol": "mg/dL",
        "HDL Cholesterol": "mg/dL",
        "Triglycerides": "mg/dL",
        "Systolic BP": "mmHg",
        "Diastolic BP": "mmHg",
        "hs-CRP": "mg/L",
        "Fasting Blood Sugar": "mg/dL"
    },
    "Hypertension Model": {
        "Age": "years",
        "BMI": "kg/m²",
        "Systolic BP": "mmHg",
        "Diastolic BP": "mmHg",
        "Serum Sodium": "mmol/L",
        "Serum Potassium": "mmol/L",
        "Total Cholesterol": "mg/dL",
        "LDL Cholesterol": "mg/dL",
        "HDL Cholesterol": "mg/dL",
        "Blood Glucose": "mg/dL",
        "Creatinine": "mg/dL",
        "eGFR": "mL/min/1.73m²"
    },
    "Obesity Model": {
        "Age": "years",
        "BMI": "kg/m²",
        "Waist": "cm",
        "Hip": "cm",
        "Waist-to-Hip Ratio": "ratio",
        "Triglycerides": "mg/dL",
        "Fasting Blood Glucose": "mg/dL"
    }
}

def hash_parameters(params):
    """Generate a unique hash for the given parameters to avoid duplicate reports."""
    params_string = "_".join(str(v) for v in params)
    return hashlib.md5(params_string.encode()).hexdigest()

def generate_report(user_email, model_name, parameters, score, concerning_params):
    """Generates and saves a PDF health report without hashed parameters in the filename."""
    
    
    from datetime import datetime

    sanitized_email = user_email.split("@")[0]  
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  
    filename = f"{sanitized_email}{model_name}{current_time}.pdf"



    filepath = os.path.join(REPORTS_FOLDER, filename)

    
    if os.path.exists(filepath):
        return filepath


    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Medscore Logo and Info
    if os.path.exists(MEDSCORE_INFO["logo"]):
        pdf.image(MEDSCORE_INFO["logo"], 10, 8, 33)

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, "Medscore Assist - Health Report", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", "B", 10)
    pdf.cell(200, 10, f"Email: {MEDSCORE_INFO['email']} | Phone: {MEDSCORE_INFO['phone']}", ln=True, align="C")
    pdf.cell(200, 10, f"Address: {MEDSCORE_INFO['address']}", ln=True, align="C")
    pdf.ln(10)

    # User Information
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, f"User: {user_email}", ln=True, align="L")
    pdf.cell(200, 10, f"Model: {model_name}", ln=True, align="L")
    pdf.ln(5)

    # Entered Parameters with Units
    pdf.set_font("Arial", "B", 11)
    pdf.cell(200, 10, "Entered Parameters:", ln=True, align="L")
    pdf.set_font("Arial", size=10)

    # Get parameter units for the selected model
    units = PARAMETER_UNITS.get(model_name, {})

    # Convert gender numeric values to "Male" / "Female"
    if "Gender" in parameters:
        parameters["Gender"] = "Male" if parameters["Gender"] == 0 else "Female"

    for key, value in parameters.items():
        unit = units.get(key, "")
        pdf.cell(200, 10, f"{key}: {value} {unit}", ln=True, align="L")


    pdf.ln(5)

    # Health Score
    pdf.set_font("Arial", "B", 11)
    pdf.cell(200, 10, f"Health Score: {round(score,2)}", ln=True, align="L")
    pdf.ln(5)

    # Concerning Parameters
    pdf.set_font("Arial", "B", 11)
    pdf.cell(200, 10, "Concerning Parameters:", ln=True, align="L")
    pdf.set_font("Arial", size=10)

    if concerning_params:
        for param in concerning_params:
            pdf.cell(200, 10, f"- {param}", ln=True, align="L")
    else:
        pdf.cell(200, 10, "No concerning parameters detected.", ln=True, align="L")

    pdf.ln(10)

    pdf.output(filepath)
    return filepath
