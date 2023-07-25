from pymongo.server_api import ServerApi
import motor.motor_asyncio as motor
from bson.objectid import ObjectId

uri = "mongodb+srv://gavinbuier:IeljglDxt5Gew8U1@userinformation.g0x0e9q.mongodb.net/?retryWrites=true&w=majority"
client = motor.AsyncIOMotorClient(uri, server_api=ServerApi('1'))
db = client.GroupWare



# class for users that stores each users information
class User:
    def __init__(self, email):
        self.email = email
        self.name = ""
        self.id = None

        #accesses the user_information collection

        #userCollection = db.user_accounts
        #document = userCollection.find_one({"email": email})
        #self.name = document["name"]
        #self.id = document["_id"]


    async def initialize(self):
        # accesses the user_information collection
        userCollection = db.user_accounts
        document = await userCollection.find_one({"email": self.email})
        self.name = str(document["name"])
        self.id = str(document["_id"])

    def getEmail(self):
        return self.email
    def getName(self):
        return self.name
    def getId(self):
        return self.id
    def getInvites():
        return
    def getFriends():
        return
    def getLocations():
        return
    def getFriendRequests():
        return
    


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
        
    def getId(self):
        return self.id

    def getName(self):
        if(self.name is None):
            return "N/A"
        return self.name

    async def getCurrentUsers(self):
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

    def getTotalUsers(self):
        return self.totalUsers