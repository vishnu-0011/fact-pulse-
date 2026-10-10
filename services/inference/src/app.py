from __future__ import annotations

from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel


class PredictionRequest(BaseModel):
    machine_id: str
    features: dict[str, float]


app = FastAPI(title="FactoryPulse Inference Service")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/predict")
def predict(payload: PredictionRequest) -> dict[str, Any]:
    score = round(sum(payload.features.values()) / max(len(payload.features), 1), 3)
    return {
        "machine_id": payload.machine_id,
        "anomaly_score": score,
        "status": "normal" if score < 75 else "attention",
    }
