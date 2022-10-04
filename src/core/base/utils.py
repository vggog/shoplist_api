from datetime import datetime


def get_current_date():
    """
    return current date and time in utc
    """
    return datetime.utcnow()
