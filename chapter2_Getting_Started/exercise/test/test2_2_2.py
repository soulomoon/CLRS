"""
selection_sort
test for
ex2_2_2.py
"""
from test_with_time import TestCaseWithTime
from chapter2_Getting_Started.exercise.ex2_2_2 import selection_sort

class Test(TestCaseWithTime):
    def test_selection_sort(self):
        a_list = [5, 2, 4, 6, 1, 3]
        result = [1, 2, 3, 4, 5, 6]
        self.assertEquals(selection_sort(a_list), result)
