import uuid

from typing import TYPE_CHECKING

from sqlalchemy import String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import TimeStampMixin, SoftDeleteMixin


if TYPE_CHECKING:
    from .place_service_association import PlaceServiceAssociation

class PlaceType(
    Base,
    TimeStampMixin,
    SoftDeleteMixin,
):
    title: Mapped[str] = mapped_column(String(100), unique=True)

    places: Mapped[list["Place"]] = relationship(
        back_populates="place_type",
        cascade="all, delete",
        # This setting tells SQLAlchemy not to issue a SQL DELETE or UPDATE on child rows (e.g., Place),
        # when the parent (e.g., PlaceType) is deleted.
        passive_deletes=True,
    )


class PlaceLocation(
    Base,
    TimeStampMixin,
    SoftDeleteMixin,
):
    longitude: Mapped[float] = mapped_column(Float(precision=8))
    latitude: Mapped[float] = mapped_column(Float(precision=8))

    place: Mapped["Place"] = relationship(
        back_populates="location",
        # this means only one place per location
        uselist=False,
    )


class PlaceService(
    Base,
    TimeStampMixin,
    SoftDeleteMixin,
):
    title: Mapped[str] = mapped_column(String(100))

    place_service_associations: Mapped["PlaceServiceAssociation"] = relationship(
        back_populates="place_service"
    )


class PlaceDetail(
    Base,
    TimeStampMixin,
    SoftDeleteMixin,
):
    pass


class Place(
    Base,
    TimeStampMixin,
    SoftDeleteMixin,
):
    title: Mapped[str] = mapped_column(
        String(100),
        unique=True,
    )

    place_type_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("place_types.id", ondelete="CASCADE")
    )

    location_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("place_locations.id", ondelete="CASCADE"), unique=True
    )

    location: Mapped["PlaceLocation"] = relationship(
        back_populates="place",
        # this means only one location per place
        uselist=False,
        cascade="all, delete",
    )

    place_type: Mapped["PlaceType"] = relationship(
        back_populates="places",
    )

    place_associations: Mapped[list["PlaceServiceAssociation"]] = relationship(
        back_populates="place"
    )
