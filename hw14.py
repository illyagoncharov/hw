import requests
import csv

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
            can = cls(*i)
            res_candidates_list.append(can)
        return res_candidates_list

    @classmethod
    def read_the_file(cls, file_name):
        try:
            read_file = cls.open_file(file_name)
        except OSError:
            #print('try open url')
            local_file_name = cls.open_url(file_name)
            read_file = cls.open_file(local_file_name)
        return read_file

    @staticmethod
    def open_file(file_name):
        with open('candidates.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            data_with_candidates = []
            for i in reader:
                data_with_candidates.append(i)
        return data_with_candidates

    @staticmethod
    def open_url(url_adress):
        response = requests.get(url_adress)
        file_name = "urlcandidates.csv"
        open(file_name, "wb").write(response.content)
        return file_name

    @staticmethod
    def create_candidates_list(data_with_candidates):
        for i in data_with_candidates:
            j = i[0].split()
            i.remove(i[0])
            i.insert(0, j[1])
            i.insert(0, j[0])
        data_with_candidates.reverse()
        data_with_candidates.pop()
        return data_with_candidates


adress = 'candidates.csv'
#adress = 'https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv'

print(Candidate.generate_candidates(adress))



