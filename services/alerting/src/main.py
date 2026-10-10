from __future__ import annotations

from typing import Any

from fastapi import FastAPI

app = FastAPI(title="FactoryPulse Alerting Service")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/alert")
def alert(payload: dict[str, Any]) -> dict[str, Any]:
    return {
        "status": "created",
        "alert": payload,
        "severity": payload.get("severity", "medium"),
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8003)
