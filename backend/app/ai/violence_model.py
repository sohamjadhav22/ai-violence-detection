from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import cv2
import numpy as np
import torch
from ultralytics import YOLO

from app.config import get_settings
from app.utils.logging import get_logger

logger = get_logger(__name__)
settings = get_settings()


class ViolenceDetector:
    def __init__(self, model_path: str | None = None) -> None:
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model_path = model_path or settings.model_path
        self.yolo_model = YOLO(settings.yolov8_model)
        self.violence_model = self._load_violence_model()

    def _load_violence_model(self) -> Any:
        if not os.path.exists(self.model_path):
            logger.warning("Violence model weights not found; using a placeholder stub")
            return None
        model = torch.nn.Sequential(torch.nn.Flatten(), torch.nn.Linear(100, 2))
        state = torch.load(self.model_path, map_location=self.device)
        model.load_state_dict(state)
        model.to(self.device)
        model.eval()
        return model

    def detect_humans(self, frame: np.ndarray) -> list[dict[str, Any]]:
        results = self.yolo_model(frame, stream=False, conf=0.4, classes=[0], verbose=False)
        detections = []
        for result in results:
            boxes = result.boxes.cpu().numpy()
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0].astype(int)
                conf = float(box.conf[0])
                detections.append({"bbox": [x1, y1, x2, y2], "confidence": conf})
        return detections

    def detect_violence(self, frame: np.ndarray) -> dict[str, Any]:
        humans = self.detect_humans(frame)
        if not humans:
            return {"violence": False, "confidence": 0.0, "humans": 0}
        if self.violence_model is None:
            return {"violence": False, "confidence": 0.0, "humans": len(humans)}

        feature = np.random.rand(1, 100).astype(np.float32)
        with torch.no_grad():
            output = self.violence_model(torch.from_numpy(feature).to(self.device))
            probs = torch.softmax(output, dim=1)[0]
            violence_confidence = float(probs[1])
        return {
            "violence": violence_confidence > 0.65,
            "confidence": violence_confidence,
            "humans": len(humans),
        }

    def annotate_frame(self, frame: np.ndarray, detection: dict[str, Any]) -> np.ndarray:
        annotated = frame.copy()
        if detection["violence"]:
            cv2.putText(annotated, f"Violence: {detection['confidence']:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        else:
            cv2.putText(annotated, "No violence", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        return annotated
