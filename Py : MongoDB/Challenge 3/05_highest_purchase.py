# Challenge 3

"""
CREATED BY: NAMAN PANDEY
DATE: 08/02/2024
QUESTION 5: 
"""

from pymongo import MongoClient
from datetime import datetime

# Connect to the MongoDB client (replace with your connection URI if not local)
client = MongoClient("mongodb://localhost:27017/")

# Select the database and collection
db = client["WSDA_Music"]

# pipeline to retrieve the customer who made the highest purchase
purchases_pipeline = [
    {
        "$lookup": {
            "from": "Customer",
            "localField": "CustomerId",
            "foreignField": "CustomerId",
            "as": "customer"
        }
    },
    {
        "$unwind": "$customer"
    },
    {
        "$group": {
            "_id": "$customer.CustomerId",
            "firstname": {
                "$first": "$customer.FirstName"
                },
            "lastname": {
                "$first": "$customer.LastName"
                },
            "purchasesMade": {
                "$sum": "$Total"
            }
        }
    },
    {
        "$sort": {"purchasesMade": -1}
    },
    {
        "$limit": 1
    }
]

# Execute the pipeline
purchases_results = list(db.Invoice.aggregate(purchases_pipeline))

# Print the result
print(purchases_results)

"""
Based on the above, we can see John Doeein has no details and has made extremely high purchases
which could point out that it is a false record, created by Jane Peacock.
Hence the financial discrepancy could be attributed to Jane Peacock.
"""