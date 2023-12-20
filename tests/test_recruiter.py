from unittest import TestCase
from hw13 import Recruiter

class RecruiterTest(TestCase):
    def setUp(self):
        self.recruiter = Recruiter(name="Ben Gun", salary_for_day=10, email="gun@gmail.com")

    def test_work(self):
        self.assertEqual('I come to the office and start to hiring.', self.recruiter.work())