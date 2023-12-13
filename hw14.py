import requests
import csv
from constants import Indexmodule
from urllib.parse import urlparse

class Candidate:
    list_candidates = []

    def __init__(self, first_name, last_name, email, tech_stack, mail_skill, mail_skill_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tech_stack = tech_stack
        self.mail_skill = mail_skill
        self.mail_skill_grade = mail_skill_grade

    def __repr__(self):
        return "%s %s" % (self.first_name, self.last_name)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def generate_candidates(cls, file_name):
        read_file = cls.read_the_file(file_name)
        data_with_candidates = cls.create_candidates_list(read_file)
        res_candidates_list = []
        for i in data_with_candidates:
            can = cls(**i)
            res_candidates_list.append(can)
        return res_candidates_list

    @classmethod
    def read_the_file(cls, file_name):
        url_parsed = urlparse(file_name)
        if url_parsed.scheme in ('http', 'https'):
            cls.open_url(file_name)
            read_file = cls.open_file(Constans._file_name)
        else:
            read_file = cls.open_file(file_name)
        return read_file

    @staticmethod
    def open_file(file_name):
        with open(file_name, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
            list_candidates = []
            for pow in reader:
                list_candidates.append(pow)
        return list_candidates

    @staticmethod
    def open_url(url_adress):
        response = requests.get(url_adress)
        with open(Constans._file_name,  'wb') as csvfile:
            csvfile.write(response.content)
        return

    @staticmethod
    def create_candidates_list(data_with_candidates):
        candidates = []
        candidate = {}
        for pow in data_with_candidates:
            candidate['first_name'] = pow['Full Name'].split()[Constans.FIRST_NAME_INDEX]
            candidate['last_name'] = pow['Full Name'].split()[Constans.LAST_NAME_INDEX]
            candidate['email'] = pow['Email']
            candidate['tech_stack'] = pow['Technologies']
            candidate['main_skill'] = pow['Main Skill']
            candidate['main_skill_grade'] = pow['Main Skill Grade']
            candidates.append(candidate)
            candidate = candidate.copy()
        return candidates


adress = 'candidates.csv'
#adress = 'https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv'

print(Candidate.generate_candidates(adress))



