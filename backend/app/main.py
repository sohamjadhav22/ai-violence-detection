from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth, cameras, incidents, alerts, users, health
from app.database.session import Base, engine
from app.models import user, camera, incident, alert, log
from app.websocket.manager import manager
from app.utils.logging import get_logger

logger = get_logger(__name__)

app = FastAPI(
    title="Violence Detection System",
    version="1.0.0",
    description="Real-time violence detection for CCTV surveillance",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/api/health", tags=["health"])
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(cameras.router, prefix="/api/cameras", tags=["cameras"])
app.include_router(incidents.router, prefix="/api/incidents", tags=["incidents"])
app.include_router(alerts.router, prefix="/api/alerts", tags=["alerts"])

Base.metadata.create_all(bind=engine)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Violence Detection System API"}


@app.on_event("shutdown")
def shutdown_event() -> None:
    logger.info("Shutting down application")
