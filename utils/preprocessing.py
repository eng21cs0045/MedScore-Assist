import joblib
import os

def load_scaler_heart():
    """
    Load the scaler used for Heart Model.
    In practice, you would have saved a fitted StandardScaler 
    as a .pkl file from your training code.
    """
    # Demo approach: We assume the scaler might be named "heart_scaler.pkl"
    scaler_path = os.path.join("Results_Detector","Models","heart_scaler.pkl")
    if os.path.exists(scaler_path):
        return joblib.load(scaler_path)
    else:
        # If you do not actually have a separate scaler file, handle accordingly
        # e.g., raise an exception or just return None
        return None

def load_scaler_hypertension():
    """
    Load the scaler for Hypertension Model.
    """
    scaler_path = os.path.join("Results_Detector","Models","hypertension_scaler.pkl")
    if os.path.exists(scaler_path):
        return joblib.load(scaler_path)
    else:
        return None

def load_scaler_obesity():
    """
    Load the scaler for Obesity Model.
    """
    scaler_path = os.path.join("Results_Detector","Models","obesity_scaler.pkl")
    if os.path.exists(scaler_path):
        return joblib.load(scaler_path)
    else:
        return None
