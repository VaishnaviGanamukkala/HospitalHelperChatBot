import pymongo

myclient = pymongo.MongoClient("mongodb://admin:admin@localhost:27017/")
mydb = myclient["rasa_history"]
mycol = mydb["NAME_COLECTION"]

x = mycol.find()

print(x)