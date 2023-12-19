from datetime import datetime
from datetime import date
import sys

class Write():
    def write(self, some_str, filename):
        with open(filename, 'a') as some_file:
            some_file.write(some_str)


class Logger(Write):
    filename = "exception_file.txt"
    def write(self):
        print("ddd")
        t_now = datetime.now()
        dt_string = t_now.strftime("%d-%m-%Y %H:%M:%S")
        super().write(f'{dt_string} | {sys.exc_info()[1]}\n', self.filename)


class Decorator():
    def __init__(self, func):
        self.func = func
    def __call__(self, *args):
        print("The call start")
        try:
            self.func(*args)
        except Exception as exc:
            Logger().write()
            print("The call stop another")







