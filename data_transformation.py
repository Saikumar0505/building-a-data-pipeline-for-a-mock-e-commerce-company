import pandas as pd

def transform_data(input_file, output_file):
    df = pd.read_csv(input_file)
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['total_price'] = df['quantity'] * df['price_per_unit']
    df = df.dropna()
    df.to_csv(output_file, index=False)
    print(f"Data transformed and saved to {output_file}")

if __name__ == "__main__":
    transform_data("data/processed/sales_combined.csv", "data/cleaned/sales_cleaned.csv")
