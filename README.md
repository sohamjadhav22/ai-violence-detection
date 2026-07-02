# Violence Detection System using CCTV Surveillance

This project provides a production-ready foundation for a real-time violence detection platform using CCTV streams, YOLOv8 for person detection, a violence classifier, FastAPI for the backend, React/Vite for the frontend, PostgreSQL for persistence, Redis/Celery for background jobs, and Docker Compose for deployment.

## Architecture
- Backend: FastAPI, SQLAlchemy, JWT auth, WebSockets, Celery
- AI: YOLOv8 + PyTorch-based violence detection stub with training pipeline
- Frontend: React + Vite + Tailwind
- Infrastructure: PostgreSQL, Redis, Docker Compose

## Folder Structure
- backend/app: API, auth, models, services, AI modules
- frontend/src: React app
- datasets: training data location
- trained_models: model weights

## Run Locally
1. Create and activate a Python virtual environment.
2. Install backend dependencies:
   `pip install -r backend/requirements.txt`
3. Start PostgreSQL and Redis (or use Docker Compose).
4. Run the backend:
   `uvicorn app.main:app --reload --app-dir backend`
5. Install frontend dependencies:
   `cd frontend && npm install && npm run dev`

## Docker Compose
```bash
docker compose up --build
```

## Notes
- The provided AI model is a lightweight placeholder and should be replaced with a trained CNN+LSTM or 3D CNN model using the RWF-2000 or RLVS dataset for production.
- The API documentation is available at `/docs`.
