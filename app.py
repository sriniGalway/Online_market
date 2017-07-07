from flask import Flask
from flask_restful import Api


from product import Product, ProductList

app = Flask(__name__)
api = Api(app)

api.add_resource(Product, '/product/<string:product_code>')
api.add_resource(ProductList, '/products')

if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True
