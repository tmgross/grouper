from pymongo import MongoClient

#connection string: mongodb+srv://gavinbuier:<password>@userinformation.g0x0e9q.mongodb.net/
#Database = GroupWare
#Collection = user_information


#finds all people with the given name in the user_information database
#input: the name of the person we want to find
#returns: a list of the information of those who meet the criteria of the input
def findPerson(name):
    #connection string.
    #uri = "mongodb+srv://gavinbuier:IeljglDxt5Gew8U1@userinformation.g0x0e9q.mongodb.net/?retryWrites=true&w=majority"
    #uri = "mongodb+srv://gavinbuier:<IeljglDxt5Gew8U1>@userinformation.g0x0e9q.mongodb.net/"
    #client = MongoClient(uri)
    from pymongo.server_api import ServerApi
    uri = "mongodb+srv://gavinbuier:IeljglDxt5Gew8U1@userinformation.g0x0e9q.mongodb.net/?retryWrites=true&w=majority"
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    #accesses the GroupWare database
    db = client.GroupWare  
    #accesses the user_information collection    
    coll = db.user_information
    # find code goes here
    cursor = coll.find({"name": name})
    
    data =[]
    # iterate code goes here
    for doc in cursor:
        data.append(doc)
        print(doc)
        
    # Close the connection to MongoDB when you're done.
    client.close()
    print(len(data))
    return data


#finds all people at the given location user_information database
#input: the location of the people we want to find
#returns: a list of the information of those who meet the criteria of the input
def getPeople(loco):
    #connection string.
    uri = "mongodb+srv://gavinbuier:IeljglDxt5Gew8U1@userinformation.g0x0e9q.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    #accesses the GroupWare database
    db = client.GroupWare  
    #accesses the user_information collection    
    coll = db.user_information
    # find code goes here
    cursor = coll.find({"location": loco})
    
    data =[]
    # iterate code goes here
    for doc in cursor:
        data.append(doc)
        print(doc)
        
    # Close the connection to MongoDB when you're done.
    client.close()
    print(len(data))
    return data





#adds a person to the database
#input: the name of the person we want to add
#returns: the id of the person we just added
def addPerson(name):
    print("Started add")
    #connection string.
    uri = "mongodb+srv://gavinbuier:IeljglDxt5Gew8U1@userinformation.g0x0e9q.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    #accesses the GroupWare database
    db = client.GroupWare  
    #accesses the user_information collection    
    coll = db.user_information 
    coll.drop()
    # insert code goes here
    docs = [
	    {"name": name,},
        {"location":1}
	    
    ]
    result = coll.insert_many(docs)
    # display the results of your operation
    print(result.inserted_ids)
    # Close the connection to MongoDB when you're done.
    client.close()
    print("add Done")
    return result.InsertOneResult




#removes all people with a given name from the database
#input: the name of the person/people we want to remove
#returns: the number of people deleted
def removePerson(name):
    #connection string.
    uri = "mongodb+srv://gavinbuier:IeljglDxt5Gew8U1@userinformation.g0x0e9q.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    #accesses the GroupWare database
    db = client.GroupWare  
    #accesses the user_information collection    
    coll = db.user_information    
    # delete code
    doc = {
    "name": {
        "$eq": name,
        }
    }
    result = coll.delete_many(doc)
    # amount deleted code goes here
    print("Number of documents deleted: ", result.deleted_count)
    # Close the connection to MongoDB
    client.close()
    return result.deleted_count



