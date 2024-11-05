# FastAPI
    Initial package
    pip install fastapi uvicorn

### Run FastAPI
    uvicorn main:app --reload
    uvicorn main:app --reload --log-level debug   // with debug

### Uvicorn
    Purpose: Built to serve ASGI applications, which support asynchronous programming.

### API Documentation(FastAPI Default):
    Swagger UI: http://127.0.0.1:8000/docs
    ReDoc: http://127.0.0.1:8000/redoc

## alembic: database migration tool
    alembic init alembic
    alembic revision --autogenerate -m "Description of changes"  // create a new migration
    alembic upgrade head       // Apply the migrations

