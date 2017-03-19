from unittest import TestCase

import time


class TestCaseWithTime(TestCase):
    def setUp(self):
        self.start_time = time.time()

    def tearDown(self):
        t = time.time() - self.start_time
        # class_name = self.id().split('.')[-2]
        # method_name = self.id().split('.')[-1]
        # print("%s: %fms." % (class_name+"."+method_name, t))
        print("%s: %fms." % (self.id(), t))
