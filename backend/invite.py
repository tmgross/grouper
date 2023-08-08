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
        self.inviteCollection = db.group_invites
        #initialize
        #asyncio.create_task(self.initialize())
        #self.initialize()
        #await self.initialize()
        #asyncio.run(self.initialize())

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
    
    def getGroupName(self):
        return self.fromName
    
    def getToName(self):
        return self.toName
    
    def getToEmail(self):
        return self.toEmail
    
    def getToId(self):
        return self.toId

    def getFromId(self):
        return self.fromId

    async def __deleteInvite(self):
        #inviteCollection = db.group_invites
        result = await self.inviteCollection.delete_one({"fromId": self.fromId,"toEmail":self.toEmail})
        return result.deleted_count
    
    async def addInvite(self):
        #inviteCollection = db.group_invites
        result = await self.inviteCollection.insert_one({"fromId": self.fromId,"toEmail":self.toEmail})
        return str(result.inserted_id)
        
    async def acceptInvite(self):
        collection = db.user_access
        dict = {}
        dict = {"userid":self.toId,"locationid":self.fromId}
        result = await collection.insert_one(dict)
        await self.rejectInvite()
        return result.inserted_id
        
    async def rejectInvite(self):
        print("rejected")
        await self.__deleteInvite()
        return
    
    

    

class FriendInvite(GroupInvite):

    def __init__(self, inviteFromId, toEmail):
        self.toEmail = toEmail
        self.fromId = inviteFromId
        self.inviteCollection = db.friend_invites

    async def initialize(self):
        print("GroupInvite.initialize()")
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


    def getFromName(self):
        return self.fromName
    
    def getFromId(self):
        return super().getFromId()
    
    def getToEmail(self):
        return super().getToEmail()
    
    def getToId(self):
        return super().getToId()
    
    def getToName(self):
        return super().getToName()
    
    def getFromEmail(self):
        return self.fromEmail

    async def __deleteInvite(self):
        return await super().__deleteInvite()

    async def addInvite(self):
        return await super().addInvite()


    async def acceptInvite(self):
        collection = db.friends
        dict = {}
        dict = {"userid":self.toId,"friendid":self.fromId}
        result = await collection.insert_one(dict)
        await self.rejectInvite()
        return result.inserted_id
    
    async def rejectInvite(self):
        return await super().rejectInvite()
    








