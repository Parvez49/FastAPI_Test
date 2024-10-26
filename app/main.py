# main.py
from fastapi import FastAPI

app = FastAPI(
    title="My FastAPI App",
    description="This is a sample FastAPI application.",
    version="0.1.0",
)

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}
