from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.chat import router

app = FastAPI()
app.include_router(router)

origins = ["http://localhost:3000"]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

if __name__ == '__main__': #execute only in if statement
  import uvicorn #web server
  uvicorn.run('main:app', host='127.0.0.1', port=8080, reload=True)
