import database
import asyncio
from objects import User
from objects import Location

def add_test(email, locoid):
    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(database.create_user(name))
    #loop.close()
    #loco.initialize()
    #user.initialize()
    loop = asyncio.get_event_loop()
    loco = loop.run_until_complete(database.getLocation(locoid))
    user = loop.run_until_complete(database.log_in_user(email))
    try:
        newid = loop.run_until_complete(database.addUserToLocation(user=user,location=loco))
        print(newid)
        #assert(user!=None)
    finally:
        loop.close()
    #asyncio.run(database.create_user(name))

    #nm = database.create_user(name)
    #assert(nm == name)


def remove_test(email, locoid):
    #add_test(name)
    #asyncio.run(database.create_user(name))
    #users = database.fetch_one_user(name)
    #assert(len(users)>0)

    loop = asyncio.get_event_loop()
    loco = loop.run_until_complete(database.getLocation(locoid))
    user = loop.run_until_complete(database.log_in_user(email))
    try:
        loop.run_until_complete(database.removeUser(user,loco))
    finally:
        loop.close()
    #asyncio.run(database.remove_user(name))
    #users = database.fetch_one_user(name)
    #assert(len(users)==0)


def login_test(email):
    loop = asyncio.get_event_loop()
    try:
        user = loop.run_until_complete(database.log_in_user(email))
        print(user.getName())
        print(user.getId())
        assert(user!=None)
    finally:
        loop.close()

def auto_logout(email):
    loop = asyncio.get_event_loop()
    try:
        user = loop.run_until_complete(database.log_in_user(email))
        dele = loop.run_until_complete(database.removeUserAny(user))
        print(dele)
        print(user.getName())
        print(user.getId())
        assert(user!=None)
    finally:
        loop.close()



def getLocos():
    loop = asyncio.get_event_loop()
    try:
        locos = loop.run_until_complete(database.getAllLocations())
        assert(locos!=None)
        print(locos)
        #for i in locos:
        #    print(i)
    finally:
        loop.close()


def testLocationGet(id):
    loop = asyncio.get_event_loop()
    try:
        locos = loop.run_until_complete(database.getLocation(id))
        assert(locos!=None)
        print(locos.getName())
        #for i in locos:
        #    print(i)
    finally:
        loop.close()


def testLoco2():
    loop = asyncio.get_event_loop()
    try:
        locos = loop.run_until_complete(database.getAllLocations())
        for l in locos.keys():
            val = loop.run_until_complete(database.getLocation(l))
            #print("123")
            print(val.getId())
            print(val.getName())
    finally:
        loop.close()

def testLocoUsers(id):
    loop = asyncio.get_event_loop()
    try:
        loco =Location(id)
        val = loop.run_until_complete(loco.getCurrentUsers())
        for l in val:
            print(l)
    finally:
        loop.close()



#remove_test("test@test.com","64bee34b6fa3a8c31741b6b0")
auto_logout("test@test.com")



#login_test("test@test.com")
#testLocoUsers("64b6bfbb54263d417e25e9d1")
#testLoco2()
#remove_test("test@main.com","64b6bfbb54263d417e25e9d1")