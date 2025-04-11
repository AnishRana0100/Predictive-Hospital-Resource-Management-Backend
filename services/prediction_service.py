import joblib
import numpy as np

# Load your pre-trained model
model = joblib.load("models/admission_forecast_model.pkl")

def predict_admissions(features: np.ndarray) -> int:
    prediction = model.predict(features)
    return int(prediction[0])

