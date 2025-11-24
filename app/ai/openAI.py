from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv() 

llm = ChatOpenAI(model='gpt-5-mini') # read by default OPEN_API_KEY
def chat_openai(prompt: str) -> str:
  response = llm.invoke(prompt)
  return response.content