# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse
import sqlite3

class Product(Resource):
    TABLE_NAME = 'products'

    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float
    )
    parser.add_argument('product_name',
        type=str
    )
   
    #GET /product/{product_id} – Return a single product in JSON format.
    def get(self, product_code):
        product = self.find_by_product(product_code)
        if product:
            return product
        return {'message': 'Product not found'}, 404

    @classmethod
    #Select query to find the product by product_code from the products db
    def find_by_product(cls, product_code):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE product_code=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (product_code,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'product_code': row[0], 'product_name': row[1], 'price': row[2]}

    #POST /product – Create a new product using posted form data
    def post(self, product_code):
        if self.find_by_product(product_code):
            return {'message': "An product with product_code '{}' already exists.".format(product_code)}

        data = Product.parser.parse_args()
        product = {'product_code': product_code, 'product_name': data['product_name'], 'price': data['price']}
        print product 
        
#        try:
        Product.insert(product)
 #       except:
 #           return {"message": "An error occurred inserting the product."}

        return product

    #Insert query to insert data new product to db - products
    @classmethod
    def insert(cls, product):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO {table} VALUES(?, ?, ?)".format(table=cls.TABLE_NAME)
        cursor.execute(query, (product['product_code'], product['product_name'], product['price']))

        connection.commit()
        connection.close()

    #DELETE /product/{product_id} – Delete a product by id.
    def delete(self, product_code):
        if not self.find_by_product(product_code):
            return {'message': "An product with product_code '{}' does not exists.".format(product_code)}, 404

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM {table} WHERE product_code=?".format(table=self.TABLE_NAME)
        cursor.execute(query, (product_code,))

        connection.commit()
        connection.close()
        return {'message': 'Product deleted'}, 200
        

    #PUT /product/{product_id} – Update a product’s name or price by id. We need to provide both product_name and price to update
    def put(self, product_code):
        if not self.find_by_product(product_code):
            return {'message': "An product with product_code '{}' does not exists.".format(product_code)}, 404

        data = Product.parser.parse_args()
        product = self.find_by_product(product_code)
        updated_product = {'product_code': product_code, 'product_name': data['product_name'], 'price': data['price']}
        if product is None:
            try:
                Product.insert(updated_product)
            except:
                return {"message": "An error occurred inserting the product."}
        else:
            try:
                Product.update(updated_product)
            except:
                raise
                return {"message": "An error occurred updating the product."}
        return updated_product

    @classmethod
    #Update query to update data update_product to db - products
    def update(cls, product):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE {table} SET product_name=?,price=? WHERE product_code=?".format(table=cls.TABLE_NAME)
        cursor.execute(query, (product['product_name'], product['price'], product['product_code']))

        connection.commit()
        connection.close()


class ProductList(Resource):
    TABLE_NAME = 'products'

    #GET /products – A list of products, names, and prices in JSON format.
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table}".format(table=self.TABLE_NAME)
        result = cursor.execute(query)
        products = []
        for row in result:
            products.append({'product_code': row[0], 'product_name': row[1], 'price': row[2]})
        connection.close()

        return products
