from fastapi import FastAPI
from app.database import engine, Base
from app.routes import router

app = FastAPI()

# Create Database Tables
Base.metadata.create_all(bind=engine)

# Include Routes
app.include_router(router)
