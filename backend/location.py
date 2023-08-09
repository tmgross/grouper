from pymongo.server_api import ServerApi
import motor.motor_asyncio as motor
from bson.objectid import ObjectId
from invite import *
from friendInvite import *
uri = "mongodb+srv://gavinbuier:IeljglDxt5Gew8U1@userinformation.g0x0e9q.mongodb.net/?retryWrites=true&w=majority"
client = motor.AsyncIOMotorClient(uri, server_api=ServerApi('1'))
db = client.GroupWare



class Location:
    def __init__(self,id):
        print(id)
        self.id = str(id)
        self.name= "N/A"
        self.totalUsers = []

    async def initialize(self):
        #accesses the user_information collection
        locoCollection = db.locations
        print("id = ",self.id)
        objInstance = ObjectId(self.id)
        document = await locoCollection.find_one({"_id": objInstance})
        print("Document = {document}")
        if document is not None:
            self.name = str(document["name"])
            self.totalUsers = []
        
    def get_id(self):
        return self.id

    def get_name(self):
        if(self.name is None):
            return "N/A"
        return self.name

    async def get_current_users(self):
        users = []
        cursor = db.user_locations.find(
            {'locationId': self.id},
            
        )
        async for document in cursor:
            if document.get("userName") is not None:
                #print(document["userName"])
                users.append(document["userName"])
        if users:
            return users
        else:
            return [""]