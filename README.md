# Violence Detection System

A production-ready foundation for a real-time violence detection platform built for CCTV surveillance. The system combines computer vision, deep learning, a FastAPI backend, a React dashboard, PostgreSQL, Redis, WebSockets, and Docker-based deployment.

## Features
- JWT authentication and role-based access
- Multiple camera support with RTSP/USB/IP camera configuration
- Human detection with YOLOv8
- Violence detection workflow with alert generation
- Incident storage with image/video artifacts
- Live dashboard for monitoring and incident history
- WebSocket live alerts and background task handling

## Tech Stack
- Backend: FastAPI, SQLAlchemy, PostgreSQL, Redis, Celery, WebSockets
- AI: YOLOv8, PyTorch, OpenCV
- Frontend: React, Vite, Tailwind CSS, Axios
- Deployment: Docker, Docker Compose

## Project Structure
- backend/app: API, auth, database models, services, AI modules
- frontend/src: dashboard UI and frontend components
- datasets: training data location
- trained_models: saved model weights
- docker/: deployment resources

## Quick Start
### Backend
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r backend/requirements.txt
uvicorn app.main:app --reload --app-dir backend
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### Docker Compose
```bash
docker compose up --build
```

## API Docs
Once the backend is running, Swagger documentation is available at:
- http://localhost:8000/docs

## Notes
- The current AI module is a functional scaffold and should be replaced with a trained CNN+LSTM or 3D CNN model using the RWF-2000 or RLVS dataset for production-grade accuracy.
- The system is designed as a strong foundation for enterprise surveillance and monitoring workflows.
