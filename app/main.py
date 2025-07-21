# app/main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to SIES-TES FastAPI!"}

@app.get("/hello")
def say_hello():
    return {"message": "Hello student!"}