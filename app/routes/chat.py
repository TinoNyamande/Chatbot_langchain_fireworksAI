from fastapi import APIRouter
from app.schemas import ChatRequest, ChatResponse
from app.services.chat_service import get_response

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    response = get_response(request.message)
    return {"response": response}