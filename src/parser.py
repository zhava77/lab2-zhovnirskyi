"""Input parsing module — converts raw data to Event objects."""

import json
from src.event import Event


def parse_json(raw: str) -> Event:
    """Parse JSON string into an Event."""
    if not raw or not raw.strip():
        raise ValueError("Input string is empty")
    data = json.loads(raw)
    if not isinstance(data, dict):
        raise ValueError("JSON root must be an object")
    event_type = data.get("type", "unknown")
    payload = data.get("payload", {})
    return Event(event_type, payload)


def parse_csv_line(line: str) -> Event:
    """Parse a simple CSV line 'type,key=value,...' into an Event."""
    if not line or not line.strip():
        raise ValueError("CSV line is empty")
    parts = line.strip().split(",")
    event_type = parts[0]
    payload = {}
    for part in parts[1:]:
        if "=" in part:
            k, v = part.split("=", 1)
            payload[k.strip()] = v.strip()
    return Event(event_type, payload)
