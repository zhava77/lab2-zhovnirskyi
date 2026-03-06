"""Validation module for events."""

ALLOWED_TYPES = {"user_login", "user_logout", "purchase", "error", "info"}


def validate_event_type(event) -> bool:
    """Check that event type is in the allowed list."""
    return event.event_type in ALLOWED_TYPES


def validate_payload(event) -> bool:
    """Check that payload is a non-empty dict."""
    return isinstance(event.payload, dict) and len(event.payload) > 0


def validate(event) -> list[str]:
    """Return list of validation errors (empty = valid)."""
    errors = []
    if not validate_event_type(event):
        errors.append(f"Unknown event type: {event.event_type}")
    if not validate_payload(event):
        errors.append("Payload must be a non-empty dict")
    return errors
