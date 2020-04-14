"""
Created on Friday March 27 16:53:34 2020

@author: nkalyan🤠
        '''Automation Testing Python Scripts using unittesting '''
"""


import unittest
from typing import List
from HW09_Nikhil_Kalyan import University, Student, Instructor


class TestUniversity(unittest.TestCase):
    """Testing methods in university class"""
    def test_student_table(self):
        """Automation testing for student table method"""
        harvard = University('/Users/nikhilkalyan/PycharmProjects/SSW 810')
        harvard.get_students_details()
        harvard.get_instructors_details()
        harvard.get_grades()

        expected_result: List = list()
        for cwid, student in harvard._student.items():
            expected_result.append((cwid, student._name, list(student.student_courses.keys())))

        self.assertEqual(expected_result, [('10115', 'Wyatt, X', ['SSW 567', 'SSW 564', 'SSW 687', 'CS 545']),
                               ('10172', 'Forbes, I', ['SSW 555', 'SSW 567']),
                               ('10175', 'Erickson, D', ['SSW 567', 'SSW 564', 'SSW 687']),
                               ('10183', 'Chapman, O', ['SSW 689']),
                               ('11399', 'Cordova, I', ['SSW 540']),
                               ('11461', 'Wright, U', ['SYS 800', 'SYS 750', 'SYS 611']),
                               ('11658', 'Kelly, P', ['SSW 540']),
                               ('11714', 'Morton, A', ['SYS 611', 'SYS 645']),
                               ('11788', 'Fuller, E', ['SSW 540'])])

    def test_instructor_table(self):
        """Automation test cases for instructor table"""
        stanford = University('/Users/nikhilkalyan/PycharmProjects/SSW 810')
        stanford.get_students_details()
        stanford.get_instructors_details()
        stanford.get_grades()

        expected_result: List = list()
        for cwid, instructor in stanford._instructor.items():
            for course, students in instructor.instructor_courses.items():
                expected_result.append((cwid, instructor._name, instructor._department, course, students))

        self.assertEqual(expected_result, [('98764', '98764', 'SFEN', 'SSW 564', 2),
                               ('98764', '98764', 'SFEN', 'SSW 687', 2),
                               ('98764', '98764', 'SFEN', 'CS 545', 1),
                               ('98763', '98763', 'SFEN', 'SSW 555', 1),
                               ('98763', '98763', 'SFEN', 'SSW 689', 1),
                               ('98760', '98760', 'SYEN', 'SYS 800', 1),
                               ('98760', '98760', 'SYEN', 'SYS 750', 1),
                               ('98760', '98760', 'SYEN', 'SYS 611', 2),
                               ('98760', '98760', 'SYEN', 'SYS 645', 1)])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

if __name__ == '__main__':
    unittest.main()
