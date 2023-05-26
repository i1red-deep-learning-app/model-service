from bson import ObjectId

from model_service.domain.entities.core.generated import GENERATED_VALUE
from model_service.domain.entities.training.training_session import TrainingSession
from model_service.domain.entities.value_objects.optimizer import Optimizer
from model_service.infrastructure.mongo.mappers.abstract_mongo_mapper import AbstractMongoMapper
from model_service.infrastructure.mongo.models.training.optimizer_model import OptimizerModel
from model_service.infrastructure.mongo.models.training.training_session_model import TrainingSessionModel


class TrainingSessionMongoMapper(AbstractMongoMapper[TrainingSession, TrainingSessionModel]):
    def entity_to_model(self, entity: TrainingSession) -> TrainingSessionModel:
        optimizer = OptimizerModel(type=entity.optimizer.type, params=entity.optimizer.params)
        model = TrainingSessionModel(
            user=entity.user,
            network_id=entity.network_id,
            dataset_id=entity.dataset_id,
            optimizer=optimizer,
            loss_function=entity.loss_function,
            metrics=entity.metrics,
            epochs=entity.epochs,
            batch_size=entity.batch_size,
            validation_split=entity.validation_split,
        )
        if entity.id is not GENERATED_VALUE:
            model.id = ObjectId(entity.id)

        return model

    def model_to_entity(self, model: TrainingSessionModel) -> TrainingSession:
        optimizer = Optimizer(type=model.optimizer.type, params=model.optimizer.params)
        entity = TrainingSession(
            id=str(model.id),
            network_id=model.network_id,
            dataset_id=model.dataset_id,
            optimizer=optimizer,
            loss_function=model.loss_function,
            metrics=model.metrics,
            epochs=model.epochs,
            batch_size=model.batch_size,
            validation_split=model.validation_split,
        )
        return entity
