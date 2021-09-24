import pymongo

client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
mydb = client['Employee']
# Creating a database name
# or if it already exists then connecting to it
Employeeinformation='xyz'
information = mydb.Employeeinformation
# Created a collection of employeeinformation

records = [{'first_name': 'Suraj', 'last_name': 'Joshi',
            'department': 'Analytics'},
           {'first_name': 'Suraj', 'last_name': 'Joshi',
            'department': 'Analytics'},
           {'first_name': 'Suraj', 'last_name': 'Joshi',
            'department': 'Analytics'},
           ]
information.insert_many(records)

# db=client['Employee']
# data=db['employeeinformation'].find({})
# print(data)
# print('Yes, you')