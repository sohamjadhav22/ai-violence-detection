from pydantic import BaseModel


class IncidentCreate(BaseModel):
    camera_id: int
    incident_type: str
    confidence: float = 0.0
    image_path: str | None = None
    video_path: str | None = None
    description: str = ""


class IncidentResponse(BaseModel):
    id: int
    camera_id: int
    incident_type: str
    confidence: float
    image_path: str | None
    video_path: str | None
    description: str

    class Config:
        from_attributes = True
