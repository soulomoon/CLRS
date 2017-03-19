from test_with_time import TestCaseWithTime
from chapter2_Getting_Started.code_for_practice.Exercises2_1_4 import *


class Exercises2_1_4(TestCaseWithTime):
    def test_add_binary(self):
        a_list = [1, 0, 1, 1, 0]
        b_list = [0, 1, 1, 1, 1]
        result1 = [1, 0, 0, 1, 0, 1]
        result2 = [0, 1, 1, 1, 1, 0]
        self.assertEquals(add_binary(a_list, b_list), result1)
        self.assertEquals(add_binary(b_list, b_list), result2)
