from fastapi import APIRouter
from pydantic import BaseModel
from services.ollama_llm import generate_response

router = APIRouter()

class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(payload: ChatRequest):
    return {
        "response": generate_response(payload.message)
    }