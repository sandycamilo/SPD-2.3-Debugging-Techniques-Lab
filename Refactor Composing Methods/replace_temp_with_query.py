# By Kamran Bigdely Nov. 2020
# Replace temp variable with query
# TODO: Use 'extract method' refactoring technique to improve this code. If required, use
#       'replace temp variable with query' technique to make it easier to extract methods.

class Employer:    
    def __init__(self, name):
        self.name = name

    def send_info(self, students):
        print("Students' contact info were sent to", self.name + '.')

class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name

    def get_gpa(self):
        return self.gpa

    def send_congrats_email(self):
        print("Congrats", self.name + ". You graduated successfully!")

class School:
    def __init__(self, students, recruiters) -> None:
        self.students = students
        self.recruiters = recruiters
    
    def passing_students(self):
        """Gets passings students."""
        min_gpa = 2.5 # minimum acceptable GPA
        passed_students = []
        for s in self.students:
            if s.get_gpa() > min_gpa:
                passed_students.append(s)
        return passed_students

    def process_graduation(self):
        """Find the students in the school who have successfully graduated."""
        passing = self.passing_students()
        return passing

    def print_graduates(self, passing):
        # Prints the student's name who have graduated
        print('*** Student who graduated *** ')
        for s in passing:
            print(s.name)
        print('****************************')
        
    def congrats_email_graduates():
        """Sends congrats emails to graduates."""
        for s in passed_students:
            s.send_congrat_email()
    
    def send_student_referrals():
        """Finds the top 10% in student body and send their contact to the top employers."""
        passed_students.sort(key=lambda s: s.get_gpa())
        percentile = 0.9
        index = int(percentile * len(passed_students))
        top_10_percent = passed_students[index:]
        for e in top_employers:
            e.send(top_10_percent)

top_employers = [Employer('Microsoft'), Employer('Free Software Foundation'), Employer('Google')]
students = [Student(2.1, 'donald'), Student(2.3, 'william'), Student(2.7, 'toro'), 
            Student(3.9, 'lili'), Student(3.2,'kami'), Student(3,'sarah')]
school  = School(students)
school.process_graduation()
