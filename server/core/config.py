from pydantic_settings import BaseSettings
from pydantic import Field
from functools import lru_cache


class Settings(BaseSettings):
    """
    Application configuration using environment variables
    """

    # App info
    APP_NAME: str = "AI Resume Analyzer"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # API settings
    API_PREFIX: str = "/api"

    # File upload
    MAX_FILE_SIZE_MB: int = 5
    ALLOWED_EXTENSIONS: list = Field(default=["txt", "pdf"])

    # CORS
    ALLOWED_ORIGINS: list = Field(default=["*"])

    # AI Settings (future use)
    OPENAI_API_KEY: str | None = Field(default=None)
    GEMINI_API_KEY: str | None = Field(default=None)

    class Config:
        env_file = ".env"
        case_sensitive = True


# Singleton settings object
@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()