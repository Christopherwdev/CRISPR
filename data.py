import pandas as pd

def load_data(filepath):
    """Loads data from a CSV file."""
    try:
        data = pd.read_csv(filepath)
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None

def preprocess_data(data):
    """Performs basic data preprocessing."""
    # Handle missing values (e.g., imputation or removal)
    data.dropna(inplace=True) #Simple example, replace with more sophisticated handling

    # Convert data types if necessary
    # ...

    return data
