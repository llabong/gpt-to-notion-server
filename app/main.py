# app/main.py

from fastapi import FastAPI
from app.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

@app.get("/")
def health_check():
    return {"message": "pong"}
