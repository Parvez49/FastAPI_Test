
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas import order_schemas
from app.routers import order_routers
from .crud import order_crud
from .db import SessionLocal


app = FastAPI(
    title="My FastAPI App",
    description="This is a sample FastAPI application.",
    version="0.1.0",
)

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


app.include_router(order_routers.router, prefix="/orders", tags=["Orders"])

