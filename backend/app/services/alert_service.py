from pathlib import Path
from datetime import datetime
from sqlalchemy.orm import Session
from app.models.incident import Incident
from app.models.alert import Alert
from app.websocket.manager import manager
from app.utils.logging import get_logger

logger = get_logger(__name__)


class AlertService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_incident(self, camera_id: int, confidence: float, incident_type: str = "violent_activity") -> Incident:
        incident = Incident(
            camera_id=camera_id,
            incident_type=incident_type,
            confidence=confidence,
            description="Violence detected",
        )
        self.db.add(incident)
        self.db.commit()
        self.db.refresh(incident)
        self._create_alert(incident)
        return incident

    def _create_alert(self, incident: Incident) -> None:
        alert = Alert(incident_id=incident.id, alert_type="websocket", message=f"Violence detected for camera {incident.camera_id}")
        self.db.add(alert)
        self.db.commit()
        self.db.refresh(alert)
        logger.info("Alert created")

    async def broadcast_alert(self, message: str) -> None:
        await manager.broadcast(message)
