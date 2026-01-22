SYSTEM_PROMPT = """
You are a conversational medical assistant.
Ask ONE clear medical question at a time.
Do not infer values.
Do not summarize.
"""

conversation_memory = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

questions = [
    "What is your age in years?",
    "What is your Body Mass Index (BMI)?",
    "What is your average glucose level (mg/dL)?",
    "Do you have hypertension? (yes or no)",
    "Do you have heart disease? (yes or no)",
    "What is your gender? (Male, Female, or Other)",
    "Have you ever been married? (Yes or No)",
    "What is your work type? (Private, Govt_job, Self-employed, children, or Never_worked)",
    "Do you live in an Urban or Rural area?",
    "What is your smoking status? (never smoked, formerly smoked, smokes, or Unknown)"
]

question_index = 0

# ---------------- HELPER FUNCTIONS ----------------

def get_next_question():
    global question_index

    if question_index >= len(questions):
        return None

    question = questions[question_index]
    question_index += 1

    conversation_memory.append(
        {"role": "assistant", "content": question}
    )

    return question


def save_user_reply(reply: str):
    conversation_memory.append(
        {"role": "user", "content": reply}
    )


def get_conversation():
    return conversation_memory


def reset_conversation():
    """
    Clears conversation and restarts from first question.
    """
    global conversation_memory, question_index

    conversation_memory.clear()
    conversation_memory.append(
        {"role": "system", "content": SYSTEM_PROMPT}
    )

    question_index = 0