from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    app_name: str = "Violence Detection System"
    database_url: str = "postgresql://postgres:postgres@db:5432/violence_db"
    redis_url: str = "redis://redis:6379/0"
    secret_key: str = "super-secret-key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60 * 24
    upload_dir: str = "/app/media"
    model_path: str = "/app/trained_models/violence_model.pt"
    yolov8_model: str = "yolov8n.pt"

    class Config:
        env_file = ".env"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    return Settings()
