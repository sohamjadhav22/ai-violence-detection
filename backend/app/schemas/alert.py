from pydantic import BaseModel


class AlertResponse(BaseModel):
    id: int
    incident_id: int
    alert_type: str
    message: str
    is_sent: bool

    class Config:
        from_attributes = True
