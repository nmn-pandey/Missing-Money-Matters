# Challenge 2

"""
CREATED BY: NAMAN PANDEY
DATE: 07/02/2024
QUESTION 4: What is the average transaction amount for each year that WSDA Music has been in business?
"""

from pymongo import MongoClient
from datetime import datetime

# Connect to the MongoDB client (replace with your connection URI if not local)
client = MongoClient("mongodb://localhost:27017/")

# Select the database and collection
db = client["WSDA_Music"]
invoice_collection = db["Invoice"]

# Aggregation pipeline to calculate average transaction amount by year
pipeline = [
    {
        "$group": {
            "_id": {
                "$substr": ["$InvoiceDate", 0, 4]  # Extract the first 4 characters (the year) from the InvoiceDate field
            },
            "Average Transaction Amount": {"$avg": "$Total"}  # Calculate average total for each year
        }
    },
    {
        "$project": {
            "_id": 0,  # Exclude _id field from the result
            "Year": "$_id",  # Rename _id to Year
            "Average Transaction Amount": {"$round": ["$Average Transaction Amount", 2]}  # Round average total to two decimal places
        }
    },
    {
        "$sort": {"Year": 1}  # Sort results by year in ascending order
    }
]

# Execute the aggregation pipeline
average_transaction_amount_by_year = list(db.Invoice.aggregate(pipeline))

# Print the results
for result in average_transaction_amount_by_year:
    print(result)


# Showing results in tabular form
"""
from tabulate import tabulate

# Execute the aggregation pipeline
average_transaction_amount_by_year = list(db.Invoice.aggregate(pipeline))

# Prepare data for tabulate
table_data = []
for result in average_transaction_amount_by_year:
    row = [result['Year'], result['Average Transaction Amount']]
    table_data.append(row)

# Print results in tabular format
headers = ["Year", "Average Transaction Amount"]
print(tabulate(table_data, headers=headers, tablefmt="grid"))
"""