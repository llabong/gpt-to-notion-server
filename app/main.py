# app/main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health_check():
    return {"message": "pong"}