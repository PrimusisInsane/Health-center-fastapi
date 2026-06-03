from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    APP_NAME = os.getenv("APP_NAME", "FastAPI App")
    DEBUG = os.getenv("DEBUG", "True") == "True"

settings = Settings()