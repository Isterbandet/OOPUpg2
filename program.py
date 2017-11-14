from student import*

class Program(Student):
    def __init__(self,program):
        self._program = program
        self._students = []

    def addStudents(self,studentObjekt):
        self._students.append(studentObjekt)

    def totalSumOfStudentFee(self):
        totalFeesum = 0
        for student in self._students:
            totalFeesum += student.getFee()
        return totalFeesum



