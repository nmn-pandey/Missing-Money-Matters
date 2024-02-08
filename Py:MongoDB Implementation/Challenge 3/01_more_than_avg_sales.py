# Challenge 3

"""
CREATED BY: NAMAN PANDEY
DATE: 07/02/2024
QUESTION 1: Get a list of employees who exceeded the average transaction amount from sales they generated during 2011 and 2012.
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

# Pipeline to get the average sales during 2011 and 2012
average_sales_pipeline = [
    {
        "$match" : {
            "InvoiceDate": {
                "$gte": start_date,
                "$lte": end_date
            }
        }
    },
    {
        "$group": {
            "_id": None,
            "average_total": {
                "$avg": "$Total"
            }
        }
    }
]

# Execute the average sales pipeline
average_sales_result = list(db.Invoice.aggregate(average_sales_pipeline))
average_sales = average_sales_result[0]['average_total']

print(f"Average transaction amount from sales during 2011 and 2012 is {average_sales}")

# Pipeline to get employees who exceeded this average sales amount
exceeding_employees_pipeline = [
    {
        "$match": {
            "Total": {
                "$gt": average_sales,
            },
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
        "$sort": {"First Name": 1}
    }
]

# Execute the average sales pipeline
exceeding_employees_result = list(db.Invoice.aggregate(exceeding_employees_pipeline))

# Print the results
for employee in exceeding_employees_result:
    print(employee)


# Displaying the results in a tabular manner
"""
from tabulate import tabulate

table_data = []
for employee in exceeding_employees_result:
    row = [employee["Employee ID"],
           employee["firstname"],
           employee["lastname"],
           employee["salesMade"]]
    table_data.append(row)

# Print results in tabular format
headers = ["Employee ID", "First Name", "Last Name", "Total Sales Made"]
print(tabulate(table_data, headers=headers, tablefmt="grid"))
"""