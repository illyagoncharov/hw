from datetime import datetime
from datetime import date
from myerrorsfile import EmailAlreadyExistsExeption
import sys


class Employee:

    email = ''

    def __init__(self, name, salary_for_day, email):
        self.name = name
        self.salary_for_day = salary_for_day
        self.save_email(email)

    def __str__(self):
        return f'{self.__class__.__name__} : {self.name}'

    def __gt__(self, other):
        return self.salary_for_day > other.salary_for_day

    def __lt__(self, other):
        return self.salary_for_day < other.salary_for_day

    def __ge__(self, other):
        return self.salary_for_day >= other.salary_for_day

    def __le__(self, other):
        return self.salary_for_day <= other.salary_for_day

    def __eq__(self, other):
        return self.salary_for_day == other.salary_for_day

    def __ne__(self, other):
        return self.salary_for_day != other.salary_for_day

    def validate(self, email):
        with open('emails.csv', "r") as file_for_email:
            read_file = file_for_email.read()
            if email in read_file:
                raise EmailAlreadyExistsExeption(f'{email} already exists')
            return self

    def save_email(self, email):
            try:
                self.validate(email)
            except EmailAlreadyExistsExeption as error:
                self.write_log(error)
            else:
                self.email = email
                self.write_email()

    def write_log(self, error):
        with open('logs.txt', "a") as logs_file:
            t_now = datetime.now()
            dt_string = t_now.strftime("%d/%m/%Y %H:%M:%S")
            logs_file.write(f'{dt_string} | {sys.exc_info()}\n')

    def write_email(self):
        with open('emails.csv', "a") as file_for_email:
            file_for_email.write(" " + self.email + "\n")

    def __count_work_day(self):
        day = date.today().day
        week_day = date.today().isoweekday()
        res = []
        k = 0
        list_week = [7, 6, 5, 4, 3, 2, 1]
        j = list_week.index(week_day)

        for i in range(day, 0, -1):
            res.append((list_week[j],i))
            if j == 6:
                j = 0
            else:
                j = j+1

        for i in res:
            if i[0] == 7 or i[0] == 6:
                 k += 1

        return len(res) - k

    def check_salary(self, days = None):
        if days is None:
            days = self.__count_work_day()
        return self.salary_for_day * days

    def work(self):
        return 'I come to the office'


class Recruiter(Employee):

    def work(self):
        return f'{super().work()} and start to hiring.'


class Developer(Employee):

    def __init__(self, name, salary_for_day, tech_stack,):
        super().__init__(name, salary_for_day)
        self.tech_stack = tech_stack

    def __gt__(self, other):
        if hasattr(other, 'tech_stack'):
            return len(self.tech_stack) > len(other.tech_stack)
        return super().__gt__(other)

    def __lt__(self, other):
        if hasattr(other, 'tech_stack'):
            return len(self.tech_stack) < len(other.tech_stack)
        return super().__gt__(other)

    def __ge__(self, other):
        if hasattr(other, 'tech_stack'):
            return len(self.tech_stack) >= len(other.tech_stack)
        return super().__gt__(other)

    def __le__(self, other):
        if hasattr(other, 'tech_stack'):
            return len(self.tech_stack) <= len(other.tech_stack)
        return super().__gt__(other)

    def __eq__(self, other):
        if hasattr(other, 'tech_stack'):
            return len(self.tech_stack) == len(other.tech_stack)
        return super().__gt__(other)

    def __ne__(self, other):
        if hasattr(other, 'tech_stack'):
            return len(self.tech_stack) != len(other.tech_stack)
        return super().__gt__(other)

    def __add__(self, other):
        new_tech_stack = list(set(self.tech_stack+other.tech_stack))
        return Developer(self.name + '' + other.name, max(self.salary_for_day, other.salary_for_day), new_tech_stack)

    def work(self):
        return f'{super().work()} and start to coding.'


class EmailAlreadyExistsExeption(Exception):
    pass


tech_stack_1 = ['Algorithms', 'Git', 'Database', 'SQL', 'Aggregation functions', 'Recursion', 'Docker']

tech_stack_2 = ['Algorithms', 'Git', 'Database', 'Aggregation functions', 'Docker', "JS"]

d1 = Developer('Alex', 100, tech_stack_1, 'd3@mail.com')
d2 = Developer('Jack', 120, tech_stack_2, 'd2@mail.com
