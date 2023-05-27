from model_service.domain.entities.training.training_session import TrainingSession
from model_service.domain.entities.value_objects.optimizer import Optimizer
from model_service.infrastructure.mongo.mappers.abstract_mongo_mapper import AbstractMongoMapper
from model_service.infrastructure.mongo.documents.training.optimizer_document import OptimizerDocument
from model_service.infrastructure.mongo.documents.training.training_session_document import TrainingSessionDocument


class TrainingSessionMongoMapper(AbstractMongoMapper[TrainingSession, TrainingSessionDocument]):
    def entity_to_document(self, entity: TrainingSession) -> TrainingSessionDocument:
        optimizer = OptimizerDocument(type=entity.optimizer.type, params=entity.optimizer.params)
        document = TrainingSessionDocument(
            id=entity.id,
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

        return document

    def document_to_entity(self, document: TrainingSessionDocument) -> TrainingSession:
        optimizer = Optimizer(type=document.optimizer.type, params=document.optimizer.params)
        entity = TrainingSession(
            id=document.id,
            user=document.user,
            network_id=document.network_id,
            dataset_id=document.dataset_id,
            optimizer=optimizer,
            loss_function=document.loss_function,
            metrics=document.metrics,
            epochs=document.epochs,
            batch_size=document.batch_size,
            validation_split=document.validation_split,
        )

        return entity
