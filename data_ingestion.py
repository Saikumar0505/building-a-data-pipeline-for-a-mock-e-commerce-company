import os
import pandas as pd

def ingest_data(input_path, output_path):
    files = os.listdir(input_path)
    data = []
    for file in files:
        if file.endswith(".csv"):
            file_path = os.path.join(input_path, file)
            df = pd.read_csv(file_path)
            data.append(df)
    combined_data = pd.concat(data)
    combined_data.to_csv(output_path, index=False)
    print(f"Data ingested and saved to {output_path}")

if __name__ == "__main__":
    ingest_data("data/raw", "data/processed/sales_combined.csv")
