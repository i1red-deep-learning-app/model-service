from tensorflow.python.keras import metrics

from model_service.domain.entities.training.metric_type import MetricType


def create_metric(metric: MetricType) -> metrics.Metric:
    match metric:
        case MetricType.ACCURACY:
            return metrics.Accuracy()
        case MetricType.SPARSE_CATEGORICAL_ACCURACY:
            return metrics.SparseCategoricalAccuracy()
        case _:
            raise NotImplementedError("Metric not supported")
