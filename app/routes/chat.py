from fastapi import Depends, APIRouter
from pydantic import BaseModel
from ai.initialize import ai_platform
from auth.apiAuth import get_user_identifier
from auth.throttle import apply_rate_limit

router = APIRouter()

# Pydantic Models
class ChatRequest(BaseModel):
  prompt: str

class ChatResponse(BaseModel):
  response: str

# API Endpoints
@router.post('/chat', response_model=ChatResponse)
async def chat(request: ChatRequest, user_id: str = Depends(get_user_identifier)):
  apply_rate_limit(user_id)
  response_text = ai_platform.chat(request.prompt)
  return ChatResponse(response=response_text)

@router.get('/')
async def root():
  return {'message': 'API is running!'}