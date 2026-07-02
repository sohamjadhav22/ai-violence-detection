from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.alert import Alert
from app.api.auth import get_current_user
from app.schemas.alert import AlertResponse

router = APIRouter()


@router.get("", response_model=list[AlertResponse])
def list_alerts(db: Session = Depends(get_db), current_user=Depends(get_current_user)) -> list[Alert]:
    return db.query(Alert).order_by(Alert.created_at.desc()).all()
