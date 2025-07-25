from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()  # .env 파일 자동 로딩

class Settings(BaseSettings):
    PROJECT_NAME: str = "GPT to Notion API"
    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
