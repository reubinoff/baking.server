from datetime import UTC, datetime

import sqlalchemy as sa
from sqlmodel import DateTime, Field, SQLModel


def utcnow() -> datetime:
    return datetime.now(UTC)


class BaseBakingTable(SQLModel):
    pass


class AuditHistoryBaseTable(BaseBakingTable):
    created_at: datetime | None = Field(
        sa_type=DateTime(timezone=True),  # type: ignore[call-overload]
        index=True,
        default_factory=utcnow,
    )
    updated_at: datetime | None = Field(
        sa_type=DateTime(timezone=True),  # type: ignore[call-overload]
        index=True,
        default_factory=utcnow,
        sa_column_kwargs={"onupdate": sa.func.now()},
    )
    deleted_at: datetime | None = Field(
        sa_type=DateTime(timezone=True),  # type: ignore[call-overload]
        index=True,
        nullable=True,
    )

    __mapper_args__ = {"eager_defaults": True}
