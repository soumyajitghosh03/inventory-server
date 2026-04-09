from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.config.db import connect_db, close_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 🔥 Startup
    print("⏳ Connecting to database...")
    await connect_db()   # <-- this prints success message
    print("🚀 Application started")

    yield

    # 🔌 Shutdown
    print("⏳ Closing database connection...")
    await close_db()
    print("🛑 Application stopped")


app = FastAPI(lifespan=lifespan)


# Optional test route
@app.get("/")
async def root():
    return {"message": "API is running"}