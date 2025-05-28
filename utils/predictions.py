import joblib
import xgboost as xgb
import numpy as np
from sklearn.preprocessing import StandardScaler  # if needed

def load_model(model_path):
    """
    Generic function to load a joblib model from the given path.
    """
    return joblib.load(model_path)

def predict_score(model, scaler, input_array):
    """
    1) Scale the input using the provided scaler (if available)
    2) Convert to XGBoost DMatrix
    3) Predict using the model
    4) Return the numeric score
    """
    if scaler is not None:
        X_scaled = scaler.transform(input_array)
    else:
        # If no scaler, pass through
        X_scaled = input_array

    dmatrix = xgb.DMatrix(X_scaled)
    prediction = model.predict(dmatrix)[0]
    return float(prediction)  # Ensure a regular float
