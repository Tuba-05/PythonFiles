# class Bleh:
#     def _init_(self, brainy):
#         self.brainy = brainy
#
#     sad = ""
#     idiot = "Yes"
#
#     @classmethod
#     def class_method(cls, sad):
#         print(f"Is Taiba sad? : {sad}")
#         print(f"Is Taiba an idiot? {cls.idiot}")
#
#     @staticmethod
#     def static_method(value):
#         if value >= 18:
#             return "In university"
#         else:
#             return "In school"
#
#
# waku = 2
# Bleh.class_method("yes")
# print(Bleh.static_method(waku))
#
# print("\n'new code:-'\n")
#
# class Bleh:
#     sad = ""
#     idiot = "Yes"
#
#     @classmethod
#     def class_method(cls, sad):
#         print(f"Is Tuba sad? : {sad}")
#         print(f"Is Tuba an idiot? {cls.idiot}")
#
#     @staticmethod
#     def static_method(value):
#         if value >= 18:
#             return "In university"
#         else:
#             return "In college"
#
#
# waku = 2
# Bleh.class_method("yes")
# print(Bleh.static_method(21))


# class BankAccount:
#     BankAccounts = 0
#     def __init__(self, balance = 0):
#         self.balance = balance
#     def deposit_amount(self, d):
#         self.amount_deposit = d
#         return f'balance:{self.balance + self.amount_deposit}'
#     def withdrawAmount(self, w):
#         self.withdraw_amount = w
#         if w <= self.balance:
#             return f'balance:{self.balance - self.withdraw_amount}'
#         else:
#             return 'the amount you entered is more than your balance'
#     @classmethod
#     def get_total_amount(cls):
#         cls.BankAccounts += 1
#         return f'total no. of bank accounts:{cls.BankAccounts}'
#
#     @staticmethod
#     def Bank_policy():
#         return "Ahzam bhai will tell bank's policy"
#
#
# print(BankAccount.Bank_policy())
# A1 = BankAccount(500)
# A2 = BankAccount(1000)
# print(A1.withdrawAmount(200),'\n', BankAccount.get_total_amount())
# print(A2.withdrawAmount(500),'\n', BankAccount.get_total_amount())

# class library:
#     total_books = 0
#     b = []
#     def __init__(self, name):
#         self.name = name
#     def add_book(self,b_name):
#         if library.total_books >= 0:
#             library.total_books += 1
#         else:
#             library.total_books = 0
#         self.book_name = b_name
#         if self.book_name not in library.b:
#             library.b.append(self.book_name)
#         else:
#             print('the book you entered already exits')
#     def remove_book(self, b_name):
#         if library.total_books > 0:
#             library.total_books -= 1
#         else:
#             library.total_books = 0
#         self.book_name = b_name
#         if self.book_name in library.b:
#             library.b.remove(self.book_name)
#         else:
#             print('the book you entered has already been removed')
#     @classmethod
#     def get_total_books(cls):
#         return f'total number of books:{cls.total_books}'
#
#     @staticmethod
#     def library_policy():
#         print("Ahzam bhai will tell libray policy.")
#
#
# l = library('"My library"')
# print(l.name)
# l.library_policy()
# l.add_book('Book1')
# l.add_book('Book2')
# l.add_book('Book3')
# l.add_book('Book4')
# print(l.get_total_books(),'\n', library.b)
# l.remove_book('Book4')
# print(l.get_total_books(),'\n', library.b)

# CLO3 SET NO.1:
# QUESTION NO.1:
class PhoneBook(list):
    def create_contacts_list(self, name, age, country):
        self.contacts = PhoneBook()
        self.name = name
        self.age = age
        self.country = country

    def add_contacts(self):  # adding contacts in list
        self.contacts.append([self.name, self.age, self.country])

    def sort_list(self):  # sorting list
        self.contacts.sort()

    def __str__(self):  # print in string
        strl_ = 'Name,Age,Country\n'
        for data in self:
            strl_ += f"{data[0]}, {data[1]}, {data[2]}\n"
        return strl_

    def search(self, name):
        contacts_found = PhoneBook()
        for item in self:
            if name in item[0]:
                contacts_found.append(item)
        return contacts_found


class ProtectedPhoneBook(PhoneBook):
    def pop(self, *args, **kwargs):
        print("Not allowed to do that")

    def remove(self, *args, **kwargs):
        print("Not allowed to do that")


# p = ProtectedPhoneBook()
# p.create_contacts_list('taiba', '12', 'pk')
# p.add_contacts()
# p.create_contacts_list('saad', '20', 'pk')
# p.add_contacts()
# print(p)
# p.pop()
# p.remove("taiba")
# print(p)


# QUESTION NO.2-4: QUESTION NO.5: used aggregation/composition in Sales class
# class Publication:
#     title = ''
#     price = ''
#     def get_data(self):
#         Publication.title = input('Book name:')
#         Publication.price = float(input('Book price:'))
#
#     def put_data(self):
#         print('Book name:',self.title ,'\nPrice:', self.price)
#
#
# class Sales:
#     records = []
#     def get_data(self):
#         for i in range(1,4):
#             i = float(input('Publication of 1st month:'))
#             self.records.append(i)
#         return self.records
#
#     def put_data(self):
#         print('Publications:\nFirst month:',self.records[0],'\nSecond month:'
#                ,self.records[1],'\nThird month:',self.records[2])
#
#
# class Book(Publication, Sales):
#     def get_data(self):
#         Publication().get_data()
#         self.page_count = int(input('Number of pages:'))
#         Sales().get_data()
#
#     def put_data(self):
#         Publication().put_data()
#         print('Page Count:', self.page_count,)
#         Sales().put_data()
#
#
# class Tape(Publication, Sales):
#     def get_data(self):
#         Publication().get_data()
#         self.playing_time = float(input('Playing time:'))
#         Sales().get_data()
#
#     def put_data(self):
#         Publication().put_data()
#         print('Playing Time:',self.playing_time)
#         Sales().put_data()
#
#
# class Disk(Publication):
#     def get_data(self):
#         self.d = {'C': 'CD', 'D': 'DVD'}
#         self.disk_type = ''
#         Publication().get_data()
#         choice = input("choose:\nC for 'CD'\nD for 'DVD'").upper()
#         if choice == 'C':
#             self.disk_type = self.d.get('C')
#         elif choice == 'D':
#             self.disk_type = self.d.get('D')
#         else:
#             print('Restart prg.')
#             exit()
#
#     def put_data(self):
#         Publication().put_data()
#         print('Disk type:', self.disk_type)
#

# b = Book()
# b.get_data()
# b.put_data()
# t = Tape()
# t.get_data()
# t.put_data()
# d = Disk()
# d.get_data()
# d.put_data()

# QUESTION NO.6-7:
# class Date:
#     format = ''
#     month_name = ''
#     d = { '01':'January', '02':'February' , '03':'March' , '04':'April' , '05':'May' ,
#           '06':'June' , '07':'July' , '08':'August' , '09':'September' , '10':'October'
#           , '11':'November' , '12':'December'}
#
#     def get(self):
#         self.date = input('Date:')
#         self.month = input('Month:')
#         self.year = input('Year:')
#
#     def set(self, dd, mon , yr ):
#         self.date = dd
#         self.month = mon
#         self.year = yr
#
#     def __str__(self):
#         choice = input('1. dd-mm-yy\n2. mm/dd/yy\n3. mm_name dd,yy\n'
#                        'enter your choice for date format:')
#         if choice == '1':
#             Date.format = 'dd-mm-yy'
#             return f"{Date.format} = {self.date}-{self.month}-{self.year}"
#         elif choice == '2':
#             Date.format = 'mm/dd/yy'
#             return f"{Date.format} = {self.month}/{self.date}/{self.year}"
#         elif choice == '3':
#             Date.format = 'mm_name dd,yy'
#             for key in Date.d:
#                 if key == self.month:
#                     Date.month_name = Date.d.get(key)
#             return f"{Date.format} = {Date.month_name} {self.date},{self.year}"


# d = Date()
# d.get()
# print(d)

# QUESTION NO.8-9":
class Date:
    format = ''
    month_name = ''
    d = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May',
         '06': 'June', '07': 'July', '08': 'August', '09': 'September', '10': 'October',
         '11': 'November', '12': 'December'}

    def get(self):
        self.date = input('Date:')
        self.month = input('Month:')
        self.year = input('Year:')

    def set(self, dd, mon, yr):
        self.date = dd
        self.month = mon
        self.year = yr

    def __str__(self):
        choice = input('1. dd-mm-yy\n2. mm/dd/yy\n3. mm_name dd,yy\n'
                       'enter your choice for date format:')
        if choice == '1':
            Date.format = 'dd-mm-yy'
            return f"Publication date:\n{Date.format} = " \
                   f"{self.date}-{self.month}-{self.year}"
        elif choice == '2':
            Date.format = 'mm/dd/yy'
            return f"Publication date:\n{Date.format} = " \
                   f"{self.month}/{self.date}/{self.year}"
        elif choice == '3':
            Date.format = 'mm_name dd,yy'
            for key in Date.d:
                if key == self.month:
                    Date.month_name = Date.d.get(key)
            return f"Publication date:\n{Date.format} = " \
                   f"{Date.month_name} {self.date},{self.year}"


class Publication:
    title = ''
    price = ''

    def get_data(self):
        Publication.title = input('Book name:')
        Publication.price = float(input('Book price:'))

    def put_data(self):
        print('Book name:', self.title, '\nPrice:', self.price)


class Book(Publication):
    Book_no = 0

    def get_data(self):
        Publication().get_data()
        self.page_count = int(input('Number of pages:'))

    def put_data(self):
        d = Date()
        d.get()
        Book.Book_no += 1
        print(d, '\nBook number:', Book.Book_no)
        Publication().put_data()
        print('Page Count:', self.page_count,)


class Tape(Publication):
    Tape_no = 0

    def get_data(self):
        Publication().get_data()
        self.playing_time = float(input('Playing time:'))

    def put_data(self):
        d = Date()
        d.get()
        Tape.Tape_no += 1
        print(d, '\nBook number:', Tape.Tape_no)
        Publication().put_data()
        print('Playing Time:', self.playing_time)


# b = Book()
# b.get_data()
# b.put_data()
# t = Tape()
# t.get_data()
# t.put_data()

x = 1


def nester():  # output order: 1,1,1,1,3
    print(x)

    class C:
        print(x)

        def m1(self):
            print(x)

        def m2(self):
            x = 3
            print(x)
    i = C()
    i.m1()
    i.m2()


# print(x)
# nester()


# class A:
#     def m(self):
#         print('in a')
#
#
# class B:
#     def m(self):
#         print('in b')
#
#
# class C:
#     def m(self):
#         print('in c')
#
#
# class X(A, B, C):
#     def m(self):
#         print('in x')
#
#
# class Y(A, B, C):
#     def m(self):
#         print('in y')
#
#
# class Z(X, Y, C):
#     def m(self):
#         print('in z')
#
#
# z = Z()
# z.m()  # in z
# print(Z.mro())  # Z,X,Y,A,B,C

def star(func):
    def inner(a):
        print('x' * 5)
        func(a)
        print('x' * 5)
    return inner


def percent(func):
    def inner(a):
        print('T' * 5)
        func(a)
        print('T' * 5)
    return inner


@star
@percent
def printer(msg):
    print(msg)


# printer('hello')

class A:
    def m(self):
        print('in A')


class C:
    def m(self):
        print('in C')


class X(A, C):
    pass


class Y(A):
    def m(self):
        print('in Y')


class Z(X, Y):
    pass


# z = Z()
# z.m()
# print(Z.mro())

# class Age:
#     def __init__(self, age):
#         self.age = age
#
#     def __add__(self, other):
#         if isinstance(other, Age):
#             return Age(self.age + other.age)
#
#     def __invert__(self):
#         return -self.age
#
#
# a1 = Age(19)
# a2 = Age(20)
# print(a1 + a2)
# sum = ~ (a1 + a2)
# print(sum)

# def count(myfunc):
#     def wrapper():
#         wrapper.count += 1
#         result = myfunc()
#         return result
#     wrapper.count = 0
#     return wrapper
#
# @count
# def myfunc():
#     pass
#
#
# if __name__ == "__main__":
#     for i in range(5):
#         myfunc()
#     print('function "myfunc" called', myfunc.count, 'times')
#
# try:
#     lst = [0, 0, 0, 0]
#     with open('data.txt', 'r') as f:
#         count = 0
#         for line in f.readlines():
#             print(line)
#             lst[count] = float(line)
#             count += 1
# except ValueError:
#     print('value error')

# def func():
#     l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 4, 3, 6, 'shaj', ]
#     l2 = []
#     count = 0
#     for i in l:
#         if i not in l2:
#             count += 1
#             l2.append(i)
#     print(l2, count)
# func()
# print(gc.isenabled())

# class Dietplan:
#     ingredients = {}
#
#     def __init__(self, ingredient="none", quantity=0, units="none"):
#         self.ingredient = str(ingredient)
#         self.quantity = float(quantity)
#         self.units = str(units)
#
#         if self.ingredient in Dietplan.ingredients:
#             Dietplan.ingredients[self.ingredient] += 1
#         else:
#             Dietplan.ingredients[self.ingredient] = 1
#
#     def __str__(self):
#         return f"{self.ingredient}: {self.quantity} {self.units}"
#
#     def display(self):
#         for key, value in Dietplan.ingredients.items():
#             print(f"{key} : {value}")
#
#
# d = Dietplan('xyz', 86, 'xyz')
# d = Dietplan('a', 1, 'a')
# d = Dietplan('c', 3, 'c')
# d = Dietplan('b', 2, 'c')
# d = Dietplan('c', 3, 'c')
# d.display()
# print(d)
# class Error(Exception):
#     pass
# try:
#     age=int(input('age:'))
#     if age <= 0:
#         raise Error
#     if age % 2 == 0:
#         print('even')
#     else:
#         print('odd')
# except ValueError:
#     print('invalid value')
# except Error:
#     print('age can not be zero.')
# else:
#     print(age)
#
# def squared(func):
#     return lambda x:func(x)*func(x)
# def x_times_3(x):
#     return 3*x
# x_times_3=squared(x_times_3)
#
# print(x_times_3(2))
#
# def x_minus_1(x):
#     return x-1
# x_minus_1=squared(x_minus_1)
# print(x_minus_1(3))
# class Error(Exception):
#     pass
# try:
#     ed = int(input('Education years:'))
#     if ed <= 16:
#         raise Error
#     print('you are eligible.')
# except Error:
#     print('this a custom exception.')
# except ValueError:
#     print('oops! there occurs a value error.')
# Error()

# x='Global'
# class A:
#    x='ClassA'
#    def methodA(self):
#       x='MethodA'
#       v=self.B()
#       v.methodB()
#    class B:
#       x='ClassB'
#       def methodB(self):
#        #  x='MethodB'
         # print(x)
# a=A()
# a.methodA()
