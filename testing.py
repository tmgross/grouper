import operations






#Testing the operations in operations.py
def testOperations():
    name = "Gavin Buier"
    print("begin remove")
    removed = operations.removePerson(name)
    assert(removed>=1)
    print("ending remove")
    return


def startTesting():
    print("Starting Tests")
    testOperations()
    print("Tests over")



startTesting()