from . import TestCaseWithTime

from chapter2_Getting_Started.code_from_book.insertion_sort import *


class test_insertion_sort(TestCaseWithTime):
    def test_insertion_sort(self):
        a_list = [5, 2, 4, 6, 1, 3]
        result = [1, 2, 3, 4, 5, 6]
        self.assertEquals(insertion_sort(a_list), result)
        self.assertEquals(a_list, [5, 2, 4, 6, 1, 3])
