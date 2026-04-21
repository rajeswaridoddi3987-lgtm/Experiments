from langgraph.graph import StateGraph, START, END
import os
from langchain_core.messages import SystemMessage, HumanMessage, BaseMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langgraph.graph import MessagesState
from langchain_core.language_models.chat_models import BaseChatModel

load_dotenv()
project = os.getenv('GOOGLE_CLOUD_PROJECT')

def get_llm(model: str = "gemini-2.5-flash"):
    return ChatGoogleGenerativeAI(
        model=model,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

