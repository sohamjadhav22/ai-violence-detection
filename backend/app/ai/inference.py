import cv2
import numpy as np
from app.ai.violence_model import ViolenceDetector


def run_live_inference(stream_url: str) -> None:
    detector = ViolenceDetector()
    cap = cv2.VideoCapture(stream_url)
    if not cap.isOpened():
        raise RuntimeError("Unable to open video stream")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        detection = detector.detect_violence(frame)
        annotated = detector.annotate_frame(frame, detection)
        cv2.imshow("Violence Detection", annotated)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
