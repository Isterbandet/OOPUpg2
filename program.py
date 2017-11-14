from student import*

class Program(Student):
    def __init__(self,program):
        self._program = program
        self._students = []

    def addStudents(self,name):
        self._students.append(name)

    def totalSumOfStudentFee(self):
        totalFeesum = 0
        for students in self._students:
            totalFeesum += students.getFee()
        return totalFeesum



