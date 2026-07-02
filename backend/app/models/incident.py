from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database.session import Base


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    camera_id = Column(Integer, ForeignKey("cameras.id"), nullable=False)
    incident_type = Column(String(100), nullable=False)
    confidence = Column(Float, default=0.0)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    image_path = Column(String(500), nullable=True)
    video_path = Column(String(500), nullable=True)
    description = Column(String(500), default="")
