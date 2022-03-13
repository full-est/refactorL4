from fastapi import Depends, FastAPI, HTTPException, Request, Response
from sqlalchemy.orm import Session
from app.db.database import SessionLocal, engine
from app import models
from app.routers import users, auth

app = FastAPI(title="ExampleOfFastAPI")

# ROUTERS
app.include_router(auth.router, prefix="/auth")
app.include_router(users.router, prefix="/users")


@app.get("/")
def root():
    return { "status": "Running." }
