from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.camera import Camera
from app.api.auth import get_current_user
from app.schemas.camera import CameraCreate, CameraResponse

router = APIRouter()


@router.post("", response_model=CameraResponse, status_code=201)
def create_camera(camera: CameraCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)) -> Camera:
    db_camera = Camera(**camera.model_dump())
    db.add(db_camera)
    db.commit()
    db.refresh(db_camera)
    return db_camera


@router.get("", response_model=list[CameraResponse])
def list_cameras(db: Session = Depends(get_db), current_user=Depends(get_current_user)) -> list[Camera]:
    return db.query(Camera).all()


@router.get("/{camera_id}", response_model=CameraResponse)
def get_camera(camera_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)) -> Camera:
    camera = db.query(Camera).filter(Camera.id == camera_id).first()
    if not camera:
        raise HTTPException(status_code=404, detail="Camera not found")
    return camera
