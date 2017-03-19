from . import TestCaseWithTime

from chapter2_Getting_Started.code_for_practice.Exercises2_1_2 import *


class test_insertion_sort_nonincreasing(TestCaseWithTime):
    def test_insertion_sort_nonincreasing(self):
        a_list = [5, 2, 4, 6, 1, 3]
        result = [6, 5, 4, 3, 2, 1]
        self.assertEquals(insertion_sort_nonincreasing(a_list), result)
        self.assertEquals(a_list, [5, 2, 4, 6, 1, 3])
