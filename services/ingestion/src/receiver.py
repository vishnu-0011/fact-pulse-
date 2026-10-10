from __future__ import annotations

import json
import time
from typing import Any


def handle_message(payload: dict[str, Any]) -> dict[str, Any]:
    records = payload.get("samples", [])
    return {
        "accepted": True,
        "event": payload.get("event", "telemetry"),
        "record_count": len(records),
        "status": "ingested",
    }


def run() -> None:
    tick = 0
    while True:
        message = {
            "event": "telemetry",
            "samples": [{
                "machine_id": f"M-{101 + (tick % 3)}",
                "temperature_c": 65 + (tick % 10),
                "timestamp": f"2026-10-10T00:{tick % 60:02d}:00Z",
            }],
        }
        print(json.dumps(handle_message(message)))
        time.sleep(3)
        tick += 1


if __name__ == "__main__":
    run()
