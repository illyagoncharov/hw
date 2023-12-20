from datetime import datetime

class Write():
    @staticmethod
    def write(some_str, filename):
        with open(filename, 'a') as some_file:
            some_file.write(some_str)


class Logger():
    filename = "exception_file.txt"

    def write(self, exc_obj):
        t_now = datetime.now()
        dt_string = t_now.strftime("%d-%m-%Y %H:%M:%S")
        count = self.counter()
        Write.write(f'{count} {dt_string} {exc_obj.__class__.__name__} {exc_obj}\n', self.filename)

    def counter(self):
        try:
            with open(self.filename, 'r') as file_:
                read_content = file_.readlines()
                return len(read_content)+1
        except Exception:
                    return 1


def logger(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as exc:
            Logger().write(exc)
    return wrapper


class SomeClass():
    @logger
    def some_func(a,b):
        return a/b

SomeClass.some_func(3,0)






