from unittest import TestCase

import time


class TestCaseWithTime(TestCase):
    def setUp(self):
        self.start_time = time.time()

    def tearDown(self):
        t = time.time() - self.start_time
        print("%s: %fms." % (self.id(), t))
