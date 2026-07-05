class ValidationError(Exception):
    """Raised when delivery data is invalid."""
    pass


def validate_delivery(record):

    required_fields = [
        "distance_km",
        "active_orders",
        "weather",
        "pickup_hour"
    ]

    for field in required_fields:
        if field not in record:
            raise ValidationError(f"Missing required field: {field}")

    if record["distance_km"] < 0:
        raise ValidationError("Distance cannot be negative.")

    if not 0 <= record["pickup_hour"] <= 23:
        raise ValidationError("Pickup hour must be between 0 and 23.")

    if not record["weather"].strip():
        raise ValidationError("Weather cannot be empty.")

    return True