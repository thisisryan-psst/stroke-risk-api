from fastapi import APIRouter
from app.schemas.request_models import UserReply
from app.utils.conversation import (
    questions, conversation_memory, get_next_question, save_user_reply, reset_conversation
)
from app.services.extractor import extract_features

router = APIRouter()

@router.get("/question")
def next_question():
    q = get_next_question()
    
    if q is None:
        return {"message": "All questions completed"}
    
    return {"question": q}


@router.post("/reply")
def user_reply(data: UserReply):
    save_user_reply(data.reply)
    return {"status": "reply saved"}


@router.get("/extract")
def extract():
    return extract_features()


@router.post("/reset")
def reset():
    reset_conversation()
    return {"status": "conversation reset"}