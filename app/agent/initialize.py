import os
from dotenv import load_dotenv
from pathlib import Path
from .gemini import Gemini
from excep.logger import logger

load_dotenv() 

def load_system_prompt(file_path: str='app/prompt/system-prompt.md') -> str:
  path = Path(file_path)  
  if not path.is_file():
    logger.error('System prompt file not found!')
    return ''
  
  try:
    with path.open('r', encoding='utf-8') as f:
      return f.read()
  except Exception as e:
    logger.exception(f'Error reading file: {e}')
    return ''
 
system_prompt = load_system_prompt() 
gemini_api_key = os.getenv('GEMINI_API_KEY')
# print('api_key', gemini_api_key)

if not gemini_api_key:
  logger.critical('No GEMINI_API_KEY provided!') # Stop program
  raise ValueError('No GEMINI_API_KEY provided!')

ai_platform = Gemini(api_key=gemini_api_key, system_prompt=system_prompt)
logger.info('Gemini AI platform initialized successfully!')