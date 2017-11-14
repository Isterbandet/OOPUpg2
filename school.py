from staff import Staff
from program import*

class School(Staff):
    def __init__(self,school):
        self._school = school
        self._program = []
        self._staff = []


    def addTeacher(self, teacherObjekt):
        self._staff.append(teacherObjekt)

    def addProgram(self, progeamObjekt):
        self._program.append(progeamObjekt)

    def totalSumOfTeacherSallery(self):
        totalSum = 0
        for staff in self._staff:
            totalSum+= staff.getPay()
        return totalSum

    def getTotalIncomeForTheProgram(self):
        totalProgram = 0
        for program in self._program:
            totalProgram += program.totalSumOfStudentFee()
        return totalProgram

    def isTheSchollSomethingTobuyAktierFrom(self):
        if self.getTotalIncomeForTheProgram() < self.totalSumOfTeacherSallery():
            print("It is time to invest")
        elif self.getTotalIncomeForTheProgram() == self.totalSumOfTeacherSallery():
            print ("The school goes +- 0 fire a teacher")
        elif self.getTotalIncomeForTheProgram() > self.totalSumOfTeacherSallery():
            print("Do not invest")