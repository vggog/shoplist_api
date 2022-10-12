import sqlalchemy as sa
from sqlalchemy.orm import as_declarative

from src.core.base.utils import get_current_date


@as_declarative()
class BaseModel:
    id = sa.Column(
        sa.Integer,
        primary_key=True,
    )
    created_at = sa.Column(
        sa.DateTime,
        default=get_current_date(),
    )
    updated_at = sa.Column(
        sa.DateTime,
        default=get_current_date(),
        onupdate=get_current_date(),
    )
