import database
import asyncio
from objects import User
from objects import Location

def add_test(name):
    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(database.create_user(name))
    #loop.close()
    loop = asyncio.get_event_loop()
    try:
        user = loop.run_until_complete(database.create_user(name))
        assert(user!=None)
    finally:
        loop.close()
    #asyncio.run(database.create_user(name))

    #nm = database.create_user(name)
    #assert(nm == name)


def remove_test(name):
    #add_test(name)
    #asyncio.run(database.create_user(name))
    #users = database.fetch_one_user(name)
    #assert(len(users)>0)

    loop = asyncio.get_event_loop()
    try:
        userid = loop.run_until_complete(database.create_user(name))
        print(userid)
        assert(userid!=None)
        loop.run_until_complete(database.remove_user(name))
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




#login_test("test@test.com")
#testLocationGet("64b6bfbb54263d417e25e9d1")
testLoco2()