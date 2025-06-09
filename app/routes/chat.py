from fastapi import APIRouter
from app.schemas import ChatRequest, ChatResponse,TranslateRequest
from app.services.chat_service import get_response,get_translated_message

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    print("✅ Chat route hit!")
    print(f"📥 conversationId = {request.conversationId}")
    response = get_response(request.message,request.conversationId)
    return {"response": response}

@router.post("/translate",response_model=ChatResponse)
async def translate_text(request:TranslateRequest):
    response = get_translated_message(request.message,request.lang1,request.lang2)
    return {"response":response}