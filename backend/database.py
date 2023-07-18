import motor.motor_asyncio as motor
from models import User

#connection string: mongodb+srv://gavinbuier:<password>@userinformation.g0x0e9q.mongodb.net/
#Database = GroupWare
#collection = user_information
from pymongo.server_api import ServerApi
#connection string.
uri = "mongodb+srv://gavinbuier:IeljglDxt5Gew8U1@userinformation.g0x0e9q.mongodb.net/?retryWrites=true&w=majority"
client = motor.AsyncIOMotorClient(uri, server_api=ServerApi('1'))

#from pymongo import MongoClient

#uri = "mongodb+srv://gavinbuier:IeljglDxt5Gew8U1@userinformation.g0x0e9q.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
#client = MongoClient(uri, server_api=ServerApi('1'))




#accesses the GroupWare database
db = client.GroupWare  
#accesses the user_information collection    
collection = db.user_information


#finds all people with the given name in the user_information database
#input: the name of the person we want to find
#returns: a list of the information of those who meet the criteria of the input
async def fetch_one_user(name):
    document = await collection.find_one({"name": name})
    return document



#finds all people in the user_information database
#input: n/a
#returns: a list of the information of all users
async def fetch_all_users():
    users = []
    cursor = collection.find()
    async for document in cursor:
        users.append(Users(**document))
    return users



'''
#finds all people at the given location user_information database
#input: the location of the people we want to find
#returns: a list of the information of those who meet the criteria of the input
def getPeople(loco):
    # find code goes here
    cursor = collection.find({"location": loco})
    
    data =[]
    # iterate code goes here
    for doc in cursor:
        data.append(doc)
        print(doc)
        
    print(len(data))
    return data
'''


#adds a person to the database
#input: the name of the person we want to add
#returns: the id of the person we just added
async def create_user(user):
    dict1 = {}
    document = user
    dict1 = {"name": document,"location":1}
	    
    
    result = await collection.insert_one(dict1)
    return result.inserted_id



#removes all people with a given name from the database
#input: the name of the person/people we want to remove
#returns: the number of people deleted
async def remove_user(name):
    result = await collection.delete_one({"name": name})
    

