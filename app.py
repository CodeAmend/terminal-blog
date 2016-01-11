import pymongo

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['fullstack']
collection = database['students']

studentList = [stud['name'] for stud in collection.find({})]

print(studentList)