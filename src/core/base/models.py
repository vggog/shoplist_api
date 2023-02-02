import sqlalchemy as sa
from sqlalchemy.orm import as_declarative

from src.core.utils import get_current_datetime


@as_declarative()
class BaseModel:
    id = sa.Column(
        sa.Integer,
        primary_key=True,
    )
    created_at = sa.Column(
        sa.DateTime,
        default=get_current_datetime(),
    )
    updated_at = sa.Column(
        sa.DateTime,
        default=get_current_datetime(),
        onupdate=get_current_datetime(),
    )
