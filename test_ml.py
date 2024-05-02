import pytest
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import fbeta_score, precision_score, recall_score
from ml.model import (train_model,compute_model_metrics)
from ml.data import (apply_label,process_data)
# TODO: add necessary import

# TODO: implement the first test. Change the function name and input as needed

@pytest.fixture
def data():
    project_path = os.getcwd()
    data_path = os.path.join(project_path, "data", "census.csv")
    data = pd.read_csv(data_path)
    return data

def test_data_size(data):
    """
    #This test checks that the size of the data is > 1000 entries.
    """
    assert data.shape[0]>1000, f'Data has greater than 1000 entries'


# TODO: implement the second test. Change the function name and input as needed
def test_model_type(data):
    """
    # Testing the model type
    """
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
    X, y, _, _ = process_data(
    data,
    categorical_features=cat_features,
    label="salary"
)
    model=train_model(X,y)
    assert isinstance(model, AdaBoostClassifier)
    


# TODO: implement the third test. Change the function name and input as needed
def test_three(data):
    """
    # add description for the third test
    """
    # Your code here
    train, test = train_test_split(data, test_size= 0.25, random_state=42)
    assert train.shape[0]>750,('Training Data has greater than 750 entries')
    assert test.shape[0]>250,('Testing Data has greater than 250 entries')

 
