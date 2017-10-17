from test_with_time import TestCaseWithTime
from chapter2_Getting_Started.exercise.ex2_1_2 import insertion_sort_nonincreasing


class Test(TestCaseWithTime):
    def test_insertion_sort_nonincreasing(self):
        a_list = [5, 2, 4, 6, 1, 3]
        result = [6, 5, 4, 3, 2, 1]
        self.assertEquals(insertion_sort_nonincreasing(a_list), result)
        self.assertEquals(a_list, [5, 2, 4, 6, 1, 3])
