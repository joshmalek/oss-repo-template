import pymongo
from pymongo import MongoClient
import pprint
from bson.objectid import ObjectId
import math
import random
import datetime
client = MongoClient()
db = client.mongo_db_lab
defi = db.definitions

def random_word_requester():
    num_docs = defi.find().count()
    rand = random.randint(0, num_docs)
    select = defi.find().skip(rand)
    for x,obj in enumerate(defi.find()):
        if(x == rand):
            obj_id = obj["_id"]
            time = datetime.datetime.isoformat(datetime.datetime.utcnow())
            defi.update({'_id': obj_id}, {'$push': {'dates': time}},upsert = True)
            
            #defi.update_one({"_id":obj_id,{""}})
            return(defi.find_one({'word':obj["word"]}))
            
if __name__ == '__main__':
    print(random_word_requester())
