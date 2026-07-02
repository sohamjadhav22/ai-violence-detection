from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.incident import Incident
from app.api.auth import get_current_user
from app.schemas.incident import IncidentCreate, IncidentResponse

router = APIRouter()


@router.post("", response_model=IncidentResponse, status_code=201)
def create_incident(incident: IncidentCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)) -> Incident:
    db_incident = Incident(**incident.model_dump())
    db.add(db_incident)
    db.commit()
    db.refresh(db_incident)
    return db_incident


@router.get("", response_model=list[IncidentResponse])
def list_incidents(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
    camera_id: int | None = Query(default=None),
) -> list[Incident]:
    query = db.query(Incident)
    if camera_id is not None:
        query = query.filter(Incident.camera_id == camera_id)
    return query.order_by(Incident.timestamp.desc()).all()


@router.get("/{incident_id}", response_model=IncidentResponse)
def get_incident(incident_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)) -> Incident:
    incident = db.query(Incident).filter(Incident.id == incident_id).first()
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    return incident
