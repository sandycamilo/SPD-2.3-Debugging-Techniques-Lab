# By Kamran Bigdely Nov. 2020
# Replace temp variable with query
# TODO: Use 'extract method' refactoring technique to improve this code. If required, use
#       'replace temp variable with query' technique to make it easier to extract methods.

class Employer:    
    def __init__(self, name):
        self.name = name

    def send(self, students):
        print("Students' contact info were sent to", self.name + '.')

class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name

    def get_gpa(self):
        return self.gpa

    def send_congrat_email(self):
        print("Congrats", self.name + ". You graduated successfully!")

class School:
    def __init__(self, students) -> None:
        self.students = students

    def process_graduation(self):
        """Finds the students in the school who have successfully graduated."""
        return self.print_names_and_email()
    
    def get_student_gpa(self):
        min_gpa = 2.5 # minimum acceptable GPA
        passed_students = []
        for student in self.students:
            if student.get_gpa() > min_gpa:
                passed_students.append(student)
        return passed_students

    def print_names_and_email(self):
        """Prints student's name who graduated and send congrats email."""
        print('*** Students who graduated *** ')
        passed_students = self.get_student_gpa()
        for student in passed_students:
            print('****************************')
            print(student.name)
            print('****************************')
            student.send_congrat_email()
        print('****************************')
        
        top_ten_percent = self.find_top_ten(passed_students)
        self.send_referral(top_ten_percent)

    def find_top_ten(self, passing):
        """Finds the top 10% of students."""
        passing.sort(key=lambda student: student.get_gpa())
        index = int(0.9 * len(passing))
        return passing[index:]
    
    def send_referral(self, top_10_percent):
        """Sends top 10% referrals to recruiters."""
        top_employers = [Employer('Microsoft'), Employer('Free Software Foundation'), Employer('Google')]
        for employer in top_employers:
            employer.send(students)

students = [Student(2.1, 'Pinocchio'), Student(2.3, 'goku'), Student(2.7, 'toro'), 
            Student(3.9, 'naruto'), Student(3.2,'kami'), Student(3,'guts')]
school  = School(students)
school.process_graduation()