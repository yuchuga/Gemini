import logging

logging.basicConfig(
  level=logging.INFO, # Default
  format='%(asctime)s [%(levelname)s] %(message)s', # Timestamp, log level, message
  handlers=[
    logging.StreamHandler(), # Console output
    logging.FileHandler('ai-models.log', encoding='utf-8') # File output
  ]
)

logger = logging.getLogger(__name__)