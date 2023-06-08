import operations






#Testing the operations in operations.py
#input: none
#returns: none
def testOperations():
    name = "Gavin Buier"
    testAdd(name)
    testRemove(name)

#testing the removePerson function
#input: the name of the person we are tying to remove
#returns: none
def testRemove(name):
    print("begin remove")
    result = testFind(name)
    removed = operations.removePerson(name)
    assert(removed==len(result))
    print("ending remove")

#testing the addPerson function
#input: the name of the person we are trying to add
#returns: none
def testAdd(name):
    print("begin add")
    result = operations.addPerson(name)
    assert(len(result)>=1)
    print("ending add")

#testing the findPerson function from operations
#input: the name of the person we are trying to find
#returns: the number of people found
def testFind(name):
    print("begin find")
    result = operations.findPerson(name)
    #print("found: "+ result[1])
    print("ending find")
    return result

#hub function to run different tests
#input: none
#returns: none
def startTesting():
    print("Starting Tests")
    testOperations()
    print("Tests over")



startTesting()