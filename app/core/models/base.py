import uuid
import inflect

from sqlalchemy import MetaData, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import (
    DeclarativeBase,
    declared_attr,
    Mapped,
    mapped_column,
)

from core.config import settings
from utils import camel_case_to_snake_case

p = inflect.engine()

class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    )

    metadata = MetaData(
        naming_convention=settings.db.naming_conventions,
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        table_name = camel_case_to_snake_case(cls.__name__)
        return p.plural(table_name)
