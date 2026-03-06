"""Event model and registry."""


class Event:
    """Represents a single event."""

    def __init__(self, event_type: str, payload: dict | None = None):
        self.event_type = event_type
        self.payload = payload or {}

    def __repr__(self):
        return f"Event(type={self.event_type}, payload={self.payload})"


class EventBus:
    """Central hub that dispatches events to registered handlers."""

    def __init__(self):
        self._handlers: dict[str, list] = {}

    def subscribe(self, event_type: str, handler):
        self._handlers.setdefault(event_type, []).append(handler)

    def publish(self, event: Event):
        for handler in self._handlers.get(event.event_type, []):
            handler(event)

    def clear(self):
        self._handlers.clear()