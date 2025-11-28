from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv() 

llm = ChatOpenAI(model='gpt-5-mini', api_key=os.getenv('OPEN_API_KEY')) # read by default OPEN_API_KEY
def chat_openai(prompt: str) -> str:
  response = llm.invoke(prompt)
  return response.content