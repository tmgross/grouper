import database
import asyncio
from objects import User
from location import *
from invite import GroupInvite
from friendInvite import FriendInvite

#this is a file for testing different operations


# testing adding a user to a location
def add_test(email, locoid):
    print("Testing adding a user to a location:")
    loop = asyncio.get_event_loop()
    loco = loop.run_until_complete(database.get_location(locoid))
    user = loop.run_until_complete(database.log_in_user(email))
    try:
        newid = loop.run_until_complete(database.add_user_to_location(user=user,location=loco))
        print(newid)
        assert(newid!=None)
    finally:
        loop.close()


# testing removing a user from a location
def remove_test(email, locoid):
    print("Testing removing a user from a location:")
    loop = asyncio.get_event_loop()
    loco = loop.run_until_complete(database.get_location(locoid))
    user = loop.run_until_complete(database.log_in_user(email))
    try:
        loop.run_until_complete(database.remove_user(user,loco))
    finally:
        loop.close()


#testing logging in a user
def login_test(email):
    print("Testing logging in a user:")
    loop = asyncio.get_event_loop()
    try:
        user = loop.run_until_complete(database.log_in_user(email))
        assert(user!=None)
        assert(user.get_name()!=None)
        assert(user.get_id()!=None)
        assert(user.get_email()==email)
    finally:
        loop.close()

# test removing a user from all locations they are at 
def auto_logout(email):
    print("Testing removal of a user from any location:")
    loop = asyncio.get_event_loop()
    try:
        user = loop.run_until_complete(database.log_in_user(email))
        dele = loop.run_until_complete(database.remove_user_any(user))
        print(dele)
        print(user.get_name())
        print(user.get_id())
        assert(user!=None)
        assert(user.get_name()!=None)
        assert(user.get_id()!=None)
        assert(user.get_email()==email)
        assert(dele>=0)
    finally:
        loop.close()


# testing getting every location 
def get_locos():
    print("Testing getting every location:")
    loop = asyncio.get_event_loop()
    try:
        locos = loop.run_until_complete(database.get_all_locations())
        assert(locos!=None)
        print(locos)
    finally:
        loop.close()

# testing getting a single location
def test_location_get(id):
    print("Testing getting a single location:")
    loop = asyncio.get_event_loop()
    try:
        locos = loop.run_until_complete(database.get_location(id))
        assert(locos!=None)
        print(locos.get_name())
        #for i in locos:
        #    print(i)
    finally:
        loop.close()

# testing getting all locations and then checking all locations
def test_loco2():
    print("Testing getting and checking every location:")
    loop = asyncio.get_event_loop()
    try:
        locos = loop.run_until_complete(database.get_all_locations())
        for l in locos.keys():
            val = loop.run_until_complete(database.get_location(l))
            assert(val!=None)
            assert(val.get_id()!=None)
            assert(val.get_name()!=None)
            print(val.get_id())
            print(val.get_name())
    finally:
        loop.close()

# testing getting the current users on a location
def test_loco_users(id):
    print("Testing getting all users at a location:")
    loop = asyncio.get_event_loop()
    try:
        loco =Location(id)
        val = loop.run_until_complete(loco.get_current_users())
        for l in val:
            assert(l!=None)
            print("user name: ",l)
    finally:
        loop.close()

#test giving a user access to a location
def test_add_user_access(email,id):
    print("Testing adding user access:")
    loop = asyncio.get_event_loop()
    try:
        loco =Location(id)
        user = loop.run_until_complete(database.log_in_user(email))
        val = loop.run_until_complete(database.add_user_access(user,loco))
        assert(val!=None)
        print(val)
    finally:
        loop.close()

# test the location filter for users view
def test_loco_filter(email):
    print("Testing location filter:")
    loop = asyncio.get_event_loop()
    try:
        user = loop.run_until_complete(database.log_in_user(email))
        locos = loop.run_until_complete(database.get_all_locations(user))
        assert(locos!=None)
        print(locos)
    finally:
        loop.close()

# test sending a group invite
def test_invite(fromId, toEmail):
    print("Testing group invite send and accept:")
    loop = asyncio.get_event_loop()
    try:
        ivt = GroupInvite(toEmail=toEmail,inviteFromId=fromId)
        loop.run_until_complete(ivt.initialize())
        id = loop.run_until_complete(ivt.add_invite())
        assert(id!=None)
        print("inserted id = ",id)
        print("Group name: ",ivt.get_group_name())
        id = loop.run_until_complete(ivt.accept_invite())
        print("Accepted id: ",id)
    finally:
        loop.close()

# getting all group invites a user has
def test_get_group_invites(userEmail):
    print("Testing getting Group Invites:")
    loop = asyncio.get_event_loop()
    try:
        ivt = GroupInvite(toEmail=userEmail,inviteFromId="64bee34b6fa3a8c31741b6b0")
        id = loop.run_until_complete(ivt.add_invite())
        assert(id!=None)
        print("inserted id = ",id)
        user = loop.run_until_complete(database.log_in_user(userEmail))
        assert(user!=None)
        ivts = loop.run_until_complete(user.get_group_invites())
        for i in ivts:
            assert(i.get_group_name()!=None)
            print("location name: ",i.get_group_name())
    finally:
        loop.close()

# testing sending a friend request
def test_friend_invite(fromId,toEmail):
    print("Testing sending a friend invite:")
    loop = asyncio.get_event_loop()
    try:
        ivt = FriendInvite(toEmail=toEmail,inviteFromId=fromId)
        loop.run_until_complete(ivt.initialize())
        id = loop.run_until_complete(ivt.add_invite())
        assert(id!=None)
        print("inserted id = ",id)
        assert(ivt!=None)
        print(ivt.get_from_name())
        print(ivt.get_to_name())
        id = loop.run_until_complete(ivt.accept_invite())
        print("Accepted id: ",id)
    finally:
        loop.close()

#testing getting all friend invites
def test_get_all_friend_invites(userEmail):
    print("Testing getting all friend invites")
    loop = asyncio.get_event_loop()
    try:
        ivt = FriendInvite(toEmail=userEmail,inviteFromId="64b98136ee31d004275ff579")
        user = loop.run_until_complete(ivt.add_invite())
        assert(id!=None)
        print("inserted id = ",id)
        assert(ivt!=None)
        print(ivt.get_from_name())
        print(ivt.get_to_name())
        user = loop.run_until_complete(database.log_in_user(userEmail))
        assert(user!=None)
        ivts = loop.run_until_complete(user.get_friend_invites())
        assert(ivts!=None)
        for i in ivts:
            print("Friend name: ",i.get_from_name())
        loop.run_until_complete(ivt.reject_invite())
    finally:
        loop.close()

#testing getting all friends
def test_get_all_friends(userEmail):
    print("Testing getting all friends:")
    loop = asyncio.get_event_loop()
    try:
        user = loop.run_until_complete(database.log_in_user(userEmail))
        assert(user!=None)
        friends = loop.run_until_complete(user.get_friends())
        for i in friends:
            print("Friend name: ",i)
    finally:
        loop.close()

#remove_test("test@test.com","64bee34b6fa3a8c31741b6b0")
#auto_logout("test@test.com")
#test_loco_filter("1234@321")
#test_invite("64bee34b6fa3a8c31741b6b0","test@test.com")
#test_get_group_invites("test@test.com")
#test_friend_invite("64b98136ee31d004275ff579","test@test.com")
#test_get_all_friend_invites("test@test.com")
test_get_all_friends("test@test.com")
#login_test("test@test.com")
#test_loco_users("64b6bfbb54263d417e25e9d1")
#test_loco2()
#remove_test("test@main.com","64b6bfbb54263d417e25e9d1")