import pytest
import os
import pandas as pd
# TODO: add necessary import
from sklearn.ensemble import AdaBoostClassifier
from ml.model import (train_model)
from ml.data import (process_data)


# TODO: implement the first test. Change the function name and input as needed
@pytest.fixture
def data():
    project_path = os.getcwd()
    data_path = os.path.join(project_path, "data", "census.csv")
    data = pd.read_csv(data_path)
    return data


@pytest.fixture
def cat_features():
    cat_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]
    return cat_features


def test_data_size(data):
    """
    This test checks that the size of the data is > 1000 entries.
    """
    assert data.shape[0] > 1000, f'Data has greater than 1000 entries'


# TODO: implement the second test. Change the function name and input as needed
def test_model_type(data, cat_features):
    """
    This tests that the model type remains as AdaBoostClassifier
    """
    X, y, _, _ = process_data(
        data,
        categorical_features=cat_features,
        label="salary"
    )
    model = train_model(X, y)
    assert isinstance(model, AdaBoostClassifier)


# TODO: implement the third test. Change the function name and input as needed
def test_cols(data, cat_features):
    """
    This tests if the dataframe containes the expected column labels.
    """
    col_names = list(data)

    i = 0

    for feat in cat_features:
        if feat in col_names:
            i += 1

    assert i == len(cat_features)
