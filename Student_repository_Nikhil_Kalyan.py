# coding=utf-8
"""
Created on Monday 28 March 00:53:34 2020

@author: nkalyan🤠
        '''implementing Python scripts to print student and instructor tables'''
"""

from typing import Dict, Iterator, Tuple, KeysView
from prettytable import PrettyTable
from collections import defaultdict
from HW08_nikhil_kalyan import file_reader


class Student(object):
    """A student class that  holds the details of students"""
    
    def __init__(self, cwid: int, name: str, dept: str) -> None:
        """Initialize/ construct the student class"""
        
        self._name: str = name
        self._cwid: int = cwid
        self._department: str = dept
        self.student_courses: Dict[str] = dict()

    def add_course(self, course: str, grade: str) -> None:
        self.student_courses[course] = grade

    def get_course(self) -> KeysView[str]:
        return self.student_courses.keys()


class Instructor(object):
    """Instructor class that holds the details of instructor, The names of course taught
    registered courses"""
    
    def __init__(self, name: str, cwid: int, department: str) -> None:
        """Initialize a constructor of instructor data"""
    
        self._name: str = name
        self._cwid: int = cwid
        self._department: str = department
        self.instructor_courses: Dict[str] = defaultdict(int)

    def add_student(self, course: str) -> None:
        self.instructor_courses[course] += 1

    def get_course(self) -> KeysView[str]:
        return self.instructor_courses.keys()

    def get_student_count(self, course: str) -> int:
        return self.instructor_courses[course]


class University(object):
    """This is the main class the reads the whole data and perform the operations that need to create a table"""
    
    def __init__(self, directory_name) -> None:
        """Initialize a constructor to store the values"""
        
        self._directory: str = directory_name
        self._student: Dict[str, Student] = dict()
        self._instructor: Dict[str, Instructor] = dict()

    def get_students_details(self) -> None:
        """Method that gets the student details"""
        try:
            student_file: Iterator[Tuple[str]] = file_reader('students.txt', 3, sep='|', header=True)
        
            for cwid, name, dept in student_file:
                self._student[cwid] = Student(cwid, name, dept)
        except(FileNotFoundError, ValueError) as e:
            print(e)

    def get_instructors_details(self) -> None:
        """Method that gets the instructor details"""
        try:
            instructor_file: Iterator[Tuple[str]] = file_reader('instructors.txt', 3, sep='\t', header=True) 
        
            for cwid, name, dept in instructor_file:
                self._instructor[cwid] = Instructor(cwid, name, dept)
        except(FileNotFoundError, ValueError) as e:
            print(e)

    def get_grades(self) -> None:
        """Method the get the grades """
        try:
            grade_file: Iterator[Tuple[str]] = file_reader('grades.txt', 4, sep='\t', header=True)
        
            for student_cwid, course, grade, instructor_cwid in grade_file:
            
                if student_cwid in self._student.keys():
                    self._student[student_cwid].student_courses[course] = grade
                
                    if instructor_cwid in self._instructor.keys():
                        self._instructor[instructor_cwid].instructor_courses[course] += 1
        except(FileNotFoundError, ValueError) as e:
            print(e)

    def student_table(self) -> PrettyTable:
        """returns the pretty table of students with the defined fields"""
        
        print_student_table: PrettyTable = PrettyTable()
        print_student_table.field_names = ["CWID", "Name", "Completed Courses"]
        
        for cwid, student in self._student.items():
            print_student_table.add_row([cwid, student.name, sorted(list(student.student_courses.keys()))])
        return print_student_table

    def instructors_table(self) -> PrettyTable:
        """Returns pretty table of instructor with defined fields"""
        
        print_instructor_table: PrettyTable = PrettyTable()
        print_instructor_table.field_names = ["CWID", "Name", "Dept", "Course", "Students"]
        
        for cwid, instructor in self._instructor.items():
            for course in instructor.instructor_courses:
                print_instructor_table.add_row([cwid, instructor.name, instructor.department, course,
                                                instructor.instructor_courses[course]])
        return print_instructor_table


def main() -> None:
    """main function"""
    directory_name: str = '/Users/nikhilkalyan/PycharmProjects/SSW 810'
    result = University(directory_name)
    result.get_students_details()
    result.get_instructors_details()
    result.get_grades()
    print("Student Summary")
    print(result.student_table())
    print("Instructor Summary")
    print(result.instructors_table())


if __name__ == "__main__":
    main()
