from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage,SystemMessage
import app.config  

model = init_chat_model(
    "accounts/fireworks/models/llama-v3p1-70b-instruct",
    model_provider="fireworks"
)

def get_response(message: str) -> str:
    return model.invoke([HumanMessage(content=message)]).content

def get_translated_message(message:str,lang1:str, lang2:str)->str:
    system_prompt = (
        f"You are a translation engine. "
        f"Translate the following text from {lang1} to {lang2}. "
        f"Do not add any commentary or explanation. "
        f"Just return the translated sentence only."
    )
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=message)
    ]
    response = model.invoke(messages)
    return response.content