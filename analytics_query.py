from sqlalchemy import create_engine

def get_top_products(db_url):
    engine = create_engine(db_url)
    query = """
    SELECT product_id, SUM(total_price) as revenue
    FROM sales_data
    GROUP BY product_id
    ORDER BY revenue DESC
    LIMIT 5;
    """
    result = engine.execute(query)
    for row in result:
        print(row)

if __name__ == "__main__":
    DATABASE_URL = "sqlite:///data/sales_data.db"
    get_top_products(DATABASE_URL)
