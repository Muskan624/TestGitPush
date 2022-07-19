import pymongo
#creating connection between python and mondodb server
client = pymongo.MongoClient("mongodb+srv://Muskan:Somu123@clustermongodb.kmygs.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
# inserting record in mongodb database
d={
    "name":"Muskan",
    "email":"muskan@ineuron.com",
    "surname":"Sinha"

}
db1=client["test1"]
coll=db1["test"]
coll.insert_one(d)
