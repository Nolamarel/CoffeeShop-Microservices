from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, field_validator


from uuid import UUID
from datetime import datetime, timezone
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field, field_validator


class Review(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    order_id: UUID
    customer_id: UUID
    rating: int = Field(ge=1, le=5)
    comment: Optional[str] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    # Автоматически ставим время при создании через репозиторий
    @field_validator("created_at", mode="before")
    @classmethod
    def _set_created_at(cls, v):
        if v is None:
            return datetime.now(timezone.utc)
        return v



