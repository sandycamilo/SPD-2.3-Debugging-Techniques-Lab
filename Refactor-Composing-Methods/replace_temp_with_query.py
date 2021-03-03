class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name

    def get_gpa(self):
        return self.gpa

    def send_congrats_email(self):
        print("Congrats", self.name + ". You graduated successfully!")

class Employer:
    def __init__(self, name):
        self.name = name

    def send(self, students):
        print("Students' contact info were sent to", self.name + '.')

class School:
    def __init__(self, students, recruiters) -> None:
        self.students = students
        self.recruiters = recruiters
    
    def get_passing_students(self):
        min_gpa = 2.5 # minimum acceptable GPA
        passed_students = []
        for student in self.students:
            if student.get_gpa() > min_gpa:
                passed_students.append(student)
        return passed_students

    def process_graduation(self):
        """Find the students in the school who have successfully graduated and send a congrants email."""
        passing = self.get_passing_students()

        print('*** Student who graduated *** ')
        for student in passing:
            print(student.name)
            student.send_congrats_email()
        print('****************************')
    
        top_ten = self.get_top_10(passing)

        self.send_referral(self.recruiters, top_ten)

    def get_top_10(self, passing):
        """Find the top 10% of them and send their contact to the top employers."""
        passing.sort(key=lambda student: student.get_gpa())
        percentile = 0.9
        index = int(percentile * len(passing))
        return passing[index:]

    def send_referral(self, recruiters, referral):
        for r in recruiters:
            r.send(referral)
            
top_employers = [Employer('Microsoft'), Employer('Free Software Foundation'), Employer('Google')]
students = [Student(2.1, 'donald'), Student(2.3, 'william'), Student(2.7, 'toro'),
            Student(3.9, 'lili'), Student(3.2,'kami'), Student(3,'sarah')]
school  = School(students, top_employers)
school.process_graduation()