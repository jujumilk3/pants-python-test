from datetime import datetime, timezone


def utcnow():
    return datetime.utcnow().replace(tzinfo=timezone.utc)


def common_util():
    return "This is imported from common.utils"
