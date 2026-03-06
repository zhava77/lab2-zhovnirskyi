"""Input parsing module — converts raw data to Event objects."""

import json
from src.event import Event


def parse_json(raw: str) -> Event:
    """Parse JSON string into an Event."""
    data = json.loads(raw)
    event_type = data.get("type", "unknown")
    payload = data.get("payload", {})
    return Event(event_type, payload)


def parse_csv_line(line: str) -> Event:
    """Parse a simple CSV line 'type,key=value,...' into an Event."""
    parts = line.strip().split(",")
    event_type = parts[0]
    payload = {}
    for part in parts[1:]:
        if "=" in part:
            k, v = part.split("=", 1)
            payload[k.strip()] = v.strip()
    return Event(event_type, payload)