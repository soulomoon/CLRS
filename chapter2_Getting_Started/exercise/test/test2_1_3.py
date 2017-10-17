"""
test
"""
from test_with_time import TestCaseWithTime
from chapter2_Getting_Started.exercise.ex2_1_3 import search


class Test(TestCaseWithTime):
    """Test"""
    def test_search(self):
        """test_search"""
        a_list = [5, 2, 4, 6, 1, 3]
        a_v = 2
        b_list = [6, 5, 4, 3, 2, 1]
        b_v = 10
        self.assertEquals(search(a_list, a_v), 1)
        self.assertEquals(search(b_list, b_v), False)
