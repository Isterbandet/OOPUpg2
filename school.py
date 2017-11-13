from staff import Staff

class School(Staff):
    def __init__(self,school):
        self._school = school


    def addStaff(self,name, address, school, pay):
        return super().__init__(name, address, school, pay)


