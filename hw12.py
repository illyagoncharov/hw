from datetime import date
#--------------------------------------------
class Employee:

    def __init__(self, name, salary_for_day):
        self.name = name
        self.salary_for_day = salary_for_day

    def __count_work_day():
        day = date.today().day
        week_day = date.today().isoweekday()
        res = []
        k = 0
        list_week = [7,6,5,4,3,2,1]
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


    def check_salary(self, days = __count_work_day()):
        return self.salary_for_day * days

    def __str__(self):
        return f'{self.__class__.__name__} : {self.name}'

    def work(self):
        return 'I come to the office'

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
#-------------------------------------

class Recruiter(Employee):

    def work(self):
        return f'{super().work()} and start to hiring.'

#---------------------------------------
class Developer(Employee):

    def __init__(self, name, salary_for_day, tech_stack):
        super().__init__(name, salary_for_day)
        self.tech_stack = tech_stack


    def work(self):
        return f'{super().work()} and start to coding.'

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
        new_tech_stack = self.tech_stack.copy()
        new_tech_stack.extend(other.tech_stack)
        new_tech_stack = list(set(new_tech_stack))
        return Developer(self.name + '' + other.name, max(self.salary_for_day, other.salary_for_day), new_tech_stack)

#-------------------------------------------------------

tech_stack_1 = ['Algorithms', 'Git', 'Database', 'SQL', 'Aggregation functions', 'Recursion', 'Docker']

tech_stack_2 = ['Algorithms', 'Git', 'Database', 'Aggregation functions', 'Docker', "JS"]

d1 = Developer('Alex', 100, tech_stack_1)
d2 = Developer('Jack', 120, tech_stack_2)
r = Recruiter('Bohdan', 150)

d3 = d1 + d2 # new object class Developer
print(d1 > r) # salary_for_day
print(d2 < d3) # tech_stack
print(d3.tech_stack)
print(d2)
print(d1.check_salary(5))
print(d3.check_salary())