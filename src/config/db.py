import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import text

# Load env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Async Engine
engine = create_async_engine(
    DATABASE_URL,
    echo=False,  # turn off in production
    pool_size=10,
    max_overflow=20
)

# Session
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base
Base = declarative_base()


# Dependency
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


# Connect test
async def connect_db():
    try:
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))
        print("✅ DATABASE CONNECTED SUCCESSFULLY")
    except Exception as e:
        print("❌ DATABASE CONNECTION FAILED")
        print(e)


# Close
async def close_db():
    await engine.dispose()