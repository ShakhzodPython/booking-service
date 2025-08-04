import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import (
    PlaceRelationMixin,
    TimeStampMixin,
    SoftDeleteMixin,
)

if TYPE_CHECKING:
    from .place import PlaceService, Place


class PlaceServiceAssociation(
    Base,
    TimeStampMixin,
    PlaceRelationMixin,
    SoftDeleteMixin,
):

    # association between PlaceServiceAssociation -> Place
    _place_id_unique = True
    _place_back_populates = "place_associations"

    place_service_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("place_services.id"),
        unique=True,
    )

    # association between PlaceServiceAssociation -> PlaceService
    place_service: Mapped["PlaceService"] = relationship(
        back_populates="place_service_associations",
    )
