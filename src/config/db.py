import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import text

# Load env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL is not set")

# Auto-fix for async
if DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace(
        "postgresql://", "postgresql+asyncpg://", 1
    )

# Async Engine
engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    connect_args={
        "ssl": "require",
        "statement_cache_size": 0
    }
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