# Run App
uv run app/main.py

# Run Specific File
uv run app/agent/openAI.py

# Test API Endpoint
http://127.0.0.1:8080/chat-gemini 

curl -X POST "http://127.0.0.1:8080/chat \
  -H "Content-Type: "application/json" \
  -H "Authorization: Bearer xxxx" \
  -d '{"prompt": "payload"}' 