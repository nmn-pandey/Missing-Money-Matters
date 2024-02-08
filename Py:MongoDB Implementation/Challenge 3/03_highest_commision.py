# Challenge 3

"""
CREATED BY: NAMAN PANDEY
DATE: 08/02/2024
QUESTION 3: Which employee made the highest commission?
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

# Pipeline to print the employee who made the highest commision payout
commision_payout_pipeline = [
    {
        "$match": {
            "InvoiceDate": {
                "$gte": start_date,
                "$lte": end_date
            }
        }
    },
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
        "$lookup": {
            "from": "Employee",
            "localField": "customer.SupportRepId",
            "foreignField": "EmployeeId",
            "as": "employee"
        }
    },
    {
        "$unwind": "$employee"
    },
    {
        "$group": {
            "_id": "$employee.EmployeeId",
            "firstname": {
                "$first": "$employee.FirstName"
                },
            "lastname": {
                "$first": "$employee.LastName"
                },
            "Employee ID": {
                "$first": "$employee.EmployeeId"
                },
            "salesMade": {
                "$sum": "$Total"
            }
        }
    },
    {
        "$addFields": { # Calculate commission payout (15% of total sales) and round to 2 decimal places
            "commisionPayout": {
                "$round": [
                    {"$multiply": ["$salesMade", 0.15]},
                    2]
            }
        }
    },
    {
        # Sorting the commision payout in descending order
        "$sort": {"commisionPayout": -1}
    },
    {
        # limiting the results returned to only the top
        "$limit": 1
    }
]

# Execute the average sales pipeline
commision_payout_results = list(db.Invoice.aggregate(commision_payout_pipeline))

# Print the results
for employee in commision_payout_results:
    print(employee)