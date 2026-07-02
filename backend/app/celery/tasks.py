from celery import Celery
from app.config import get_settings

settings = get_settings()
celery_app = Celery("violence_detection", broker=settings.redis_url, backend=settings.redis_url)


@celery_app.task
def process_video_clip(video_path: str) -> str:
    return f"Processed {video_path}"
