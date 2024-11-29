import pandas as pd
from sqlalchemy import create_engine

def load_data_to_db(db_url, input_file):
    engine = create_engine(db_url)
    df = pd.read_csv(input_file)
    df.to_sql("sales_data", con=engine, if_exists="replace", index=False)
    print(f"Data loaded into database: {db_url}")

if __name__ == "__main__":
    DATABASE_URL = "sqlite:///data/sales_data.db"
    load_data_to_db(DATABASE_URL, "data/cleaned/sales_cleaned.csv")
