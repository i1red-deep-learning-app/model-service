import attrs

from model_service.domain.entities.core.entity import entity, BaseEntity
from model_service.domain.entities.core.generated import Generated


@entity
@attrs.define
class TableDataset(BaseEntity):
    id: Generated[str] = attrs.field()
    user: str = attrs.field()
    file_key: str = attrs.field()
    label_column: str = attrs.field()
