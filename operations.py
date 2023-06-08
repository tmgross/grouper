from pymongo import MongoClient

#connection string: mongodb+srv://gavinbuier:<password>@userinformation.g0x0e9q.mongodb.net/
#Database = GroupWare
#Collection = user_information


#finds all people with the given name
def findPerson(name):
        # Replace the uri string with your MongoDB deployment's connection string.
    uri = "mongodb+srv://<user>:<password>@<cluster-url>?retryWrites=true&writeConcern=majority"
    client = MongoClient(uri)
    # database and collection code goes here
    db = client.sample_guides
    coll = db.planets
    # find code goes here
    cursor = coll.find({"Name": name})
    # iterate code goes here
    for doc in cursor:
        print(doc)
    # Close the connection to MongoDB when you're done.
    client.close()





#adds a person to the database
def addPerson(name):
    # Replace the uri string with your MongoDB deployment's connection string.
    #uri = "mongodb+srv://<user>:<password>@<cluster-url>?retryWrites=true&writeConcern=majority"
    uri = "mongodb+srv://gavinbuier:IeljglDxt5Gew8U1@userinformation.g0x0e9q.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    # database and collection code goes here
    db = client.GroupWare
    coll = db.user_information
    coll.drop()
    # insert code goes here
    docs = [
	    {"Name": name,},
	    
    ]
    result = coll.insert_many(docs)
    # display the results of your operation
    print(result.inserted_ids)
    # Close the connection to MongoDB when you're done.
    client.close()
    return




#removes a person from the database
def removePerson(name):
    # Replace the uri string with your MongoDB deployment's connection string.
    uri = uri = "mongodb+srv://gavinbuier:IeljglDxt5Gew8U1@userinformation.g0x0e9q.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    db = client.GroupWare      #client.sample_guides (sample guides is the name of the db)
    coll = db.user_information     #db.comets (comets is the name of the collection)
    # delete code goes here
    doc = {
    "name": {
        "$eq": name,
        }
    }
    result = coll.delete_many(doc)
    # amount deleted code goes here
    print("Number of documents deleted: ", result.deleted_count)
    # Close the connection to MongoDB when you're done.
    client.close()
    return result.deleted_count



def main():
    uri = "mongodb+srv://gavinbuier:IeljglDxt5Gew8U1@userinformation.g0x0e9q.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    # database and collection code goes here
    db = client.sample_guides