import uuid

from enum import Enum

from sqlalchemy import String, Enum as SqlEnum, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import TimeStampMixin, SoftDeleteMixin


# str mixin allows storing values as strings
class PlaceType(str, Enum):
    HOTEL = "Hotel"
    TOUR = "Tour"
    APARTMENT = "Apartment"
    COTTAGE = "Cottage"


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

    location_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("place_locations.id", ondelete="CASCADE"), unique=True
    )

    place_type: Mapped[PlaceType] = mapped_column(
        SqlEnum(PlaceType, name="place_type_enum"),
    )

    location: Mapped["PlaceLocation"] = relationship(
        back_populates="place",
        # this means only one location per place
        uselist=False,
        # If a related child object is no longer associated with a parent,
        # it will be automatically deleted from the database
        cascade="all, delete-orphan",
    )
