from __future__ import annotations

import json
import time
from typing import Any


def telemetry_payload(machine_id: str, tick: int) -> dict[str, Any]:
    return {
        "machine_id": machine_id,
        "timestamp": f"2026-10-10T00:{tick % 60:02d}:00Z",
        "temperature_c": 64.0 + (tick % 9) * 1.5,
        "vibration_mm_s": 2.5 + (tick % 5) * 0.3,
        "pressure_bar": 100.0 + (tick % 7) * 0.8,
        "status": "warning" if tick % 5 == 0 else "ok",
    }


def run() -> None:
    machines = ["M-101", "M-102", "M-103"]
    tick = 0

    while True:
        payload = {
            "source": "simulator",
            "event": "telemetry",
            "samples": [telemetry_payload(machine, tick + offset) for offset, machine in enumerate(machines)],
        }
        print(json.dumps(payload))
        time.sleep(2)
        tick += 1


if __name__ == "__main__":
    run()
