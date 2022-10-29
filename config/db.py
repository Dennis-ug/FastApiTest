from pymongo import MongoClient
conn = MongoClient("mongodb://localhost:27017/?readPreference=primary&ssl=false&directConnection=true/done")
