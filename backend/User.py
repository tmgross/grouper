from pymongo.server_api import ServerApi
import motor.motor_asyncio as motor


class User:
    def __init__(self,email):
        self.email = email
        uri = "mongodb+srv://gavinbuier:IeljglDxt5Gew8U1@userinformation.g0x0e9q.mongodb.net/?retryWrites=true&w=majority"
        client = motor.AsyncIOMotorClient(uri, server_api=ServerApi('1'))
        db = client.GroupWare  
        #accesses the user_information collection    
        collection = db.user_accounts
        document = collection.find_one({"email": email})
        self.name = document["name"]
        self.accountNum = document["_id"]
    
    def getEmail():
        return self.email
    def getName():
        return self.name
    def getAccountNum():
        return self.accountNum
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
    uri = "mongodb+srv://gavinbuier:IeljglDxt5Gew8U1@userinformation.g0x0e9q.mongodb.net/?retryWrites=true&w=majority"
    client = motor.AsyncIOMotorClient(uri, server_api=ServerApi('1'))
    db = client.GroupWare  
    #accesses the user_information collection    
    collection = db.user_accounts
    dict1 = {"email": email ,"name":name}
    result = collection.insert_one(dict1)
    return result.inserted_id