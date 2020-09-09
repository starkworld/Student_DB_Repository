"""
Created on Friday April 06 16:53:34 2020

@author: nkalyan🤠
        '''Automation Testing Python Scripts using unittesting '''
"""

import os
import unittest
from typing import Iterator, Tuple, Dict, List, Union, Set
from HW10_nikhil_kalyan import University, Student, Instructor, file_reader, Major


class TestUniversity(unittest.TestCase):
    """Path setup"""

    def setUp(self):
        self.path: str = "/Users/nikhilkalyan/PycharmProjects/SSW 810"
        self.repository: University = University(self.path, False)

    def test_majors_table(self):
        """ Testing majors table"""
        expected_result: List[List] = [['SFEN', ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545']],
                   ['SYEN', ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810']]]

        output: List[str] = [majors.ptable_row() for majors in self.repository._majors.values()]
        self.assertEqual(expected_result, output)

    def test_Student_table(self):
        """ Testing student table """
        expected_result: List[List, int] = [[['10103', 'Baldwin, C', 'SFEN', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], [],
              3.44],
            ['10115', 'Wyatt, X', 'SFEN', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], [],
              3.81],
            ['10172', 'Forbes, I', 'SFEN', ['SSW 555', 'SSW 567'], ['SSW 540', 'SSW 564'], ['CS 501', 'CS 513', 'CS 545'],
              3.88],
            ['10175', 'Erickson, D', 'SFEN', ['SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'],
              ['CS 501', 'CS 513', 'CS 545'], 3.58],
            ['10183', 'Chapman, O', 'SFEN', ['SSW 689'], ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545'],
              4.0],
            ['11399', 'Cordova, I', 'SYEN', ['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], [], 3.0],
            ['11461', 'Wright, U', 'SYEN', ['SYS 611', 'SYS 750', 'SYS 800'], ['SYS 612', 'SYS 671'],
              ['SSW 540', 'SSW 565', 'SSW 810'], 3.92],
            ['11658', 'Kelly, P', 'SYEN', [], ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810'], 0.0],
            ['11714', 'Morton, A', 'SYEN', ['SYS 611', 'SYS 645'], ['SYS 612', 'SYS 671', 'SYS 800'],
              ['SSW 540', 'SSW 565', 'SSW 810'], 3.0],
            ['11788', 'Fuller, E', 'SYEN', ['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], [], 4.0]]]
        
        output = [[student.ptable_row() for cwid, student in self.repository._students.items()]]
        
        self.assertEqual(expected_result, output)

    def test_instructor_table(self):
        """Testcase for instructor table """
        expected_result: Set[Union[Tuple[str, str, str, str, int]]] = {('98765', 'Einstein, A', 'SFEN', 'SSW 567', 4),
                   ('98765', 'Einstein, A', 'SFEN', 'SSW 540', 3),
                   ('98764', 'Feynman, R', 'SFEN', 'SSW 564', 3),
                   ('98764', 'Feynman, R', 'SFEN', 'SSW 687', 3),
                   ('98764', 'Feynman, R', 'SFEN', 'CS 501', 1),
                   ('98764', 'Feynman, R', 'SFEN', 'CS 545', 1),
                   ('98763', 'Newton, I', 'SFEN', 'SSW 555', 1),
                   ('98763', 'Newton, I', 'SFEN', 'SSW 689', 1),
                   ('98760', 'Darwin, C', 'SYEN', 'SYS 800', 1),
                   ('98760', 'Darwin, C', 'SYEN', 'SYS 750', 1),
                   ('98760', 'Darwin, C', 'SYEN', 'SYS 611', 2),
                   ('98760', 'Darwin, C', 'SYEN', 'SYS 645', 1)}
        output: Set = {tuple(detail) for instructor in self.repository._instructors.values() for detail in
                   instructor.ptable_row()}
        self.assertEqual(expected_result, output)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
