from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Findna"
    VERSION: str = "1.0.0"
    DEBUG: bool = True
    ALLOWED_HOSTS: list = ["http://localhost:3000"]

    # Database
    DATABASE_URL: str = "postgresql://findna_user:findna_pass@localhost:5432/findna"

    # External APIs (placeholder for now)
    NEWS_API_KEY: str = ""

    class Config:
        env_file = ".env"


_settings = None


def get_settings() -> Settings:
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings
