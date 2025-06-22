import os
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.language_models import BaseChatModel

# Load environment variables
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# 🔹 Custom LLM using OpenRouter
class OpenRouterChat(BaseChatModel):
    def _generate(self, messages, **kwargs):
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        }

        chat_messages = [{"role": msg.type, "content": msg.content} for msg in messages]

        payload = {
            "model": "mistralai/mistral-7b-instruct",
            "messages": chat_messages,
        }

        response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=payload, headers=headers)
        response.raise_for_status()
        content = response.json()["choices"][0]["message"]["content"]

        return type("LLMResult", (), {"generations": [[type("Generation", (), {"text": content})()]]})()

    @property
    def _llm_type(self) -> str:
        return "openrouter-chat"

# 🔹 Load prebuilt vector DB
embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectordb = Chroma(persist_directory="db", embedding_function=embedding)

# 🔹 Initialize FastAPI
app = FastAPI()
llm = OpenRouterChat()

# 🔹 Request schema
class ChatRequest(BaseModel):
    query: str

# 🔹 Chat endpoint
@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        retriever = vectordb.as_retriever(search_type="similarity", search_kwargs={"k": 5})
        docs = retriever.get_relevant_documents(request.query)
        context = "\n".join([doc.page_content for doc in docs])

        messages = [
            SystemMessage(content=f"You are Vincent Bot. Use the context below to answer:\n{context}"),
            HumanMessage(content=request.query)
        ]

        response = llm._generate(messages)
        return {"response": response.generations[0][0].text.strip()}

    except Exception as e:
        return {"error": str(e)}
