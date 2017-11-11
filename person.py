

class Person:
    def __init__(self, name, address):
        self._name = name
        self._address = address

    def getName(self):
        return str(self._name)
    def getAddress(self):
        return self._address

    def setAddress(self,address):
        self._address = str(address)

    def __str__(self):
        return Person[self._name,self._address]