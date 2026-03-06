"""Event model and registry (refactored)."""

from datetime import datetime, timezone


class Event:
    """Represents a single event with timestamp."""

    def __init__(self, event_type: str, payload: dict | None = None):
        self.event_type = event_type
        self.payload = payload or {}
        self.timestamp = datetime.now(timezone.utc)

    def __repr__(self):
        return (
            f"Event(type={self.event_type}, "
            f"payload={self.payload}, "
            f"ts={self.timestamp.isoformat()})"
        )


class EventBus:
    """Central hub that dispatches events to registered handlers."""

    def __init__(self):
        self._handlers: dict[str, list] = {}
        self._history: list[Event] = []

    def subscribe(self, event_type: str, handler):
        self._handlers.setdefault(event_type, []).append(handler)

    def unsubscribe(self, event_type: str, handler):
        handlers = self._handlers.get(event_type, [])
        if handler in handlers:
            handlers.remove(handler)

    def publish(self, event: Event):
        self._history.append(event)
        for handler in self._handlers.get(event.event_type, []):
            handler(event)

    def get_history(self) -> list[Event]:
        return list(self._history)

    def clear(self):
        self._handlers.clear()
        self._history.clear()