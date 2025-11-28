from fastapi import Depends, APIRouter
from pydantic import BaseModel
from agent.initialize import ai_platform
from agent.groq import chat_groq
from auth.apiAuth import get_user_identifier
from auth.throttle import apply_rate_limit

router = APIRouter()

# Pydantic Models
class ChatRequest(BaseModel):
  prompt: str

class ChatResponse(BaseModel):
  response: str

# API Endpoints
@router.post('/chat-groq', response_model=ChatResponse)
def ask_llm(request: ChatRequest):
  response = chat_groq(request.prompt)
  AIMessage = response["messages"][1].content
  return ChatResponse(response=AIMessage)

@router.post('/chat-gemini', response_model=ChatResponse)
async def chat(request: ChatRequest, user_id: str = Depends(get_user_identifier)):
  apply_rate_limit(user_id)
  response = ai_platform.chat(request.prompt)
  return ChatResponse(response=response)

@router.get('/')
async def root():
  return {'message': 'API is running!'}