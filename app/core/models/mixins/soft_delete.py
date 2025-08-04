from sqlalchemy import Boolean
from sqlalchemy.orm import Mapped, mapped_column


class SoftDeleteMixin:
    is_deleted: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    def soft_delete(self):
        self.is_deleted = True