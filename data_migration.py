# Move to Orders.csv file to Mysql Database if Tables are Empty !
import pandas as pd
from db import create_conn
from datetime import datetime

def data_migration_db():
    db = create_conn()
    cursor = db.cursor()
    csv_file_path = "./orders.csv"

    data = pd.read_csv(csv_file_path)

    try:
        for _, row in data.iterrows():
            print(f'import product id - {row["product_id"]}')
            order_date = datetime.strptime(row["order_date"], "%d-%m-%Y")
            order_date = order_date.strftime("%Y-%m-%d")

            cursor.execute(f'INSERT INTO `orders`(`order_date`, `ship_mode`, `segment`, `country`, `city`, `state`, `postel_code`, `region`) VALUES ("{order_date}" , "{row["ship_mode"]}" , "{row["segment"]}" , "{row["country"]}" ,"{row["city"]}", "{row["state"]}" , "{row["postel_code"]}" , "{row["region"]}")')
            orderId = cursor.lastrowid
            selling_price = row["list_price"] * (1 - (row["quantity"]/100))
            total_price = selling_price * row["quantity"]
            margin_price = selling_price - row["cost_price"]
            profit_price = margin_price * row["quantity"]
            cursor.execute(f'INSERT INTO `order_products`(`order_id`, `category`, `sub_category`, `product_id`, `cost_price`, `list_price`, `quantity`, `discount_percent`, `selling_price`, `total_price`, `margin_price`, `profit_price`) VALUES ("{orderId}" ,"{row["category"]}" , "{row["sub_category"]}" , "{row["product_id"]}" , "{row["cost_price"]}" , "{row["list_price"]}" , "{row["quantity"]}", "{row["discount_percent"]}" , "{selling_price}" , "{total_price}" , "{margin_price}" , "{profit_price}")')
        print(f"Data imported successfully !")

    except Exception as err:
        print(f"Error: {err}")

    finally:
        cursor.close()
        db.commit()
        db.close()

data_migration_db()