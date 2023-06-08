import operations






#Testing the operations in operations.py
def testOperations():
    name = "Gavin Buier"
    testAdd(name)
    testRemove(name)

def testRemove(name):
    print("begin remove")
    removed = operations.removePerson(name)
    assert(removed>=1)
    print("ending remove")
    return

def testAdd(name):
    print("begin add")
    result = operations.addPerson(name)
    assert(len(result)>=1)
    print("ending add")

def startTesting():
    print("Starting Tests")
    testOperations()
    print("Tests over")



startTesting()