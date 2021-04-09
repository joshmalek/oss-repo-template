import pymongo
from pymongo import MongoClient
import pprint
from bson.objectid import ObjectId
client = MongoClient()
db = client.mongo_db_lab
defi = db.definitions
print("find_all = retrieved " +str(defi.find().count()) + " definitions")
print("find_one = ")
pprint.pprint(defi.find_one())
print("find capitaland record =")
pprint.pprint(defi.find_one({"word": "Capitaland"}))

print("find by id (56fe9e22bad6b23cde07b93f) = ")
pprint.pprint(defi.find_one({'_id': ObjectId('56fe9e22bad6b23cde07b93f')}))

print("Inserting new record ")
new_word = {"word": "Funding","definition": "A myth told to grad students"}
defi.insert_one(new_word)
print("find Funding record =")
pprint.pprint(defi.find_one({"word": "Funding"}))