from pymongo.server_api import ServerApi
import motor.motor_asyncio as motor



#object for a location
class Location:
    def __init__(self,id):
        self.id = id
        uri = "mongodb+srv://gavinbuier:IeljglDxt5Gew8U1@userinformation.g0x0e9q.mongodb.net/?retryWrites=true&w=majority"
        client = motor.AsyncIOMotorClient(uri, server_api=ServerApi('1'))
        db = client.GroupWare  
        #accesses the user_information collection    
        collection = db.locations
        document = collection.find_one({"_id": id})
        self.name = document["name"]
        self.totalUsers = []
    
    def getId():
        return self.id
    def getName():
        return self.name
    def getCurrentUsers():
        return
    def getTotalUsers():
        return self.totalUsers
    