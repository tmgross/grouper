from pymongo.server_api import ServerApi
import motor.motor_asyncio as motor


uri = "mongodb+srv://gavinbuier:IeljglDxt5Gew8U1@userinformation.g0x0e9q.mongodb.net/?retryWrites=true&w=majority"
client = motor.AsyncIOMotorClient(uri, server_api=ServerApi('1'))
db = client.GroupWare  




# class for users that stores each users information
class User:
    def __init__(self,email):
        self.email = email
        #uri = "mongodb+srv://gavinbuier:IeljglDxt5Gew8U1@userinformation.g0x0e9q.mongodb.net/?retryWrites=true&w=majority"
        #client = motor.AsyncIOMotorClient(uri, server_api=ServerApi('1'))
        #db = client.GroupWare  

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
    

# Creates new user account in the database
# Takes a name and email as parameters
# returns the id of the new user
def createNewUser(email,name):
    #uri = "mongodb+srv://gavinbuier:IeljglDxt5Gew8U1@userinformation.g0x0e9q.mongodb.net/?retryWrites=true&w=majority"
    #client = motor.AsyncIOMotorClient(uri, server_api=ServerApi('1'))
    #db = client.GroupWare  
    #accesses the user_information collection    
    userCollection = db.user_accounts
    dict1 = {"email": email ,"name":name}
    result = userCollection.insert_one(dict1)
    return result.inserted_id



#object for a location
class Location:
    def __init__(self,id):
        self.id = id
        uri = "mongodb+srv://gavinbuier:IeljglDxt5Gew8U1@userinformation.g0x0e9q.mongodb.net/?retryWrites=true&w=majority"
        client = motor.AsyncIOMotorClient(uri, server_api=ServerApi('1'))
        db = client.GroupWare  
        #accesses the user_information collection    
        locoCollection = db.locations
        document = locoCollection.find_one({"_id": id})
        self.name = document["name"]
        self.totalUsers = []
    
    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getCurrentUsers(self):
        cursor = db.user_locations.find({'location': self.id},{'name':1,'_id':0,'location':0})
        return cursor
    
    def getTotalUsers(self):
        return self.totalUsers
 