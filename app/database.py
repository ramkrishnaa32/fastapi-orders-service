from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
import urllib.parse

load_dotenv()
username = os.getenv("DB_USERNAME")
password = urllib.parse.quote(os.getenv("DB_PASSWORD"))
db_name =  os.getenv("DB_NAME")
DATABASE_URL = f"postgresql://{username}:{password}@localhost:5432/{db_name}"
print("URL: ", DATABASE_URL)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()