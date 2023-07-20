from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    email: str
    name: str

    class Config:
        schema_extra = {
            "example": {
                "email": "user@example.com",
                "name": "John Doe"
            }
        }





'''


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
'''