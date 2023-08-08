import motor.motor_asyncio as motor

from objects import *
from invite import *

#connection string.
uri = "mongodb+srv://gavinbuier:IeljglDxt5Gew8U1@userinformation.g0x0e9q.mongodb.net/?retryWrites=true&w=majority"
client = motor.AsyncIOMotorClient(uri)
db = client.GroupWare

# takes an email and name of a user
# inserts the information into the user accounts table
# returns the row id of the new row if successful
# throws an error if it failed
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

# takes in the users email
# creates a user object for that user
# returns the user object if successful else it throws an error
async def log_in_user(email):
    try:
        user = User(email)
        await user.initialize()
        return user
    except Exception as e:
        print("Error occurred while logging in:", e)
        return None

# takes the name of the new group
# inserts the name into to locations table
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

async def remove_user(user,location):
    locoCollection = db.user_locations
    result = await locoCollection.delete_one({"userEmail": user.getEmail(),"locationId":location.getId()})
    return result.deleted_count

# takes in a user
# removes the user from the locations table
# returns the number of rows deleted
async def remove_user_any(user):
    locoCollection = db.user_locations
    result = await locoCollection.delete_one({"userEmail": user.getEmail()})
    return result.deleted_count

# takes in a user and a location
# adds the user to the location in the user locations table
# returns the id of the newly created row
async def add_user_to_location(user,location):
    await remove_user_any(user)
    collection = db.user_locations
    dict1 = {}
    dict1 = {"userEmail": user.getEmail(),"locationId":str(location.getId()),"userName":user.getName(),"userid":user.getId()}
    result = await collection.insert_one(dict1)
    return str(result.inserted_id)

# takes in a user and a location
# adds that user to the user_access table along with the location
# returns the id of the new row in the table
async def add_user_access(user,location):
    collection = db.user_access
    dict = {}
    dict = {"userid":user.getId(),"locationid":location.getId()}
    result = await collection.insert_one(dict)
    return str(result.inserted_id)


# takes in a Id of the group sending the invite and the Email of the user the invite is sent to
#adds an invite into the group_invites table in the database
async def new_group_invite(fromId,toEmail):
    ivt = GroupInvite(fromId,toEmail)
    ivt.addInvite()


#takes in the current users email
# gets all of the group invite objects that that user has in an array
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

#takes in the email of the current user
# returns a list of all of the friend invite objects the user has
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


# takes the id of the user
# gets ids of all of thier friends
# uses those ids and the user_accounts table to get the info for each friend
async def get_all_friends(userId):
    friendIds = []
    collection = db.friends
    cursor = collection.find({"userid":userId})
    async for document in cursor:
            #print("ran")
            friendIds.append(ObjectId(document["friendid"]))
    filter = {"_id": { '$in': friendIds }}
    users = db.user_accounts
    cursor = users.find(filter)
    friendNames = []
    async for document in cursor:
            print(document)
            if document.get("name") is not None:
                friendNames.append(document["name"])
                print(document["name"])
    return friendNames

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
async def get_location(id):
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



# takes in a user object
# finds all locations that that user has access to 
# returns a dictionary of those locatios with id as the key and name as the value
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