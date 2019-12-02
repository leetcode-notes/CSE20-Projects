##########
class Students:

    def __init__(self, students=[]):
        self.students = dict()
        for student in self.students:
            self.students[student.fetch_number()] = student

    def add_student(self, student):
        ''' Add a student to the students dictionary.
            Return True if successful, else return False. '''
        # YOUR CODE HERE
        pass

    def add_students(self, students):
        ''' Add list of students to the students dictionary. '''
        # YOUR CODE HERE
        pass

    def fetch_students(self):
        ''' Return the students dictionary. '''
        return self.students

    def fetch_student(self, studentID):
        ''' Return the student with this student number (ID). '''
        # YOUR CODE HERE
        pass

    def fetch_student_numbers(self):
        return list(self.students.keys())



class Student:

    def __init__(self, first_name = 'First_Name',
                       last_name = 'Last_Name',
                       student_number = '0000'):
        self.first_name = first_name
        self.last_name = last_name
        self.student_number = student_number
        self.past_courses = []      # course numbers (IDs)
        self.current_courses = []   # course numbers (IDs)

    def fetch_name(self):
        ''' Return the name of this student, (first_name, last_name). '''
        # YOUR CODE HERE
        pass

    def fetch_number(self):
        ''' Return this students student number (ID). '''
        # YOUR CODE HERE

    def add_past_courses(self, course_IDs = []):
        ''' Append this list of past course numbers (IDs)
            to the list of this student's past courses. '''
        # YOUR CODE HERE
        pass

    def add_current_courses(self, course_IDs = []):
        ''' Append this list of current course numbers (IDs)
            to the list of this student's current courses. '''
        # YOUR CODE HERE
        pass

    def add_course(self, courseID):
        ''' Append this course number (ID) to the list of current_courses. '''
        # YOUR CODE HERE
        pass

    def fetch_past_courses(self):  return self.past_courses

    def fetch_current_courses(self):  return self.current_courses

    def drop_current_course(self, courseID):
        ''' Drop this course number (ID) from the list of current_courses.
            Return True if successful, else return False. '''
        #YOUR CODE HERE
        pass

    def drop_all_current_courses(self):
        ''' Empty the current_courses list. '''
        self.current_courses = []

    def current_to_past_courses(self):
        ''' Move all current course numbers (IDs) to the list of past_courses. '''
        self.past_courses += self.current_courses
        self.drop_all_current_courses()



class Courses:

    def __init__(self, courses=[]):
        self.courses = dict()
        # This dictionary has course numbers (IDs) for its keys.
        for course in courses:
            self.courses[course.fetch_course_number()] = course

    def add_course(self, course):
        ''' Add this course to the courses dictionary.
            Return True if successful, else return False. '''
        # YOUR CODE HERE
        pass

    def add_courses(self, courses):
        # YOUR CODE HERE
        pass

    def fetch_course_numbers(self):
        ''' Return a list of course numbers (IDs). '''
        return list(self.courses.keys())

    def fetch_courses(self):
        ''' Return the dictionary of courses. '''
        return self.courses

    def fetch_course(self, courseID):
        ''' Fetch the course with this course number (ID). '''
        #YOUR CODE HERE
        pass


class Course:

    def __init__(self, course_name = 'CS 000',
                 course_number = '0000',
                 semester = 'Fall',
                 year = 2019,
                 enrolled_students = []):
        ''' The enrolled_students argument is a list of student numbers (Ids) '''

        self.course_name = course_name
        self.course_number = course_number
        self.semester = semester
        self.year = year
       # This dictionary has student numbers (IDs) as keys,
       # and the student's grade as the value.
        self.enrolled_students = {student : 'NG' for student in enrolled_students}

    def fetch_course_name(self):
        ''' Return this course name. '''
        # YOUR CODE HERE
        pass

    def fetch_course_number(self):
        ''' Return this course number. '''
        # YOUR CODE HERE
        pass

    def fetch_enrolled_studentIDs(self):
        ''' Return a list of enrolled student numbers (IDs). '''
        return list(self.enrolled_students.keys())

    def fetch_enrolled_students(self):
        ''' Return the dictionary of enrolled students and their grades. '''
        # YOUR CODE HERE
        pass

    def fetch_when_offered(self):
        ''' Return (semester, year) of when this course was offered. '''
        return (self.semester, self.year)

    def enroll_student(self, studentID):
        ''' Enroll a student in the course.
            Return True if successful, else return False. '''
        # YOUR CODE HERE
        pass

    def enroll_students(self, studentIDs):
        ''' Enroll multiple students in the course.
            Return True if successful, else return False. '''
        # YOUR CODE HERE
        pass

    def drop_student(self, studentID):
        ''' Drop this student from the course.
            Return True if successful, else return False. '''
        # YOUR CODE HERE
        pass

    def submit_grade(self, studentID, grade):
        ''' Enter a grade for this student. '''
        # YOUR CODE HERE
        pass

    def fetch_grades(self):
        ''' Return the enrolled_students dictionary. '''
        return self.enrolled_students

    def fetch_grade(self, studentID):
	  ''' Return this student’s grade. '''
        # YOUR CODE HERE
        pass



def roll_courses():
    ''' A semester has finished, and the grades are all in. This function rolls all
       the current courses for each student from current_courses to past_courses. '''
    pass
def compute_gpa(studentID):
    ''' Returns the GPA of the student with input student number(ID),
       rounded off to 2 decimal places. '''
    pass
def compute_gpas(studentIDs):
    ''' Retuns a list of the gpas of all the students on the input list. '''
    pass
def best_student():
    ''' Returns the name of the student with the highest GPA, in the format:
       FirstName LastName  (with one space between them)  '''
    pass
def worst_student():
    ''' Returns the name of the student with the lowest GPA, in the format:
       FirstName LastName   (with one space between them)  '''
    pass
def compute_mean_GPA(): 
    ''' Return the mean GPA of all students, rounded off to 2 decimal places. '''
    pass

def compute_mean_course_GPA(courseID):
    ''' Returns the mean GPA for the grades assigned to students who took this course. '''
    pass

all_courses = Courses()
all_students = Students()
