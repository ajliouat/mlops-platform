import pandas as pd
from src.data_processing.process_data import process_data

def test_process_data():
    process_data("data/raw_data.csv")
    processed_data = pd.read_csv("data/processed_data.csv")
    assert not processed_data.isnull().any().any()