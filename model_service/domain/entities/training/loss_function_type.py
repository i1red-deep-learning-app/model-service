from enum import Enum


class LossFunctionType(Enum):
    BINARY_CROSSENTROPY = "binary_cross_entropy"
    SPARSE_CATEGORICAL_CROSSENTROPY = "categorical_cross_entropy"
