from person import *
class Staff(Person):
        def __init__(self, name, address, school,pay):
            super().__init__(name, address)
            self._school = school

            self._pay = pay

        def getSchool(self):
            return self._school



        def getPay(self):
            return float(self._pay)

        def setSchool(self, school):
            self._school= str(school)



        def setFee(self, pay):
            self._pay = pay

        def __str__(self):
            return 