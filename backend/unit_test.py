import unittest
import asyncio
import database

class TestDatabaseMethods(unittest.TestCase):
    # The first two test cases are commented out because running multiple test cases does not work, as the loop
    # cannot be reopened once it is closed. The final, uncommented test case covers all functions, so this
    # should not be a problem 
    '''
    def test_create_user(self):
        loop = asyncio.new_event_loop()
        try:
            user = loop.run_until_complete(database.create_user("AddTest"))
            self.assertNotEqual(user, None)
        finally:
            loop.close()
    
    def test_remove_user(self):
        loop = asyncio.new_event_loop()
        try:
            user = loop.run_until_complete(database.create_user("RemoveTest"))
            self.assertNotEqual(user, None)
            result = loop.run_until_complete(database.remove_user("RemoveTest"))
            self.assertNotEqual(result, None)
        finally:
            loop.close()
    '''
    def test_fetch_one_user(self):
        loop = asyncio.new_event_loop()
        try:
            user = loop.run_until_complete(database.create_user("FetchOneTest"))
            self.assertNotEqual(user, None)
            document = loop.run_until_complete(database.fetch_one_user("FetchOneTest"))
            self.assertEqual(document.get('name'), "FetchOneTest")
            result = loop.run_until_complete(database.remove_user("FetchOneTest"))
            self.assertNotEqual(result, None)
        finally:
            loop.close()
if __name__ == '__main__':
    unittest.main()