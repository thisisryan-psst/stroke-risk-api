from fastapi import APIRouter
from app.services.predictor import predict_stroke
from app.services.groq_chat import ask_groq
from app.config import BEST_THRESHOLD

router = APIRouter()


@router.post("/predict")
def predict(features: dict):
    return predict_stroke(features)


@router.post("/explain")
def explain(features: dict):
    # First, get prediction safely
    result = predict_stroke(features)

    # 🛑 GUARD: prediction not ready or failed
    if "error" in result:
        return {
            "explanation": "Prediction is not available yet. Please complete all questions first."
        }

    risk_label = result["risk_label"]
    stroke_probability = result["stroke_probability"]

    prompt = f"""
    A stroke prediction model produced the following:

    Risk label: {risk_label}
    Stroke probability: {stroke_probability}
    Threshold: {BEST_THRESHOLD}

    Patient data:
    {features}

    Explain the result in simple medical language
    and give appropriate health advice.
    """

    explanation = ask_groq(
        [{"role": "user", "content": prompt}]
    )

    return {"explanation": explanation}
