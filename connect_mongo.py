import pymongo
from pymongo import MongoClient
connection = MongoClient('localhost', 3001)
db = connection.meteor
tasks = db.tasks
tasks.insert({"text":'hello from python2'})
#print(tasks.find_one()['text'])

