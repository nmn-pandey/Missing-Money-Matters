# Challenge 2

"""
CREATED BY: NAMAN PANDEY
DATE: 07/02/2024
QUESTION 3: How many transactions are above the average transaction amount during the same time period?
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

# Calculate the average total for the specified date range
average_total_pipeline = [
    {
        "$match": {
            # Filter documents within the specified date range
            "InvoiceDate": {"$gte": start_date, "$lte": end_date}
        }
    },
    {
        "$group": {
            "_id": None,
            # Calculate the average total
            "average_total": {"$avg": "$Total"}
        }
    }
]

# Execute the aggregation pipeline
average_total_result = list(db.Invoice.aggregate(average_total_pipeline))
# Extract the average total from the result
average_total = average_total_result[0]['average_total'] if average_total_result else 0

print(f"Average Total is {average_total}")

# Aggregation pipeline to count transactions above average
pipeline = [
    {
        "$match": {
            # Filter documents where the total is greater than the average total
            "Total": {"$gt": average_total},
             # Filter documents within the specified date range
            "InvoiceDate": {"$gte": start_date, "$lte": end_date}
        }
    },
    {
        # Count the number of documents that match the filter
        "$count": "Transactions above Average"
    }
]

# Execute the aggregation pipeline
transactions_above_average = list(db.Invoice.aggregate(pipeline))

print(f"{transactions_above_average[0]['Transactions above Average']} transactions are above average.")