from unittest import TestCase
from hw14 import Candidate

class CandidateTest(TestCase):

    def setUp(self):
        tech_stack1 = ['Algorithms', 'Git', 'Database', 'Aggregation functions', 'Docker', "JS"]
        self.candidate = Candidate(first_name="John", last_name="Snow" , email="snow@gp.com",
                                   tech_stack=tech_stack1, main_skill = 'Python', main_skill_grade = 'Junior')
        self.file_list = [{'Full Name': 'Ivan Chechov',
                      'Email': 'ichech@example.com',
                      'Technologies': 'Python|Django|Angular',
                      'Main Skill': 'Python',
                      'Main Skill Grade': ' Senior'},
                     {'Full Name': 'Max Payne',
                      'Email': 'mpayne@example.com',
                      'Technologies': 'PHP|Laravel|MySQL',
                      'Main Skill': 'PHP',
                      'Main Skill Grade': 'Middle'},
                     {'Full Name': 'Tom Hanks',
                      'Email': 'thanks@example.com',
                      'Technologies': 'Python|CSS',
                      'Main Skill': 'Python',
                      'Main Skill Grade': 'Junior'}
                     ]


    def test_full_name(self):
        self.assertEqual("John Snow", self.candidate.full_name)

    def test_read_the_file(self):
        adress = 'candidates.csv'

        self.assertEqual(self.file_list, Candidate.read_the_file(adress))

    def test_create_candidates_list(self):
        res_data = [{'first_name': 'Ivan',
                     'last_name': 'Chechov',
                     'email': 'ichech@example.com',
                     'tech_stack': 'Python|Django|Angular',
                     'main_skill': 'Python',
                     'main_skill_grade': ' Senior'},
                    {'first_name': 'Max',
                     'last_name': 'Payne',
                     'email': 'mpayne@example.com',
                     'tech_stack': 'PHP|Laravel|MySQL',
                     'main_skill': 'PHP',
                     'main_skill_grade': 'Middle'},
                    {'first_name': 'Tom',
                     'last_name': 'Hanks',
                     'email': 'thanks@example.com',
                     'tech_stack': 'Python|CSS',
                     'main_skill': 'Python',
                     'main_skill_grade': 'Junior'}]
        self.assertEqual(res_data, Candidate.create_candidates_list(self.file_list))