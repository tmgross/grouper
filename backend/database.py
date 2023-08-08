import motor.motor_asyncio as motor

from objects import *
from invite import *

#connection string.
uri = "mongodb+srv://gavinbuier:IeljglDxt5Gew8U1@userinformation.g0x0e9q.mongodb.net/?retryWrites=true&w=majority"
client = motor.AsyncIOMotorClient(uri)
db = client.GroupWare


async def create_new_user(email, name):
    #accesses the user_information collection
    userCollection = db.user_accounts
    dict1 = {"email": email ,"name": name}
    try:
        result = await userCollection.insert_one(dict1)
        print(result)
        return str(result.inserted_id)
    except Exception as e:
        print("Error occurred while creating user:", e)
        return None


async def log_in_user(email):
    try:
        user = User(email)
        await user.initialize()
        return user
    except Exception as e:
        print("Error occurred while logging in:", e)
        return None


async def create_new_group(group):
    #accesses the user_information collection
    locoCollection = db.locations
    dict1 = {"name": group}
    try:
        result = await locoCollection.insert_one(dict1)
        print(result)
        return str(result.inserted_id)
    except Exception as e:
        print("Error occurred while creating group:", e)
        return None

async def removeUser(user,location):
    locoCollection = db.user_locations
    result = await locoCollection.delete_one({"userEmail": user.getEmail(),"locationId":location.getId()})
    return result.deleted_count


async def remove_user_any(user):
    locoCollection = db.user_locations
    result = await locoCollection.delete_one({"userEmail": user.getEmail()})
    return result.deleted_count


async def addUserToLocation(user,location):
    await remove_user_any(user)
    collection = db.user_locations
    dict1 = {}
    dict1 = {"userEmail": user.getEmail(),"locationId":str(location.getId()),"userName":user.getName()}
    result = await collection.insert_one(dict1)
    return result.inserted_id

async def add_user_access(user,location):
    collection = db.user_access
    dict = {}
    dict = {"userid":user.getId(),"locationid":location.getId()}
    result = await collection.insert_one(dict)
    return result.inserted_id

async def new_group_invite(toEmail,fromId):
    ivt = GroupInvite(fromId,toEmail)
    ivt.addInvite()

async def get_all_group_invites(userEmail):
    invites = []
    collection = db.group_invites
    cursor = collection.find({"toEmail":userEmail})
    async for document in cursor:
            print("ran")
            ivt= GroupInvite(document["fromId"],document["toEmail"])
            await ivt.initialize()
            invites.append(ivt)
    return invites


async def get_all_friend_invites(userEmail):
    invites = []
    collection = db.friend_invites
    cursor = collection.find({"toEmail":userEmail})
    async for document in cursor:
            print("ran")
            ivt= FriendInvite(document["fromId"],document["toEmail"])
            await ivt.initialize()
            invites.append(ivt)
    return invites

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




async def get_all_locations(user):
    accessCollection = db.user_access
    #objid = ObjectId(user.getId())
    locations = accessCollection.find({"userid": user.getId()})
    accessable = [ObjectId(l["locationid"]) async for l in locations]
    locoCollection = db.locations
    filter = {"_id": { '$in': accessable }}
    print(filter)
    cursor = locoCollection.find(filter)
    print(cursor)
    locos = {}
    async for document in cursor:
            print(document)
            if document.get("name") is not None:
                locos[str(document["_id"])]=document["name"]
                print(document["name"])
    #for d in locos.keys():
    #     print("id = ",d)
    return locos