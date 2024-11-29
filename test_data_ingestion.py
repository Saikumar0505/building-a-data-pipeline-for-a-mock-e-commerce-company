import os
from src.data_ingestion import ingest_data

def test_ingest_data():
    input_path = "data/raw/"
    output_path = "data/processed/sales_combined.csv"
    ingest_data(input_path, output_path)
    assert os.path.exists(output_path)
