# Challenge 1

"""
CREATED BY: NAMAN PANDEY
DATE: 28/01/2024
QUESTION 2: How much money did WSDA Music make during the same period?
"""

from pymongo import MongoClient
from datetime import datetime

# Connect to the MongoDB client (replace with your connection URI if not local)
client = MongoClient("mongodb://localhost:27017/")

# Select the database and collection
db = client["WSDA_Music"]
invoice_collection = db["Invoice"]

# Define the date range in the string format
start_date = '2011-01-01 00:00:00'
end_date = '2012-12-31 23:59:59'

# Aggregation pipeline to filter and sum total sales
pipeline = [
    {
        "$match": {
            "InvoiceDate" : {
                "$gte": start_date,
                "$lte": end_date
            }
        }
    },
    {
        "$group": {
            "_id": None,
            "Total Sales": { "$sum" : "$Total"}
        }
    }
]
# Execute the aggregation pipeline on the 'invoice_collection' and convert the result to a list.
# The aggregation pipeline is stored in the 'pipeline' variable and is designed to filter documents by date and sum their sales.
total_sales_list = list(invoice_collection.aggregate(pipeline))

# Extract the total sales amount from the first element of the 'total_sales_list'.
total_sales = total_sales_list[0]['Total Sales']

print("Total Sales made between 2011 and 2012 is", total_sales)
