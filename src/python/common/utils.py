from datetime import datetime, timezone


def utcnow():
    return datetime.utcnow().replace(tzinfo=timezone.utc)
