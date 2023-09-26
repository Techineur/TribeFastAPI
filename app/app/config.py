from functools import lru_cache
from pydantic import BaseSettings
from dotenv import load_dotenv
from starlette.config import Config

load_dotenv()

class Settings(BaseSettings):
    redis_url: str = 'redis://redis:6379'
    title : str = 'Tribe Mobile Controller'
    ALGORITHM: str = "ES512"
    DB_URL: str
    PUBLIC_ES_KEY: str 
    PRIVATE_ES_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60


    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'



@lru_cache()
def get_config():
    return Settings()

config = get_config()


