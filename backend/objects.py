from pymongo.server_api import ServerApi
import motor.motor_asyncio as motor
from bson.objectid import ObjectId
from invite import *
from friendInvite import *
uri = "mongodb+srv://gavinbuier:IeljglDxt5Gew8U1@userinformation.g0x0e9q.mongodb.net/?retryWrites=true&w=majority"
client = motor.AsyncIOMotorClient(uri, server_api=ServerApi('1'))
db = client.GroupWare


# class for users that stores each users information
class User:
    def __init__(self, email):
        self.email = email
        self.name = ""
        self.id = None

    # initializes the users data from the database
    async def initialize(self):
        print("objects.py User.initialize()")
        # accesses the user_information collection
        userCollection = db.user_accounts
        document = await userCollection.find_one({"email": self.email})
        self.name = str(document["name"])
        self.id = str(document["_id"])

    #returns the users email
    def get_email(self):
        return self.email
    
    #returns the users name
    def get_name(self):
        return self.name
    
    #returns the usrs id
    def get_id(self):
        return self.id
    
    # takes in the current users email
    # gets all of the group invite objects that that user has in an array
    async def get_group_invites(self):
        invites = []
        collection = db.group_invites
        cursor = collection.find({"toEmail":self.email})
        async for document in cursor:
            print("ran")
            ivt= GroupInvite(document["fromId"],document["toEmail"])
            await ivt.initialize()
            invites.append(ivt)
        return invites
    
    #takes in the email of the current user
    # returns a list of all of the friend invite objects the user has
    async def get_friend_invites(self):
        invites = []
        collection = db.friend_invites
        cursor = collection.find({"toEmail":self.email})
        async for document in cursor:
            print("ran")
            ivt= FriendInvite(document["fromId"],document["toEmail"])
            await ivt.initialize()
            invites.append(ivt)
        return invites
    

    # takes the id of the user
    # gets ids of all of thier friends
    # uses those ids and the user_accounts table to get the info for each friend
    async def get_friends(self):
        friendIds = []
        collection = db.friends
        cursor = collection.find({"userid":self.id})
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
    
    #gets the locations the user has access to
    async def get_locations(self):
        accessCollection = db.user_access
        locations = accessCollection.find({"userid": self.id})
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
        return locos
    
    

