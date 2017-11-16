import unittest

from person import Person
from staff import Staff
from student import Student
from school import*
from program import*

class TestPerson(unittest.TestCase):
    def test_person_01_constructor( self ):
        p = Person("Mark", "Min Gata 1")
        self.assertEqual( str(p), "Person[name=Mark,address=Min Gata 1]" )

    def test_person_02_get_name( self ):
        p = Person("Mark", "Min Gata 1")
        self.assertEqual( p.getName(), "Mark" )

    def test_person_03_get_address( self ):
        p = Person("Mark", "Min Gata 1")
        self.assertEqual( p.getAddress(), "Min Gata 1" )

    def test_person_04_set_address( self ):
        p = Person("Mark", "Min Gata 1")
        p.setAddress( "Annan Gata 2" )
        self.assertEqual( p.getAddress(), "Annan Gata 2" )


class TestStudent(unittest.TestCase):
    def test_student_01_constructor( self ):
        p = Student("Mark", "Min Gata 1", "IoT", 17, 50000)
        self.assertEqual( str(p), "Student[Person[name=Mark,address=Min Gata 1],program=IoT,year=17,fee=50000.00]" )

    def test_student_02_get_program( self ):
        p = Student("Mark", "Min Gata 1", "IoT", 17, 50000)
        self.assertEqual( p.getProgram(), "IoT" )

    def test_student_03_set_program( self ):
        p = Student("Mark", "Min Gata 1", "IoT", 17, 50000)
        p.setProgram( "3D Design" )
        self.assertEqual( p.getProgram(), "3D Design" )

    def test_student_04_get_year( self ):
        p = Student("Mark", "Min Gata 1", "IoT", 17, 50000)
        self.assertEqual( p.getYear(), 17 )

    def test_student_05_set_year( self ):
        p = Student("Mark", "Min Gata 1", "IoT", 17, 50000)
        p.setYear(16)
        self.assertEqual( p.getYear(), 16 )

    def test_student_06_get_fee( self ):
        p = Student("Mark", "Min Gata 1", "IoT", 17, 50000)
        self.assertEqual( p.getFee(), 50000 )

    def test_student_07_set_fee( self ):
        p = Student("Mark", "Min Gata 1", "IoT", 17, 50000)
        p.setFee( 125.66 )
        self.assertEqual( p.getFee(), 125.66 )




class TestStaff(unittest.TestCase):
    def test_staff_01_constructor( self ):
        p = Staff("Mark", "Min Gata 1", "Nackademin", 50)
        self.assertEqual( str(p), "Staff[Person[name=Mark,address=Min Gata 1],school=Nackademin,pay=50.00]" )

    def test_staff_02_get_school( self ):
        p = Staff("Mark", "Min Gata 1", "Nackademin", 50)
        self.assertEqual( p.getSchool(), "Nackademin" )

    def test_staff_03_set_school( self ):
        p = Staff("Mark", "Min Gata 1", "Nackademin", 50)
        p.setSchool( "Medieinstitutet" )
        self.assertEqual( p.getSchool(), "Medieinstitutet" )

    def test_staff_04_get_pay( self ):
        p = Staff("Mark", "Min Gata 1", "Nackademin", 50)
        self.assertEqual( p.getPay(), 50 )

    def test_staff_05_set_pay( self ):
        p = Staff("Mark", "Min Gata 1", "Nackademin", 50)
        p.setPay( 125.66 )
        self.assertEqual( p.getPay(), 125.66 )



class testMyOwnStuff(unittest.TestCase):
    # Här ser jag att de går att räkna ut lätatlönen
     def test_Teachers_sallery(self):
        Nackademin = School("Nackademin")
        staff1=Staff("Mark", "KlassrumC001", "Nackademin", 45000)
        staff2=Staff("Satanipekele", "sverige", "Nackademin", 1000)
        Nackademin.addTeacher(staff1)
        Nackademin.addTeacher(staff2)
        self.assertEqual( Nackademin.totalSumOfTeacherSallery(),46000)

     def test_Student_FeeeContribution_Different_Programs(self):
        # Här ser jag att det funkar att lägga in eleverna i 2 olika program. Och att den räknar ut värdet av programmens income.

        Student1 = Student("Anton", "Enköping", "IoT", 94, 50000)
        Student2 = Student("The", "Man", "Hackeranked", 94, 10000)

        program1 = Program("IoT")
        program2 = Program("Hackeranked")

        program1.addStudents(Student1)
        program2.addStudents(Student2)

        school = School("Backademin")
        school.addProgram(program1)
        school.addProgram(program2)
        self.assertEqual(school.getTotalIncomeForTheProgram(), 60000)




     def test_if_itistimeto_Invest_The_Answer_Should_be_No(self):
        #Det här är bara super Dry
        school = School("Backademin")

        Student1 = Student("Anton", "Enköping", "IoT", 94, 50000)
        Student2 = Student("The", "Man", "Hackeranked", 94, 10000)
        #Lärarlön 60000
        staff1 = Staff("Mark", "KlassrumC001", "Nackademin", 45000)
        staff2 = Staff("Satanipekele", "sverige", "Nackademin", 1000)
        #Elevfee 55000
        school.addTeacher(staff1)
        school.addTeacher(staff2)
        program1 = Program("IoT")
        program2 = Program("Hackeranked")
        program1.addStudents(Student1)
        program2.addStudents(Student2)
        school.addProgram(program1)
        school.addProgram(program2)
        self.assertEqual(school.isTheSchollSomethingTobuyAktierFrom(), "Do not invest")


     def test_if_itistimeto_Invest_The_Answer_Should_be_YES(self):
        # Det här är bara super Dry
        school = School("Backademin")

        Student1 = Student("Anton", "Enköping", "IoT", 94, 50000)
        Student2 = Student("The", "Man", "Hackeranked", 94, 10000)
        # Lärarlön 60000
        staff1 = Staff("Mark", "KlassrumC001", "Nackademin", 50000)
        staff2 = Staff("Satanipekele", "sverige", "Nackademin", 60000)
        # Elevfee 11000
        school.addTeacher(staff1)
        school.addTeacher(staff2)
        program1 = Program("IoT")
        program2 = Program("Hackeranked")
        program1.addStudents(Student1)
        program2.addStudents(Student2)
        school.addProgram(program1)
        school.addProgram(program2)
        self.assertEqual(school.isTheSchollSomethingTobuyAktierFrom(), "It is time to invest")


     def test_if_itistimeto_Invest_The_Answer_Should_be_TheSchoolGoesEven(self):
        # Det här är bara super Dry
        school = School("Backademin")

        Student1 = Student("Anton", "Enköping", "IoT", 94, 10000)
        Student2 = Student("The", "Man", "Hackeranked", 94, 10000)
        # Lärarlön 20000
        staff1 = Staff("Mark", "KlassrumC001", "Nackademin", 10000)
        staff2 = Staff("Satanipekele", "sverige", "Nackademin", 10000)
        # Elevfee 20000
        school.addTeacher(staff1)
        school.addTeacher(staff2)
        program1 = Program("IoT")
        program2 = Program("Hackeranked")
        program1.addStudents(Student1)
        program2.addStudents(Student2)
        school.addProgram(program1)
        school.addProgram(program2)
        self.assertEqual(school.isTheSchollSomethingTobuyAktierFrom(), "The school goes +- 0 fire a teacher")


"""
program1 = Program("IoT")
program2 = Program("Hackeranked")

Student1=Student("Name","addres","Program",94,25)
Student2=Student("Name","addres","Program",94,25)

program1.addStudents(Student1)
program2.addStudents(Student2)



school = School("Backademin")

school.addProgram(program1)
school.addProgram(program2)

staff1=Staff("Name","addres","S",25)
staff2=Staff("Name","addres","Skola",25)
school.addTeacher(staff1)
school.addTeacher(staff2)

school.isTheSchollSomethingTobuyAktierFrom()
"""

if __name__ == '__main__':
    unittest.main(verbosity=2)
