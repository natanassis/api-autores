import os
from dotenv import load_dotenv

load_dotenv(".flaskenv")

SECRET_KEY = os.getenv("SECRET_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")

#print(f"API Key: {API_KEY}")
#print(f"Database URL: {DATABASE_URL}")

class Config:
    api_key =SECRET_KEY
    database_url = DATABASE_URL