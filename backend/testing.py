import database
import asyncio
from objects import User
from objects import Location
from invite import GroupInvite
from invite import FriendInvite

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


def testAddUserAccess(email,id):
    loop = asyncio.get_event_loop()
    try:
        loco =Location(id)
        val = loop.run_until_complete(loco.getCurrentUsers())
        for l in val:
            print(l)
    finally:
        loop.close()


def testLocoFilter(email):
    loop = asyncio.get_event_loop()
    try:
        user = loop.run_until_complete(database.log_in_user(email))
        locos = loop.run_until_complete(database.get_all_locations(user))
        print(locos)
    finally:
        loop.close()

def testInvite(fromId, toEmail):
    loop = asyncio.get_event_loop()
    try:
        ivt = GroupInvite(toEmail=toEmail,inviteFromId=fromId)
        loop.run_until_complete(ivt.initialize())
        user = loop.run_until_complete(ivt.addInvite())
        #locos = loop.run_until_complete(database.get_all_locations(user))
        print(user)
        print(ivt.getGroupName())
        result = loop.run_until_complete(ivt.acceptInvite())
        print(result)
    finally:
        loop.close()

def testGetAllInvites(userEmail):
    loop = asyncio.get_event_loop()
    try:
        ivt = GroupInvite(toEmail=userEmail,inviteFromId="64bee34b6fa3a8c31741b6b0")
        #loop.run_until_complete(ivt.initialize())
        user = loop.run_until_complete(ivt.addInvite())
        #print(user)
        ivts = loop.run_until_complete(database.get_all_group_invites(userEmail))
        #locos = loop.run_until_complete(database.get_all_locations(user))
        for i in ivts:
            print("location name: ",i.getGroupName())
    finally:
        loop.close()



def testFriendInvite(fromId,toEmail):
    loop = asyncio.get_event_loop()
    try:
        ivt = FriendInvite(toEmail=toEmail,inviteFromId=fromId)
        loop.run_until_complete(ivt.initialize())
        user = loop.run_until_complete(ivt.addInvite())
        #locos = loop.run_until_complete(database.get_all_locations(user))
        print(user)
        print(ivt.getFromName())
        print(ivt.getToName())
        result = loop.run_until_complete(ivt.acceptInvite())
        print(result)
    finally:
        loop.close()

#remove_test("test@test.com","64bee34b6fa3a8c31741b6b0")
#auto_logout("test@test.com")
#testLocoFilter("1234@321")
#testInvite("64bee34b6fa3a8c31741b6b0","test@test.com")
#testGetAllInvites("test@test.com")
testFriendInvite("64b98136ee31d004275ff579","test@test.com")
#login_test("test@test.com")
#testLocoUsers("64b6bfbb54263d417e25e9d1")
#testLoco2()
#remove_test("test@main.com","64b6bfbb54263d417e25e9d1")