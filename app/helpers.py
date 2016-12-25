from uuid import uuid4
import arrow


def generate_sid():
    return str(uuid4())


def get_utc():
    _utc = arrow.utcnow()
    return str(_utc.timestamp)

