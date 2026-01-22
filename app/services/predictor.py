import pandas as pd
from app.models.ml_model import model
from app.config import BEST_THRESHOLD

def predict_stroke(features: dict):
    df = pd.DataFrame([features])

    proba = model.predict_proba(df)[:, 1][0]
    prediction = 1 if proba >= BEST_THRESHOLD else 0

    risk_label = "HIGH stroke risk" if prediction else "LOW stroke risk"

    return {
        "stroke_probability": round(float(proba), 4),
        "threshold": BEST_THRESHOLD,
        "prediction": prediction,
        "risk_label": risk_label
    }
