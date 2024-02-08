# Challenge 2

"""
CREATED BY: NAMAN PANDEY
DATE: 07/02/2024
QUESTION 2: Get a list of customers, sales reps, and total transaction amounts for each customer between 2011 and 2012.
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

# Define the date range - DIDN'T WORK SINCE DATE IS SAVED AS STRING IN OUR CURRENT DB
#start_date = datetime(2011, 1, 1)
#end_date = datetime(2012, 12, 31)

# Aggregation pipeline
pipeline = [
    {
        "$match": {
            "InvoiceDate": {"$gte": start_date, "$lte": end_date}
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
            "_id": {
                "City": "$customer.City",
                "State": "$customer.State",
                "FirstName": "$customer.FirstName",
                "LastName": "$customer.LastName",
                "SalesRepFirstName": "$employee.FirstName",
                "SalesRepLastName": "$employee.LastName"
            },
            "Email": {"$first": "$customer.Email"},
            "Address": {"$first": "$customer.Address"},
            "PurchasesMade": {"$sum": "$Total"}
        }
    },
    {
        "$project": {
            "Name": {"$concat": ["$_id.FirstName", " ", "$_id.LastName"]},
            "Email": 1,
            "Address": {"$concat": ["$Address", ", ", "$_id.City", ", ", "$_id.State"]},
            "SalesRep": {"$concat": ["$_id.SalesRepFirstName", " ", "$_id.SalesRepLastName"]},
            "PurchasesMade": 1,
            "_id": 0
        }
    },
    {
        "$sort": {"Name": 1}
    }
]

# Execute the aggregation pipeline
results = list(db.Invoice.aggregate(pipeline))

# Print the results
for result in results:
    name = f"{result['Name']}"
    email = result['Email']
    address = result['Address']
    sales_rep = result['SalesRep']
    purchases_made = result['PurchasesMade']

    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Address: {address}")
    print(f"Sales Rep: {sales_rep}")
    print(f"Purchases Made: {purchases_made}")
    print()


# TO SHOW RESULTS IN TABULAR FORM
"""
from tabulate import tabulate

# Execute the aggregation pipeline
results = list(db.Invoice.aggregate(pipeline))

# Prepare data for tabulate
table_data = []
for result in results:
    name = f"{result['Name']}"
    email = result['Email']
    address = result['Address']
    sales_rep = result['SalesRep']
    purchases_made = result['PurchasesMade']

    table_data.append([name, email, address, sales_rep, purchases_made])

# Print results in tabular format
headers = ["Name", "Email", "Address", "Sales Rep", "Purchases Made"]
print(tabulate(table_data, headers=headers, tablefmt="grid"))
"""