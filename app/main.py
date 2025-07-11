# app/main.py
from fastapi import FastAPI

app = FastAPI(title="CRM Distribuidora")

@app.get("/")
def root():
    return {"message": "Bienvenido al CRM Distribuidora"}
