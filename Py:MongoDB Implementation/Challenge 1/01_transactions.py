# Challenge 1

"""
CREATED BY: NAMAN PANDEY
DATE: 28/01/2024
QUESTION 1: How many transactions took place between the years 2011 and 2012?
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

# Query to count number of documents/records
number_of_transactions = invoice_collection.count_documents({
    "InvoiceDate": {
        "$gte": start_date,
        "$lte": end_date
    }
})

# Print number of transactions
print(f"{number_of_transactions} Transactions took place between 2011 and 2012")