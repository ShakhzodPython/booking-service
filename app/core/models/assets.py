from .base import Base
from mixins import CreatedAtMixin, PlaceRelationMixin


class PlaceServiceImage(Base, CreatedAtMixin):
    pass


class PlaceImage(
    Base,
    CreatedAtMixin,
    PlaceRelationMixin,
):
    pass

