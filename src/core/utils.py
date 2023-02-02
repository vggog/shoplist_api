import random
from datetime import datetime


def get_current_datetime():
    return datetime.utcnow()


def generate_one_time_code():
    return random.randint(100_000, 999_999)
