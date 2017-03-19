from test_with_time import TestCaseWithTime
from chapter2_Getting_Started.code_for_practice.Exercises2_1_3 import *


class Exercises2_1_3(TestCaseWithTime):
    def test_search(self):
        a_list = [5, 2, 4, 6, 1, 3]
        a = 2
        b_list = [6, 5, 4, 3, 2, 1]
        b = 10
        self.assertEquals(search(a_list, a), 1)
        self.assertEquals(search(b_list, b), False)
