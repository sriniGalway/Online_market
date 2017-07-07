# Online_market
Online market python API

Technolgies used:
-----------------

Python 
Flask

Files:
------
```
requirements.txt - Holds list of Python pip dependencies
app.py - main Flask app python file
create_table.py - To create the data.db with product table and initial data
product.py - python file with main processing logic
```

Command Line Execution:
-----------------------

To install all Python dependencies:

    sudo pip install -r requirements.txt

To create the data.db with product table and initial data, use (ensure that the data.db does not exist):

    python create_table.py

To run the online market application, use:

    python app.py

Then to feed in test messages use:
Follow the below postman document for the rest API call - 
https://documenter.getpostman.com/view/464098/restfulapi-sqlite-products/6fWzjon
For ex: to perform GET, 
curl --request GET \
  --url http://127.0.0.1:5000/product/002 \
  --header 'content-type: application/json'
