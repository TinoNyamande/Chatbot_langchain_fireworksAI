from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage,SystemMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START,StateGraph,MessagesState
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
import app.config  

model = init_chat_model(
    "accounts/fireworks/models/llama-v3p1-70b-instruct",
    model_provider="fireworks"
)

workflow = StateGraph(state_schema=MessagesState)
prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer everything in a detailed , proffessional way"
        ),
        MessagesPlaceholder(variable_name="messages")
    ]
)

def call_model(state:MessagesState):
    prompt = prompt_template.invoke(state["messages"])
    response = model.invoke(prompt)
    return {"messages":response}

workflow.add_edge(START,"model")
workflow.add_node("model",call_model)

memory = MemorySaver()

app = workflow.compile(checkpointer=memory)

def get_response(message: str,conversationId:str) -> str:
    print("✅ Chat service hit!")
    print(f"📥 conversationId = {conversationId}")    
    config = {"configurable":{"thread_id":conversationId}}
    input_messages = HumanMessage(message)
    output = app.invoke({"messages":input_messages},config)
    return output["messages"][-1].content

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