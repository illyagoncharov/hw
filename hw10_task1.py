class Phone:
    number = '___12312312'
    _counter = 0

    def set_phone_number(self, new_number):
        self.number = new_number
        return self.number

    def get_accept_call_count(self):
        return self._counter

    def accept_call(self):
        print("phone:", self.number, "call accepted")
        self._counter = self._counter +1


phone1 = Phone()
phone1.set_phone_number("(067)12312312")
phone2 = Phone()
phone2.set_phone_number("(050)12312312")
phone3 = Phone()
phone3.set_phone_number("(063)12312312")

for i in range(1,3):
    phone1.accept_call()
    for j in range(1,3):
        phone2.accept_call()
        for k in range(1,3):
            phone3.accept_call()
print("phone 1 - ", phone1.get_accept_call_count())
print("phone 2 - ", phone2.get_accept_call_count())
print("phone 3 - ", phone3.get_accept_call_count())
phone_list = [phone1, phone2, phone3]

def call_sum(list_phone):
    sum_call = 0
    for i in list_phone:
        sum_call += i.get_accept_call_count()
    print("Number of input calls ", sum_call)
    with open("sumcall.csv", "w") as file1:
        file1.write(f"Number of input calls {sum_call}")
    return sum_call

call_sum(phone_list)


