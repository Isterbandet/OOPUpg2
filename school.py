from staff import Staff
from program import*

class School(Staff):
    def __init__(self,school):
        self._school = school
        self.program = []
        self.staff = []


    def addTeacher(self,teacher):
        self.staff.append(teacher)

    def addProfram(self, progeam):
        self.program.append(progeam)

    def totalSumOfTeacherSallery(self):
        totalSum = 0
        for pay in self.staff:
            totalSum+= self.getPay()
        return totalSum

