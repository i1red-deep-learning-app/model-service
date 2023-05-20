import numpy as np
import pandas as pd
import pytest


@pytest.fixture
def data(labels_column: str) -> pd.DataFrame:
    data_size = 1000
    column_1_data = np.random.randn(data_size)
    labels = (column_1_data > 0.5).astype("int")
    return pd.DataFrame({"column_1": column_1_data, labels_column: labels})
