import requests

from langchain.agents import create_agent
from langchain.tools import tool
from dotenv import load_dotenv

load_dotenv() 

@tool('get_weather', description='Return weather information', return_direct=False)
def get_weather(city: str) -> dict:
  try: 
    url = f'https://wttr.in/{city}?format=j1'
    response = requests.get(url)
    return response.json()
  except Exception as e :
    return  { 'Error': str(e) }

llm = create_agent(
  model = 'groq:llama-3.1-8b-instant', 
  tools = [get_weather],
  system_prompt = 'You are a helpful chat assistant. Be clear, concise and polite. '
)

def chat_groq(prompt: str) -> str:
  response = llm.invoke({
    'messages': [
      {'role': 'user', 'content': prompt}
    ]
  })
  print(response)
  print(response['messages'][1].content) # AIMessage
  return response