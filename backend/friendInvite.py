from pymongo.server_api import ServerApi
import motor.motor_asyncio as motor
from bson.objectid import ObjectId
import asyncio
from invite import *

uri = "mongodb+srv://gavinbuier:IeljglDxt5Gew8U1@userinformation.g0x0e9q.mongodb.net/?retryWrites=true&w=majority"
client = motor.AsyncIOMotorClient(uri, server_api=ServerApi('1'))
db = client.GroupWare



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
    
