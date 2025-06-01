from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
import app.config  

model = init_chat_model(
    "accounts/fireworks/models/llama-v3p1-70b-instruct",
    model_provider="fireworks"
)

def get_response(message: str) -> str:
    return model.invoke([HumanMessage(content=message)]).content