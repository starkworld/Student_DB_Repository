"""
Created on Sunday April 12 16:53:34 2020

@author: nkalyan🤠
        Testing University repository database by using python methods and modules. 
"""


import os
import unittest
from typing import Iterator, Tuple, Dict, List, Union
from Student_repository_nikhil_kalyan import University, Student, Instructor, Major


class TestUniversity(unittest.TestCase):
    """Test cases for university class methods"""

    def setUp(self):
        """Setting up the path"""
        self.test_path: str = "/Users/nikhilkalyan/PycharmProjects/SSW 810"
        self.stevens: University = University(self.test_path, False)
        self.test_path: str = "/Users/nikhilkalyan/PycharmProjects/SSW 810"
        self.harvard = University(self.test_path, False)

    def test_majors_summary_table(self):
        """ Testing updated majors table """
        expected_output: List[List[Union[str, List[str]]]] = [['SFEN', ['SSW 540', 'SSW 555', 'SSW 810'], ['CS 501', 'CS 546']],
                   ['CS', ['CS 546', 'CS 570'], ['SSW 565', 'SSW 810']]]

        output = [majors.ptable_row() for majors in self.stevens._majors.values()]
        self.assertEqual(expected_output, output)

    def test_Student_summary_table(self):
        """ Testing updated student table """
        expected_output: List[List[Union[str, List[str]]]] = [['10103', 'Jobs, S', 'SFEN', ['CS 501', 'SSW 810'], ['SSW 540', 'SSW 555'], [], 3.38],
                   ['10115', 'Bezos, J', 'SFEN', ['SSW 810'], ['SSW 540', 'SSW 555'], ['CS 501', 'CS 546'], 2.0],
                   ['10183', 'Musk, E', 'SFEN', ['SSW 555', 'SSW 810'], ['SSW 540'], ['CS 501', 'CS 546'], 4.0],
                   ['11714', 'Gates, B', 'CS', ['CS 546', 'CS 570', 'SSW 810'], [], [], 3.5]]

        output: List = [student.ptable_row() for cwid, student in self.stevens._students.items()]
        self.assertEqual(expected_output, output)

    def test_Instructor_summary_table(self):
        """Test cases for updated instructor table from database"""
        expected_output: List[List[Union[str, List[str]]]] = [['98764', 'Cohen, R', 'SFEN', 'CS 546', 1],
                   ['98763', 'Rowland, J', 'SFEN', 'SSW 810', 4],
                   ['98763', 'Rowland, J', 'SFEN', 'SSW 555', 1],
                   ['98762', 'Hawking, S', 'CS', 'CS 501', 1],
                   ['98762', 'Hawking, S', 'CS', 'CS 546', 1],
                   ['98762', 'Hawking, S', 'CS', 'CS 570', 1]]

        output = [info for instructor in self.harvard._instructors.values() for info in instructor.ptable_row()]

        self.assertEqual(expected_output, output)
        
    def test_grades_summary_table(self):
        """Testing updated grade table"""
        expected_output: List[List[str]] = [['Bezos, J', 10115, 'SSW 810', 'A', 'Rowland, J'],
                                            ['Bezos, J', 10115, 'CS 546', 'F', 'Hawking, S'],
                                            ['Gates, B', 11714, 'SSW 810', 'B-', 'Rowland, J'],
                                            ['Gates, B', 11714, 'CS 546', 'A', 'Cohen, R'],
                                            ['Gates, B', 11714, 'CS 570', 'A-', 'Hawking, S'],
                                            ['JObs, S', 10103, 'SSW 810', 'A-', 'Rowland, J'],
                                            ['JObs, S', 10103, 'CS 501', 'B', 'Hawking, S'],
                                            ['Musk, E', 10183, 'SSW 555', 'A', 'Rowland, J'],
                                            ['Musk, E', 10183, 'SSW 810', 'A', 'Rowland, J']]
        
        output: List = [each_row for each_row in self.stevens.student_summary_database()]
        print(output)
        self.assertEqual(expected_output, output)        

if __name__ == "__main__":
    """Execution starts from here"""
    unittest.main(exit=False, verbosity=2)