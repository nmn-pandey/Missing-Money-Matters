# Challenge 3

"""
CREATED BY: NAMAN PANDEY
DATE: 08/02/2024
QUESTION 4: List the customers that the employee identified in the last question.
"""

from pymongo import MongoClient
from tabulate import tabulate
from datetime import datetime

# Connect to the MongoDB client (replace with your connection URI if not local)
client = MongoClient("mongodb://localhost:27017/")

# Select the database and collection
db = client["WSDA_Music"]
# Write the query for filtering customers whose support rep is Jane (SupportRepId is 3)
query = {"SupportRepId": 3}

# Executing that query
results = db.Customer.find(query)

# Printing results
#for customer in results:
#    print(customer)

# Displaying data in tabular form
table_data = []
for customer in results:
    # Access fields using .get() method to handle missing fields gracefully
    row = [
        customer.get("CustomerId", ""),
        customer.get("FirstName", "") + " " + customer.get("LastName", ""),
        (customer.get("Address", "") + " " + customer.get("City", "") + " " + customer.get("State", "") + " " + customer.get("Country", "")).strip(),
        customer.get("Email", ""),
        customer.get("Phone", "")
    ]
    table_data.append(row)

headers = ["Customer ID", "Name", "Address", "Email", "Phone"]
print(tabulate(table_data, headers=headers, tablefmt="grid"))

