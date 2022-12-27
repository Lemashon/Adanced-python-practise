import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["test"]
coll = db["test"]
coll.insert_one({"name": "Allen", "age":30})
docs = coll.find({})
for doc in docs:
    print (doc)
    
client.close()