#----------------------
# Title: trejo-user-update.py
# Author: Professor Krasso
# Date: 05 13 2022
# Modified By: Allan Trejo
# Description: Updates user in database using Python and MongoDB 
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

#Update users email 
db.users.update_one(
    {
        "employee_id": "12345678"},
        {
            "$set":{
                "email":"altrejo@my365.bellevue.edu"
            }
        }
)

#print results of find one query with certain fields 
pprint.pprint(db.users.find_one({"employee_id": "12345678"},
{ 
    "email":1,
    "employee_id":1,
    "first_name":1,
    "last_name":1,
}))