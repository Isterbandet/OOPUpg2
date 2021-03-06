from person import *
class Student(Person):
    def __init__(self,name,address,program,year,fee):
        super().__init__(name,address)
        self._program = program
        self._year = year
        self._fee = fee



    def getProgram(self):
        return self._program
    def getYear(self):
        return self._year
    def getFee(self):
        return float(self._fee)

    def setProgram(self,program):
        self._program = str(program)
    def setYear(self,year):
        self._year = year

    def setFee(self,fee):
        self._fee = float(fee)

    def __str__(self):
        return "Student[{},program={},year={},fee={:.2f}]".format(super().__str__(),self.getProgram(),self.getYear(),self.getFee())
                                                                    #DRYYYYDRYYYYDRYYYYDRYYYYDRYYYYDRYYYYDRYYYYDRYYYYDRYYYYDRYYYY
