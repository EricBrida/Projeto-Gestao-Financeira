from fastapi import FastAPI, Depends
from app import models
from app.database import engine, Base, SessionLocal
from app.routes import auth

app = FastAPI(
    title="Projeto Gestão Financeira API"
)
Base.metadata.create_all(bind=engine)

app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "API Ok!!"}