class Empioyee:
    def __init__(self, name, salary_for_day):
        self.name = name
        self.salary_for_day = salary_for_day

    def __str__(self):
        return "{}:{}".format(self.__class__.__name__, self.name,)

    def work(self):
        return 'I come to the office'

    def __gt__(self, other):
        return int(self.salary_for_day) > other.salary_for_day

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


class Recruiter(Empioyee):

    def work(self):
        return f'{super().work()} and start to hiring.'

class Developer(Empioyee):

    def work(self):
        return f'{super().work()} and start to coding.'


d = Developer('Alex', 100)
r = Recruiter('Bohdan', 150)
print(d)
print(r)
print(d > r)
print(r.work())