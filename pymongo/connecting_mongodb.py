from pymongo import MongoClient

# Connect to a local MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Access a database
db = client["starwars"]

# Access a collection
collection = db["characters"]

print("Connected to MongoDB!")

result = collection.find_one({"name": "Chewbacca"})
print(result)

client.close()