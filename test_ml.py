import pytest
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import fbeta_score, precision_score, recall_score
from ml.model import (train_model,compute_model_metrics)
from ml.data import apply_label
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
def test_():
    """
    # Testing the 
    """
    pass

    


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # add description for the third test
    """
    # Your code here
    pass
