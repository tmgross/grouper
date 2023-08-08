from pymongo.server_api import ServerApi
import motor.motor_asyncio as motor
from bson.objectid import ObjectId
import asyncio

uri = "mongodb+srv://gavinbuier:IeljglDxt5Gew8U1@userinformation.g0x0e9q.mongodb.net/?retryWrites=true&w=majority"
client = motor.AsyncIOMotorClient(uri, server_api=ServerApi('1'))
db = client.GroupWare



class GroupInvite:

    def __init__(self,  inviteFromId, toEmail):
        self.toEmail = toEmail
        self.fromId = inviteFromId
        #stores which collection to store the invite in
        self.inviteCollection = db.group_invites

    # pulls the needed data from the database
    async def initialize(self):
        print("GroupInvite.initialize()")
        # accesses the user_information collection
        userCollection = db.locations
        print(self.fromId)
        print(self.toEmail)
        document = await userCollection.find_one({"_id": ObjectId(self.fromId)})
        self.fromName = str(document["name"])
        userCollection = db.user_accounts
        document = await userCollection.find_one({"email": self.toEmail})
        self.toName = str(document["name"])
        self.toId = str(document["_id"])
    
    def get_group_name(self):
        return self.fromName
    
    def get_to_name(self):
        return self.toName
    
    def get_to_email(self):
        return self.toEmail
    
    def get_to_id(self):
        return self.toId

    def get_from_id(self):
        return self.fromId

    # deletes the invite to the respective invite table (friends to friendInvite, group for GroupInvites)
    #returns the number of rows deleted
    async def __delete_invite(self):
        #inviteCollection = db.group_invites
        result = await self.inviteCollection.delete_one({"fromId": self.fromId,"toEmail":self.toEmail})
        return result.deleted_count
    
    # adds the invite to the respective invite table (friends to friendInvite, group for GroupInvites)
    #returns the Id of the new row in the table
    async def add_invite(self):
        result = await self.inviteCollection.insert_one({"fromId": self.fromId,"toEmail":self.toEmail})
        return str(result.inserted_id)
        
    # accepts the invite
    # adds the user to the user_access tabel
    # removes the invite from its table
    async def accept_invite(self):
        collection = db.user_access
        dict = {}
        dict = {"userid":self.toId,"locationid":self.fromId}
        result = await collection.insert_one(dict)
        await self.__delete_invite()
        return result.inserted_id
        
    # calls the delete invite function could be expanded for messaging later
    async def reject_invite(self):
        print("rejected")
        await self.__delete_invite()
        return
    
    

    

class FriendInvite(GroupInvite):

    def __init__(self, inviteFromId, toEmail):
        self.toEmail = toEmail
        self.fromId = inviteFromId
        #stores which collection to store the invite in
        self.inviteCollection = db.friend_invites

    #pulls the needed data for the object from the database
    async def initialize(self):
        print("FriendInvite.initialize()")
        # accesses the user_information collection
        userCollection = db.user_accounts
        print(self.fromId)
        print(self.toEmail)
        document = await userCollection.find_one({"_id": ObjectId(self.fromId)})
        self.fromName = str(document["name"])
        self.fromEmail = str(document["email"])
        document = await userCollection.find_one({"email": self.toEmail})
        self.toName = str(document["name"])
        self.toId = str(document["_id"])


    def get_from_name(self):
        return self.fromName
    
    def get_from_id(self):
        return super().get_from_id()
    
    def get_to_email(self):
        return super().get_to_email()
    
    def get_to_id(self):
        return super().get_to_id()
    
    def get_to_name(self):
        return super().get_to_name()
    
    def get_from_email(self):
        return self.fromEmail

    async def __delete_invite(self):
        return await super()._GroupInvite__delete_invite()

    async def add_invite(self):
        return await super().add_invite()

    #adds the two users as friend and deletes the invite
    # returns an array of size 2 for each of the new ids in the friends table
    async def accept_invite(self):
        results = []
        collection = db.friends
        dict = {}
        dict = {"userid":self.toId,"friendid":self.fromId}
        result = await collection.insert_one(dict)
        results.append(str(result))
        dict2 = {}
        dict2 = {"userid":self.fromId,"friendid":self.toId}
        result = await collection.insert_one(dict2)
        results.append(str(result))
        await self.__delete_invite()
        return results
    
    async def reject_invite(self):
        return await super().reject_invite()
    








