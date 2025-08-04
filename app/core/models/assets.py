from .base import Base
from mixins import (
    CreatedAtMixin,
    PlaceRelationMixin,
    SoftDeleteMixin,
)


class PlaceServiceImage(
    Base,
    CreatedAtMixin,
    SoftDeleteMixin,
):
    pass


class PlaceImage(
    Base,
    CreatedAtMixin,
    PlaceRelationMixin,
    SoftDeleteMixin,
):
    pass
