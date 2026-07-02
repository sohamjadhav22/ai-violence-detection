from pydantic import BaseModel


class CameraCreate(BaseModel):
    name: str
    stream_url: str
    camera_type: str = "rtsp"
    is_active: bool = True
    location: str = ""


class CameraResponse(BaseModel):
    id: int
    name: str
    stream_url: str
    camera_type: str
    is_active: bool
    location: str

    class Config:
        from_attributes = True
