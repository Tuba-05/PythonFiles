# LAB NO # 1:
#Q1
# class Bank:
#     def __init__(self, loan_taken_previously):
#         self.loan_taken_previously = loan_taken_previously
#     def application_for_loan(self):
#         if self.loan_taken_previously == True:
#             print('loan granted')
#         else:
#             print('loan is not granted')
# Person1 = Bank(True)
# Person1.application_for_loan()
# Person2 = Bank(False)
# Person2.application_for_loan()

# Q2:
# class Complex:
#     def __init__(self):
#         self.real = input('enter real number:')
#         self.imaginary = input('enter imaginary number:')
#     def complex_no_(self):
#         print(self.real,'+',self.imaginary)
# num1 = Complex()
# num1.complex_no_()

# Q3:
# class Snake:
#     def introduction(self, name, color, age):
#         self.name = name
#         self.color = color
#         self.age = age
#         print('snake name is', self.name, 'color is', self.color, 'and age is', self.age)
#
# name = input('enter snake name:')
# color = input('enter snake color:')
# age = input('enter snake age:')
# s1 = Snake()
# s1.introduction(name, color, age)
#
# Q4:
# class Car:
#    def __init__(self, wheel, miles, make, model, year, sold_on):
#        self.wheel = wheel
#        self.miles = miles
#        self.make= make
#        self.model = model
#        self.year = year
#        self.sold_on = sold_on
#
#    def sales_price(self, sold_on):
#        if sold_on == 'none':
#           return self.make
#        else:
#           return 0
#
#    def purchase_price(self, sold_on):
#        if sold_on == 'none':
#           return 0
#        else:
#           return self.make
# Car1 = Car(4, 500 ,900000, 'Mercedes', 2021, 'none')
# print(Car1.purchase_price('none'))
# print(Car1.sales_price('none'))

# LAB8:
# from abc import ABCMeta, abstractmethod
# class Super(metaclass=ABCMeta):
#     def delegate(self):
#         self.action()
#     @abstractmethod
#     def action(self):
#         return 'super class'
#
#
# class Sub(Super):
#     def action(self):
#         return 'sub class'
#
#
# X = Sub()
# print(X.action())

# from abc import ABC, abstractmethod
# class Vehicle(ABC):
#     def __init__(self,c ,e):
#         self.company = c
#         self.engine_oil= e
#     @abstractmethod
#     def method(self):
#         return 'oops'
#
# class Car(Vehicle):
#     def __init__(self,c, e, w, s):
#         super().__init__(c,e)
#         self.wheels = w
#         self.no_plate = s
#     def method(self):
#         return f'Car: \ncompany:{self.company} \nengine oil:{self.engine_oil} \nnumber of wheels:{self.wheels}' \
#                f'\nnumber plate:{self.no_plate}'
# class Bike(Vehicle):
#     def __init__(self,c, e, w, s):
#         super().__init__(c,e)
#         self.wheels = w
#         self.no_plate = s
#     def method(self):
#         return f'Bike: \ncompany:{self.company} \nengine oil:{self.engine_oil} \nnumber of wheels:{self.wheels}' \
#                f'\nnumber plate:{self.no_plate}'
# class Truck(Vehicle):
#     def __init__(self,c, e, w, s):
#         super().__init__(c,e)
#         self.wheels = w
#         self.no_plate = s
#     def method(self):
#         return f'Truck: \ncompany:{self.company} \nengine oil:{self.engine_oil} \nnumber of wheels:{self.wheels}' \
#                f'\nnumber plate:{self.no_plate}'
#
#
# C = Car("Suzuki",'Castrol GTX Magnatec','4','BDC999')
# print(C.method())
# B = Bike("Suzuki",'Castrol GTX Magnatec','2','KEDO184')
# print(B.method())
# T = Truck("Suzuki",'Castrol GTX Magnatec','6','YYX597')
# print(T.method())

# from abc import ABC, abstractmethod
# class AbstractCalculator(ABC):
#     def __init__(self, n1, n2):
#         self.n1 = n1
#         self.n2 = n2
#     @abstractmethod
#     def M_operation(self):
#         return f'n1:{self.n1} \n n2:{self.n2}'
#
# class Addition_operation(AbstractCalculator):
#     def M_operation(self):
#         return f'n1+n2 = {self.n1 + self.n2}'
#
#
# class Subtraction_operation(AbstractCalculator):
#     def M_operation(self):
#         return f'n1-n2 = {self.n1 - self.n2}'
#
#
# class Multiplication_operation(AbstractCalculator):
#     def M_operation(self):
#         return f'n1*n2 = {self.n1 * self.n2}'
#
#
# class Division_operation(AbstractCalculator):
#     def M_operation(self):
#         if self.n2 != 0:
#             return f'n1/n2 = {self.n1 / self.n2}'
#         else:
#             return f'setting n2 =1 \n n1 /n2:{self.n1}'
#
#
# A = Addition_operation(55,5)
# print(A.M_operation())
# S = Subtraction_operation(55,5)
# print(S.M_operation())
# M = Multiplication_operation(55,5)
# print(M.M_operation())
# D = Division_operation(55,5)
# print(D.M_operation())

# LAB10:
# from abc import ABC,abstractmethod
# class Animal(ABC):
#     def __init__(self, n):
#         self.n = n
#     @abstractmethod
#     def talk(self):
#         pass
# class Cat(Animal):
#     def __init__(self,n):
#         super().__init__(n)
#     def talk(self):
#         return f'{self.n}: meow'
# class Dog(Animal):
#     def __init__(self,n):
#         super().__init__(n)
#     def talk(self):
#         return f'{self.n}: woof'
# C = Cat('abc')
# print(C.talk())
# D = Dog('xyz')
# print(D.talk())

# from abc import ABC,abstractmethod
# class Person(ABC):
#     total_price = 50000
#     @abstractmethod
#     def ticket_price(self):
#         pass
#
#
# class employed_person(Person):
# # concession for employed person is 25%
#     def ticket_price(self):
#         concessionary_price = self.total_price - (self.total_price * 0.25)
#         return concessionary_price
#
#
# class student(Person):
# # concession for student is 50%
#     def ticket_price(self):
#         concessionary_price = self.total_price - (self.total_price * 0.5)
#         return concessionary_price
#
#
# ep = employed_person()
# print(ep.ticket_price())
# st = student()
# print(st.ticket_price())

# LAB 9:
# def divide(x,y):
#     print(x/y)
# divide(4,2)

# def check(func):
#     def wrapper(x,y):
#         if y == 0:
#             print('division can not be zero')
#         else:
#             func(x,y)
#     return wrapper
# @check
# def divide(x,y):
#     print(x/y)
# divide(4,2)
# divide(4,0)

# LAB 11:
# try:
#     ed = int(input('years of education:'))
#     assert  ed > 16
# except ValueError:
#     print('ERROR: invalid value foe int type.')
# except:
#     print('Education not enough.')
# else:
#     print('Your are eligible.')

# def smart_division():
#     try:
#         num = int(input('numerator:'))
#         den = int(input('denominator:'))
#         assert den != 0
#     except ValueError:
#         print('Invalid value entered.')
#     except:
#         print('Zero division error.')
#     else:
#         print(num/den)
# smart_division()

# def factorial():
#     try:
#         n = int(input('number:'))
#         assert n > 0
#     except ValueError:
#         print('Invalid value error occured.')
#     except:
#         print(' Zero & negative integers are not allowed.')
#     else:
#         fact = 1
#         while n > 1:
#             fact *= n
#             n -= 1
#             print(fact)
# factorial()

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
