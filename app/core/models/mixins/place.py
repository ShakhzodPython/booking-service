import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from core.models import Place


class PlaceRelationMixin:
    _place_id_nullable: bool = False
    _place_back_populates: str | None = None

    @declared_attr
    def place_id(cls) -> Mapped[uuid.UUID]:
        return mapped_column(
            ForeignKey("places.id"),
            nullable=cls._place_id_nullable,
        )

    @declared_attr
    def place(cls) -> Mapped["Place"]:
        return relationship(
            "Place",
            back_populates=cls._place_back_populates,
        )
