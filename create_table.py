# -*- coding: utf-8 -*-
import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()


#Create table query to create products table with initial products
create_table = "CREATE TABLE IF NOT EXISTS products (product_code text PRIMARY KEY, product_name text, price real)"
cursor.execute(create_table)

### products available on our site initially
insert_data = """INSERT INTO products (product_code, product_name, price) VALUES 
('001', 'Lavender heart', 9.25),
('002', 'Personalised cufflinks', 45.00),
('003', 'Kids T-shirt', 19.95);"""

cursor.execute(insert_data)

connection.commit()

connection.close()
