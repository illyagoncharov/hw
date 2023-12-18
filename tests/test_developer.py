from unittest import TestCase, mock
from hw13 import Developer

class DeveloperTest(TestCase):

    def setUp(self):
        tech_stack_1 = ['Algorithms', 'Git', 'Database', 'SQL', 'Aggregation functions', 'Recursion', 'Docker']
        tech_stack_2 = ['Algorithms', 'Git', 'Database', 'Aggregation functions', 'Docker', "JS"]
        tech_stack_3 = ['Algorithms', 'Git', 'Database', 'SQL', 'Aggregation functions', 'Recursion', 'Docker', "JS"]
        self.developer1 = Developer(name="Ben", salary_for_day=15, tech_stack=tech_stack_1, email="gun@gmail.com")
        self.developer2 = Developer(name="Tom", salary_for_day=10, tech_stack=tech_stack_2, email="tom@gmail.com")
        self.developer3 = Developer(name="BenTom", salary_for_day=15, tech_stack=tech_stack_3, email="BenTom@gmail.com")

    def test___gt__(self):
        self.assertTrue(len(self.developer1.tech_stack) > len(self.developer2.tech_stack))

    def test___lt__(self):
        self.assertFalse(len(self.developer1.tech_stack) < len(self.developer2.tech_stack))

    def test___ge__(self):
        self.assertTrue(len(self.developer1.tech_stack) >= len(self.developer2.tech_stack))

    def test___le__(self):
        self.assertFalse(len(self.developer1.tech_stack) <= len(self.developer2.tech_stack))

    def test___eq__(self):
        self.assertFalse(len(self.developer1.tech_stack) == len(self.developer2.tech_stack))

    def test___ne__(self):
        self.assertTrue(len(self.developer1.tech_stack) != len(self.developer2.tech_stack))

    def test___add__(self):
        tech_stack_3 = ['Algorithms', 'Git', 'Database', 'SQL', 'Aggregation functions', 'Recursion', 'Docker', "JS"]
        self.assertEqual(set(tech_stack_3), set(self.developer1.tech_stack+self.developer2.tech_stack))
        self.assertEqual(self.developer3, (self.developer1+self.developer2))


