from pymongo.server_api import ServerApi
import motor.motor_asyncio as motor


uri = "mongodb+srv://gavinbuier:IeljglDxt5Gew8U1@userinformation.g0x0e9q.mongodb.net/?retryWrites=true&w=majority"
client = motor.AsyncIOMotorClient(uri, server_api=ServerApi('1'))
db = client.GroupWare



# class for users that stores each users information
class User:
    def __init__(self, email):
        self.email = email

        #accesses the user_information collection
        userCollection = db.user_accounts
        document = userCollection.find_one({"email": email})
        self.name = document["name"]
        self.id = document["_id"]

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