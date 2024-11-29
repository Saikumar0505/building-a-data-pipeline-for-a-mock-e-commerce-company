import pandas as pd
from src.data_transformation import transform_data

def test_transform_data():
    input_file = "data/processed/sales_combined.csv"
    output_file = "data/cleaned/sales_cleaned.csv"
    transform_data(input_file, output_file)
    df = pd.read_csv(output_file)
    assert "total_price" in df.columns
