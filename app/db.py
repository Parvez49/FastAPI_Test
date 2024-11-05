
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://myuser:mypassword@postgres:5432/mydb"  # Or use SQLite URL like 'sqlite:///./test.db'
# DATABASE_URL = "postgresql://myuser:mypassword@host.docker.internal:5435/mydb"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()