import database
import asyncio
from objects import User
from location import *
from invite import GroupInvite
from friendInvite import FriendInvite

#this is a file for testing different operations
import unittest

class Testing(unittest.TestCase):
    """
    # testing adding a user to a location
    def add_test(self):
        print("Testing adding a user to a location:")
        email = "test@test.com"
        locoid = "64bee34b6fa3a8c31741b6b0"
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
    def remove_test(self):
        print("Testing removing a user from a location:")
        email = "test@test.com"
        locoid = "64bee34b6fa3a8c31741b6b0"
        loop = asyncio.get_event_loop()
        loco = loop.run_until_complete(database.get_location(locoid))
        user = loop.run_until_complete(database.log_in_user(email))
        try:
            loop.run_until_complete(database.remove_user(user,loco))
        finally:
            loop.close()


    #testing logging in a user
    def login_test(self):
        print("Testing logging in a user:")
        email = "test@test.com"
        loop = asyncio.get_event_loop()
        try:
            user = loop.run_until_complete(database.log_in_user(email))
            assert(user!=None)
            assert(user.get_name()!=None)
            assert(user.get_id()!=None)
            assert(user.get_email()==email)
        finally:
            loop.close()
    """
    # testing adding a user to a location
    async def add_test(self):
        print("Testing adding a user to a location:")
        email = "test@test.com"
        locoid = "64bee34b6fa3a8c31741b6b0"
        #loop = asyncio.get_event_loop()
        loco = await database.get_location(locoid)
        user = await database.log_in_user(email)
        newid = await database.add_user_to_location(user=user,location=loco)
        print(newid)
        assert(newid!=None)


    # testing removing a user from a location
    async def remove_test(self):
        print("Testing removing a user from a location:")
        email = "test@test.com"
        locoid = "64bee34b6fa3a8c31741b6b0"
        loco = await database.get_location(locoid)
        user = await database.log_in_user(email)
        res = await database.remove_user(user,loco)
        assert(res>=0)


    #testing logging in a user
    async def login_test(self):
        print("Testing logging in a user:")
        email = "test@test.com"
        user = await database.log_in_user(email)
        assert(user!=None)
        assert(user.get_name()!=None)
        assert(user.get_id()!=None)
        assert(user.get_email()==email)
        


    # test removing a user from all locations they are at 
    async def auto_logout(self):
        print("Testing removal of a user from any location:")
        email = "test@test.com"
        user = await database.log_in_user(email)
        dele = await database.remove_user_any(user)
        assert(user!=None)
        assert(user.get_name()!=None)
        assert(user.get_id()!=None)
        assert(user.get_email()==email)
        assert(dele>=0)
        print(dele)
        print(user.get_name())
        print(user.get_id())


    # testing getting every location 
    async def get_locos(self):
        print("Testing getting every location:")
        locos = await database.get_all_locations()
        assert(locos!=None)
        print(locos)


    # testing getting a single location
    async def test_location_get(self):
        print("Testing getting a single location:")
        id = "64bee34b6fa3a8c31741b6b0"
        locos = await database.get_location(id)
        assert(locos!=None)
        print(locos.get_name())


    # testing getting all locations and then checking all locations
    async def test_loco2(self):
        print("Testing getting and checking every location:")
        locos = await database.get_all_locations()
        for l in locos.keys():
            val = await database.get_location(l)
            assert(val!=None)
            assert(val.get_id()!=None)
            assert(val.get_name()!=None)
            print(val.get_id())
            print(val.get_name())


    # testing getting the current users on a location
    async def test_loco_users(self):
        print("Testing getting all users at a location:")
        id = "64bee34b6fa3a8c31741b6b0"
        loco =Location(id)
        val = await loco.get_current_users()
        for l in val:
            assert(l!=None)
            print("user name: ",l)

    '''
    #test giving a user access to a location
    def test_add_user_access(self):
        print("Testing adding user access:")
        id = "64bee34b6fa3a8c31741b6b0"
        email = "test@test.com"
        loop = asyncio.get_event_loop()
        try:
            loco =Location(id)
            user = loop.run_until_complete(database.log_in_user(email))
            val = loop.run_until_complete(database.add_user_access(user,loco))
            assert(val!=None)
            print(val)
        finally:
            loop.close()
    '''
    #test giving a user access to a location
    async def test_add_user_access(self):
        print("Testing adding user access:")
        id = "64bee34b6fa3a8c31741b6b0"
        email = "test@test.com"
        loco =Location(id)
        user = await database.log_in_user(email)
        val = await database.add_user_access(user,loco)
        assert(val!=None)
        print(val)


    # test the location filter for users view
    async def test_loco_filter(self):
        print("Testing location filter:")
        email = "test@test.com"
        user = await database.log_in_user(email)
        locos = await database.get_all_locations(user)
        assert(locos!=None)
        print(locos)

    # test sending a group invite
    async def test_invite(self):
        print("Testing group invite send and accept:")
        toEmail = "test@test.com"
        fromId = "64bee34b6fa3a8c31741b6b0"
        ivt = GroupInvite(toEmail=toEmail,inviteFromId=fromId)
        await ivt.initialize()
        id = await ivt.add_invite()
        assert(id!=None)
        print("inserted id = ",id)
        print("Group name: ",ivt.get_group_name())
        id = await (ivt.accept_invite())
        print("Accepted id: ",id)

    # getting all group invites a user has
    async def test_get_group_invites(self):
        print("Testing getting Group Invites:")
        userEmail = "test@test.com"
        ivt = GroupInvite(toEmail=userEmail,inviteFromId="64bee34b6fa3a8c31741b6b0")
        id = await ivt.add_invite()
        assert(id!=None)
        print("inserted id = ",id)
        user = await database.log_in_user(userEmail)
        assert(user!=None)
        ivts = await user.get_group_invites()
        for i in ivts:
            assert(i.get_group_name()!=None)
            print("location name: ",i.get_group_name())


    # testing sending a friend request
    async def test_friend_invite(self):
        print("Testing sending a friend invite:")
        fromId ="64b98136ee31d004275ff579"
        toEmail ="test@test.com"
        ivt = FriendInvite(toEmail=toEmail,inviteFromId=fromId)
        await ivt.initialize()
        id = await ivt.add_invite()
        assert(id!=None)
        print("inserted id = ",id)
        assert(ivt!=None)
        print(ivt.get_from_name())
        print(ivt.get_to_name())
        id = await ivt.accept_invite()
        print("Accepted id: ",id)

    #testing getting all friend invites
    async def test_get_all_friend_invites(self):
        print("Testing getting all friend invites")
        userEmail ="test@test.com"
        ivt = FriendInvite(toEmail=userEmail,inviteFromId="64b98136ee31d004275ff579")
        user = await ivt.add_invite()
        assert(id!=None)
        print("inserted id = ",id)
        assert(ivt!=None)
        print(ivt.get_from_name())
        print(ivt.get_to_name())
        user = await database.log_in_user(userEmail)
        assert(user!=None)
        ivts = await user.get_friend_invites()
        assert(ivts!=None)
        for i in ivts:
            print("Friend name: ",i.get_from_name())
        num = await ivt.reject_invite()
        assert(num>0)

    #testing getting all friends
    async def test_get_all_friends(self):
        print("Testing getting all friends:")
        userEmail ="test@test.com"
        user = await database.log_in_user(userEmail)
        assert(user!=None)
        friends = await user.get_friends()
        for i in friends:
            print("Friend name: ",i)

    
if __name__ == '__main__':
    unittest.main()

    
    
    
