import sqlalchemy

from src.core.base.utils import get_current_date


class BaseModel:
    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
    )
    created_at = sqlalchemy.Column(
        sqlalchemy.DateTime,
        default=get_current_date(),
    )
    updated_at = sqlalchemy.Column(
        sqlalchemy.DateTime,
        default=get_current_date(),
        onupdate=get_current_date(),
    )
