import pymongo
from pymongo import MongoClient
connection = MongoClient('localhost', 3001)
# connect via database name
db = connection.meteor
# get collection from database
tasks = db.tasks
# insert something into the collection
tasks.insert({"text":'hello from python2'})
#print(tasks.find_one()['text'])

