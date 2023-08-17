import motor.motor_asyncio as motor

from objects import *
from invite import *
from friendInvite import *
from location import *

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
    result = await locoCollection.delete_one({"userEmail": user.get_email(),"locationId":location.get_id()})
    return result.deleted_count

# takes in a user
# removes the user from the locations table
# returns the number of rows deleted
async def remove_user_any(user):
    locoCollection = db.user_locations
    result = await locoCollection.delete_one({"userEmail": user.get_email()})
    return result.deleted_count

# takes in a user and a location
# adds the user to the location in the user locations table
# returns the id of the newly created row
async def add_user_to_location(user,location):
    await remove_user_any(user)
    collection = db.user_locations
    dict1 = {}
    dict1 = {"userEmail": user.get_email(),"locationId":str(location.get_id()),"userName":user.get_name(),"userid":user.get_id()}
    result = await collection.insert_one(dict1)
    return str(result.inserted_id)

# takes in a user and a location
# adds that user to the user_access table along with the location
# returns the id of the new row in the table
async def add_user_access(user,location):
    collection = db.user_access
    dict = {}
    dict = {"userid":user.get_id(),"locationid":location.get_id()}
    result = await collection.insert_one(dict)
    return str(result.inserted_id)


# takes in a Id of the group sending the invite and the Email of the user the invite is sent to
#adds an invite into the group_invites table in the database
async def new_group_invite(fromId,toEmail):
    ivt = GroupInvite(fromId,toEmail)
    ivt.add_invite()


async def new_friend_invite(fromId,toEmail):
    ivt = FriendInvite(fromId,toEmail)
    ivt.add_invite()


#returns the location based on id
async def get_location(id):
    loco = Location(str(id))
    await loco.initialize()
    print(loco.get_name())
    return loco

# returns all of the locations in the locations database {id,name}
async def get_all_locations():
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
    locations = accessCollection.find({"userid": user.get_id()})
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