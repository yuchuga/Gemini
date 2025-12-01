import requests

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langchain.tools import tool
from pydantic import BaseModel

load_dotenv() 

class OutputSchema(BaseModel):
  response: str

@tool('get_weather', description='Return weather information', return_direct=False)
def get_weather(city: str) -> dict:
  """Get weather for a city"""
  try: 
    url = f'https://wttr.in/{city}?format=j1'
    response = requests.get(url)
    return response.json()
  except Exception as e :
    return  { 'Error': str(e) }

agent = create_agent(
  model='groq:llama-3.1-8b-instant',
  tools=[get_weather],
  system_prompt='You are a helpful chat assistant. Be clear, concise and polite.',
  response_format=ToolStrategy(OutputSchema)
)

def chat_groq(prompt: str) -> str:
  response = agent.invoke({
    'messages': [
      {'role': 'user', 'content': prompt}
    ]
  })
  print(response)
  print(response['messages'][1].content) # AIMessage
  return response