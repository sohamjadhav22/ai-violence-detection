# Violence Detection System

[![GitHub Repo stars](https://img.shields.io/github/stars/sohamjadhav22/ai-violence-detection?style=social)](https://github.com/sohamjadhav22/ai-violence-detection)
[![GitHub last commit](https://img.shields.io/github/last-commit/sohamjadhav22/ai-violence-detection)](https://github.com/sohamjadhav22/ai-violence-detection/commits/main)
[![Docker](https://img.shields.io/badge/Docker-ready-blue)]()
[![Python](https://img.shields.io/badge/Python-3.12-green)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-%2300C5FF.svg?style=for-the-badge&logo=fastapi&logoColor=white)]()
[![React](https://img.shields.io/badge/React-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)]()

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

## Architecture Overview
- Cameras feed live streams into the backend inference pipeline.
- YOLOv8 detects persons, while a violence classifier evaluates suspicious activity.
- Incidents are saved to the database, alerts are emitted through WebSockets, and the React dashboard displays live status.

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

## Demo / Usage
- Start the backend and frontend locally.
- Add one or more cameras through the API or the dashboard.
- Watch live incident detection and alerts appear in the dashboard.
- Use the `incidents` endpoint to review historical events and confidence details.

## Notes
- The current AI module is a functional scaffold and should be replaced with a trained CNN+LSTM or 3D CNN model using the RWF-2000 or RLVS dataset for production-grade accuracy.
- The system is designed as a strong foundation for enterprise surveillance and monitoring workflows.
