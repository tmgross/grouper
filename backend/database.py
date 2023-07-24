import motor.motor_asyncio as motor
from pymongo.server_api import ServerApi

from objects import User
from objects import Location

#connection string.
uri = "mongodb+srv://gavinbuier:IeljglDxt5Gew8U1@userinformation.g0x0e9q.mongodb.net/?retryWrites=true&w=majority"
client = motor.AsyncIOMotorClient(uri, server_api=ServerApi('1'))
#accesses the GroupWare database
db = client.GroupWare
#accesses the user_information collection
collection = db.user_accounts



async def create_new_user(email, name):
    #accesses the user_information collection
    userCollection = db.user_accounts
    dict1 = {"email": email ,"name": name}
    result = await userCollection.insert_one(dict1)
    print(result)
    return result.inserted_id


async def log_in_user(email):
    user = User(email)
    await user.initialize()
    return user



'''
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

'''
# adds a person to a location in user locations
# input: the name of the person we want to add
# returns: the id of the person we just added
async def addUserToLocation(user,locationid):
    dict1 = {}
    document = user
    dict1 = {"name": document.getName(),"location":locationid,"userid":document.getId()}
    result = await collection.insert_one(dict1)
    return result.inserted_id



#removes all people with a given name from the database
#input: the name of the person/people we want to remove
#returns: the number of people deleted
async def remove_user(user):
    result = await collection.delete_one({"userid": user.getId()})


# adds a new location to the locations table
async def createNewLocation(name):
    locoCollection = db.locations
    dict1 = {"name":name}
    result = await locoCollection.insert_one(dict1)
    return result.inserted_id
'''
#returns the location based on id
async def getLocation(id):
    loco = Location(str(id))
    await loco.initialize()
    print(loco.getName())
    return loco

# returns all of the locations in the locations database {id,name}
async def getAllLocations():
    locoCollection = db.locations
    cursor = locoCollection.find()
    locos = {}
    async for document in cursor:
            if document.get("name") is not None:
                locos[str(document["_id"])]=document["name"]
                print(document["name"])
    #for d in locos.keys():
    #     print("id = ",d)
    return locos

