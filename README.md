# Run App
uv run app/main.py

# Test API Endpoint
curl -X POST "http://127.0.0.1:8080/chat
  -H "Content-Type: "application/json"
  -H "Authorization: Bearer xxxx"
  -d '{"prompt": "payload"}'