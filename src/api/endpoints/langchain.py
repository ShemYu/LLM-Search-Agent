# endpoints/langchain.py

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from src.llm.langchain import chat, summarize

router = APIRouter()


class ChatRequest(BaseModel):
    prompt: str


class SummarizeRequest(BaseModel):
    text: str


@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    response = chat(request.prompt)
    return {"response": response}


@router.post("/summarize")
async def summarize_endpoint(request: SummarizeRequest):
    summary = summarize(request.text)
    return {"summary": summary}
