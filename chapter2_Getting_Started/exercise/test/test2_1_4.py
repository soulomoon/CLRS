"""Test"""
from test_with_time import TestCaseWithTime
from chapter2_Getting_Started.exercise.ex2_1_4 import add_binary


class Test(TestCaseWithTime):
    """Test"""
    def test_add_binary(self):
        """test_add_binary"""
        a_list = [1, 0, 1, 1, 0]
        b_list = [0, 1, 1, 1, 1]
        result1 = [1, 0, 0, 1, 0, 1]
        result2 = [0, 1, 1, 1, 1, 0]
        self.assertEquals(add_binary(a_list, b_list), result1)
        self.assertEquals(add_binary(b_list, b_list), result2)
        self.assertEquals(add_binary(b_list, result1), None)
