from uuid import UUID, uuid4

import attrs

from model_service.domain.entities.core.entity import Entity


@attrs.define(kw_only=True)
class TableDataset(Entity):
    id: UUID = attrs.field(factory=uuid4)
    user: str = attrs.field()
    file_key: str = attrs.field()
    label_column: str = attrs.field()
