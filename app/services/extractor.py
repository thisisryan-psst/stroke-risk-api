import json
from app.services.groq_chat import ask_groq
from app.utils.conversation import conversation_memory

def extract_features():
    extract_prompt = """
    From the above conversation, extract the following medical features.
    Return ONLY valid JSON:

    {
      "age": number,
      "bmi": number,
      "avg_glucose_level": number,
      "hypertension": 0 or 1,
      "heart_disease": 0 or 1,
      "gender": "Male" | "Female" | "Other",
      "ever_married": "Yes" | "No",
      "work_type": "Private" | "Govt_job" | "Self-employed" | "children" | "Never_worked",
      "Residence_type": "Urban" | "Rural",
      "smoking_status": "never smoked" | "formerly smoked" | "smokes" | "Unknown"
    }
    """

    response = ask_groq(
        conversation_memory + [{"role": "user", "content": extract_prompt}]
    )

    return json.loads(response)
