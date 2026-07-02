from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.database.session import Base


class Camera(Base):
    __tablename__ = "cameras"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    stream_url = Column(String(500), nullable=False)
    camera_type = Column(String(50), default="rtsp")
    is_active = Column(Boolean, default=True)
    location = Column(String(255), default="")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
