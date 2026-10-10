from __future__ import annotations

from fastapi import FastAPI

app = FastAPI(title="FactoryPulse Copilot Service")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/chat")
def chat() -> dict[str, str]:
    return {"response": "FactoryPulse copilot is ready."}
