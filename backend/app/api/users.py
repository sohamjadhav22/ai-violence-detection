from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.user import User
from app.api.auth import get_current_user, require_admin
from app.schemas.auth import UserResponse

router = APIRouter()


@router.get("", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db), current_user: User = Depends(require_admin)) -> list[User]:
    return db.query(User).all()
