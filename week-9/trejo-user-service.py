#----------------------
# Title: trejo-user-service.py
# Author: Professor Krasso
# Date: 05 13 2022
# Modified By: Allan Trejo
# Description: Python Connection to Local MongoDB instance
#--------------------
from pymongo import MongoClient
import pprint
import datetime

#Establish a connection with local Mongo Instance
client = MongoClient('localhost', 27017)

#Prints to console client connection 
print(client)

#use web335 db 
db = client.web335

#User document model
user = {
    "first_name":"Odyole",
    "last_name":"Rules",
    "email":"awesome@employee.com",
    "employee_id":"12345678",
    "date_created": datetime.datetime.utcnow()
}

#store autogenerated id
user_id = db.users.insert_one(user).inserted_id

#print to console autogenerated ID
print(user_id)

#print results of find one query
pprint.pprint(db.users.find_one({"employee_id": "12345678"}))