from person import *
class Student(Person):
    def __init__(self,name,address,program,year,fee):
        super().__init__(name,address)
        self._program = program
        self._year = year
        self._fee = fee



    def getProgram(self,_program):
        return self._program
    def getYear(self,_year):
        return self._year
    def getFee(self,_fee):
        return self._fee

    def setProgram(self,program):
        self._program = str(program)
    def setYear(self,year):
        self._year = int(year)

    def setFee(self,fee):
        self._fee = int(fee)

    def __str__(self):
        return str(self._year,self._program,self._fee)