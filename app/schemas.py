from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    conversationId:str

class ChatResponse(BaseModel):
    response: str

class TranslateRequest(BaseModel):
    message: str
    lang1: str
    lang2: str