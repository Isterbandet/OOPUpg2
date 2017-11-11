

class Person:
    def __init__(self, name, address):
        self._name = name
        self._address = address

    def getName(self):
        return self._name
    def getAddress(self):
        return self._address

    def setAddress(self,address):
        self._address = address

    def __str__(self):
        return str(self._name,self._address)