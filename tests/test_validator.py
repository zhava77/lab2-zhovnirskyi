"""Unit tests for the validator module."""

import sys
import os

from src.event import Event
from src.validator import validate, validate_event_type, validate_payload

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


def test_valid_event():
    event = Event("user_login", {"user_id": "123"})
    errors = validate(event)
    assert errors == [], f"Expected no errors, got {errors}"


def test_invalid_event_type():
    event = Event("unknown_type", {"key": "value"})
    errors = validate(event)
    assert len(errors) == 1
    assert "Unknown event type" in errors[0]


def test_empty_payload():
    event = Event("user_login", {})
    errors = validate(event)
    assert len(errors) == 1
    assert "non-empty dict" in errors[0]


def test_validate_event_type_true():
    event = Event("purchase", {"item": "book"})
    assert validate_event_type(event) is True


def test_validate_payload_true():
    event = Event("info", {"msg": "hello"})
    assert validate_payload(event) is True
