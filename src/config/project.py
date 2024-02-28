from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str
    VERSION: str
    DEBUG: bool
    SECRET_KEY: str
    CORS_ALLOWED_ORIGINS: str


settings = Settings()
