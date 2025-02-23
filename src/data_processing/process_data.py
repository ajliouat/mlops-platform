import pandas as pd

def process_data(file_path):
    # Load data
    data = pd.read_csv(file_path)
    
    # Example: Drop missing values
    data = data.dropna()
    
    # Save processed data
    data.to_csv("data/processed_data.csv", index=False)