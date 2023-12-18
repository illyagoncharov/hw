from unittest import TestCase, mock
from hw13 import Employee

class EmployeeTest(TestCase):
    def setUp(self):
        self.employee1 = Employee(name="Ben Gun", salary_for_day=15, email="gun@gmail.com")
        self.employee2 = Employee(name="Tom Red", salary_for_day=10, email="tom@gmail.com")

    def test_work(self):
        self.assertEqual("I come to the office", self.employee1.work())

    def test_check_salary(self):
        days = 5
        self.assertEqual(self.employee1.salary_for_day * days, self.employee1.check_salary(days))

    def test_validate(self):
        correct_email = "g@gmail.com"
        self.assertEqual("g@gmail.com", self.employee1.validate(correct_email))

    def test___gt__(self):
        self.assertTrue(self.employee1.salary_for_day > self.employee2.salary_for_day)

    def test___lt__(self):
        self.assertFalse(self.employee1.salary_for_day < self.employee2.salary_for_day)

    def test___ge__(self):
        self.assertTrue(self.employee1.salary_for_day >= self.employee2.salary_for_day)

    def test___le__(self):
        self.assertFalse(self.employee1.salary_for_day <= self.employee2.salary_for_day)

    def test___eq__(self):
        self.assertFalse(self.employee1.salary_for_day == self.employee2.salary_for_day)

    def test___ne__(self):
        self.assertTrue(self.employee1.salary_for_day != self.employee2.salary_for_day)



