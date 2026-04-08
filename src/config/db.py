from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base     
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv  

load_dotenv()  # Load environment variables from .env file

DATABASE_URL = os.getenv("POSTGRESQL_DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 
Base = declarative_base()  # Base class for our models

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

