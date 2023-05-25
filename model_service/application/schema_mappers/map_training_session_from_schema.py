from model_service.application.schemas.training_session_schema import TrainingSessionSchema
from model_service.domain.entities.training.loss_function_type import LossFunctionType
from model_service.domain.entities.training.metric_type import MetricType
from model_service.domain.entities.training.training_session import TrainingSession
from model_service.domain.entities.value_objects.optimizer import Optimizer
from model_service.application.shared.execution_context import ExecutionContext
from model_service.shared.dependency_management.dependency_kind import SCOPED
from model_service.shared.dependency_management.provide import Dependency, provide


@provide
def map_training_session_from_schema(
    schema: TrainingSessionSchema, execution_context: ExecutionContext = Dependency(SCOPED)
) -> TrainingSession:
    optimizer = Optimizer(type=schema.optimizer.type, params=schema.optimizer.params)
    loss_function = LossFunctionType(schema.loss_function)
    metrics = [MetricType[metric] for metric in schema.metrics]
    return TrainingSession.create(
        user=execution_context.user,
        network_id=schema.network_id,
        dataset_id=schema.dataset_id,
        optimizer=optimizer,
        loss_function=loss_function,
        metrics=metrics,
        epochs=schema.epochs,
        batch_size=schema.batch_size,
        validation_split=schema.validation_split,
    )
