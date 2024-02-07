# Challenge 2

"""
CREATED BY: NAMAN PANDEY
DATE: 28/01/2024
QUESTION 1: Get a list of customers who made purchases between 2011 and 2012.
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

# Aggregation pipeline
pipeline = [
    {
        "$lookup": {
            "from": "Customer",
            "localField": "CustomerId",
            "foreignField": "CustomerId",
            "as": "customerDetails"
        }
    },
    {
        "$unwind": "$customerDetails"
    },
    {
        "$match": {
            "InvoiceDate": {
                "$gte": start_date,
                "$lte": end_date
            }
        }
    },
    {
        "$group": {
            "_id": {
                "FirstName": "$customerDetails.FirstName",
                "LastName": "$customerDetails.LastName",
                "City": "$customerDetails.City",
                "State": "$customerDetails.State"
            },
            "Email": {"$first": "$customerDetails.Email"},
            "Address": {"$first": "$customerDetails.Address"}
        }
    },
    {
        "$sort": {"_id.FirstName": 1}
    }
]

# Execute the aggregation pipeline
customers = list(db.Invoice.aggregate(pipeline))

# Print the results
for customer in customers:
    full_name = f"{customer['_id']['FirstName']} {customer['_id']['LastName']}"
    address = customer['Address']
    city = customer['_id'].get('City', '')
    state = customer['_id'].get('State', '')
    email = customer['Email']

    print(f"Name: {full_name}")
    print(f"Address: {address}")
    print(f"City: {city}")
    print(f"State: {state}")
    print(f"Email: {email}")
    print()


# TO SHOW RESULTS IN TABULAR FORM
"""
from tabulate import tabulate

# Execute the aggregation pipeline
customers = list(db.Invoice.aggregate(pipeline))

# Prepare data for tabulate
table_data = []
for customer in customers:
    full_name = f"{customer['_id']['FirstName']} {customer['_id']['LastName']}"
    address = customer['Address']
    city = customer['_id'].get('City', '')
    state = customer['_id'].get('State', '')
    email = customer['Email']

    table_data.append([full_name, address, city, state, email])

# Print results in tabular format
headers = ["Full Name", "Address", "City", "State", "Email"]
print(tabulate(table_data, headers=headers, tablefmt="grid"))
"""