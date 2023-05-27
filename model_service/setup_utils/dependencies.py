from model_service.domain.data_storage.abstract_data_storage import AbstractDataStorage
from model_service.domain.entities.dataset.table_dataset import TableDataset
from model_service.domain.entities.training.training_result import TrainingResult
from model_service.domain.repositories.abstract_feed_forward_network_repository import (
    AbstractFeedForwardNetworkRepository,
)
from model_service.domain.repositories.abstract_table_dataset_repository import AbstractTableDatasetRepository
from model_service.domain.repositories.abstract_training_result_repository import AbstractTrainingResultRepository
from model_service.domain.repositories.abstract_training_session_repository import AbstractTrainingSessionRepository
from model_service.infrastructure.mongo.documents.dataset.table_dataset_document import TableDatasetDocument
from model_service.infrastructure.mongo.documents.training.training_result_document import TrainingResultDocument
from model_service.infrastructure.mongo.mappers.default_mongo_mapper import DefaultMongoMapper
from model_service.infrastructure.mongo.mappers.feed_forward_network_mongo_mapper import FeedForwardNetworkMongoMapper
from model_service.infrastructure.mongo.mappers.training_session_mongo_mapper import TrainingSessionMongoMapper
from model_service.infrastructure.mongo.repositories.mongo_feed_forward_network_repository import (
    MongoFeedForwardNetworkRepository,
)
from model_service.infrastructure.mongo.repositories.mongo_table_dataset_repository import MongoTableDatasetRepository
from model_service.infrastructure.mongo.repositories.mongo_training_result_repository import (
    MongoTrainingResultRepository,
)
from model_service.infrastructure.mongo.repositories.mongo_training_session_repository import (
    MongoTrainingSessionRepository,
)
from model_service.infrastructure.s3.s3_data_storage import S3DataStorage
from model_service.setup_utils.s3 import S3Settings
from model_service.shared.dependency_management.providers.singleton_dependency_provider import (
    SingletonDependencyProvider,
)


def setup_dependencies(provider: SingletonDependencyProvider) -> None:
    s3_settings = S3Settings()
    provider.set(
        AbstractFeedForwardNetworkRepository, MongoFeedForwardNetworkRepository(FeedForwardNetworkMongoMapper())
    )
    provider.set(AbstractTrainingSessionRepository, MongoTrainingSessionRepository(TrainingSessionMongoMapper()))
    provider.set(
        AbstractTableDatasetRepository,
        MongoTableDatasetRepository(DefaultMongoMapper(TableDataset, TableDatasetDocument)),
    )
    provider.set(
        AbstractTrainingResultRepository,
        MongoTrainingResultRepository(DefaultMongoMapper(TrainingResult, TrainingResultDocument)),
    )
    provider.set(AbstractDataStorage, S3DataStorage(s3_settings.bucket_name))
