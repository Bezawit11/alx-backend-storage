from pymongo import MongoClient 
 
client = MongoClient() 
db = client.logs
 
# print collection statistics 
# events is the collection name here 
print db.command("collstats", "nginx") 

 
# print database statistics 
print db.command("dbstats")
