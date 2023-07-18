import database
import asyncio


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


remove_test("Bob Bob")