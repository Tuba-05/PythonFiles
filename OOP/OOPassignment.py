print("OUTPUT:")
# QUESTION NO.1:
#
# class Circle:
#     radius = 8
#     color = 'red'
#
#     def set_radius(self, radius):
#         self.radius = radius
#
#     def set_color(self, color):
#         self.color = color
#
#     def get_radius(self):
#         print( "Radius:",self.radius)
#
#     def get_color(self):
#         print ("Color:",self.color)
#
#     def get_circumference(self):
#         return 2 * 3.142 * float(self.radius)
#
#     def get_area(self):
#         return 3.142 * (float(self.radius)**2)
# Driver Code:
# C1 = Circle()
# C1.set_radius(4)
# C1.set_color('green')
# C1.get_radius()
# C1.get_color()
# print('Circumference of circle:',C1.get_circumference())
# print('Area of circle:',C1.get_area())

# QUESTION NO.2:
# class BankAccount:
#     def withdraw_(self):
#         amount_in_account = 500000
#         withdrawal_money = int(input('Enter amount you want to withdraw:'))
#         self.amount_left = int(amount_in_account - withdrawal_money)
#
#     def deposit_(self):
#         amount_in_account = 500000
#         deposited_money = int(input('Enter amount you want to deposit:'))
#         self.amount_left = int(amount_in_account + deposited_money)
#
#     def balance_(self):
#         print(f' your current account balance is', end=" ")
#         return self.amount_left
#
#
# Driver Code:
# print(f'Current Account Balance: 500000 \n Choose options:\n 1.To withdraw money form your account'
#       f' \n 2.To deposit money form your account')
# choice = input("Enter your choice:")
# if choice == "1":
#     P1 = BankAccount()
#     P1.withdraw_()
#     print(P1.balance_())
# elif choice == "2":
#     P1 = BankAccount()
#     P1.deposit_()
#     print(P1.balance_())
# else:
#     print("")
#
# QUESTION NO.3:
# class BankAccount:
#     def withdraw_(self, w):
#         __amount_in_account = 500000
#         __withdrawal_money = w
#         self.__amount_left = int(__amount_in_account - __withdrawal_money)
#
#     def deposit_(self, d):
#         __amount_in_account = 500000
#         __deposited_money = d
#         self.__amount_left = int(__amount_in_account + __deposited_money)
#
#     def balance_(self):
#         print(f' your current account balance is', end=" ")
#         return self.__amount_left
#
#
# # Driver Code:
# print(f'Current Account Balance: 500000 \n Choose options:\n '
#       f'1.To withdraw money form your account \n '
#       f'2.To deposit money form your account')
# choice = input("Enter your choice:")
# if choice == "1":
#     P1 = BankAccount()
#     P1.withdraw_(4246)
#     print(P1.balance_())
# elif choice == "2":
#     P1 = BankAccount()
#     P1.deposit_(5463)
#     print(P1.balance_())
# else:
#     print("")
#
# QUESTION NO.4:
# class Worker:
#     __hours_worked = 5
#     __wage_rate = 5000
#
#     def set_hours_worked(self,h):
#         self.__hours_worked = h
#
#     def change_rate(self,r):
#         self.__wage_rate = r
#
#     def pay(self):
#         return self.__hours_worked * self.__wage_rate
#
#
# Driver Code:
# W1 = Worker()
# W1.set_hours_worked(5)
# W1.change_rate(3000)
# print("worker payment:",W1.pay())
#
# QUESTION NO.5:
# class Worker:
#     __hours_worked = 5
#     __wage_rate = 5000
#
#     def __init__(self, h, r):
#         self.__hours_worked = h
#
#         self.__wage_rate = r
#     def hours_worked(self):
#         return self.__hours_worked
#
#     def change_rate(self):
#         return self.__wage_rate
#
#     def pay(self):
#         return self.__hours_worked * self.__wage_rate
#
#
# Driver Code:
# W1 = Worker(9, 9000)
# print("Worker payment:",W1.pay())
#
# QUESTION NO.6:
# class Vehicle:
#     __no_of_wheels = ' 4 '
#     __color = 'Grey'
#     __model_no = 'Supra'
#
#     def set_no_of_wheels(self, w):
#         self.__no_of_wheels = w
#
#     def set_color(self, c):
#         self.__color = c
#
#     def set_model_no(self, m):
#         self.__model_no = m
#
#     def get_no_of_wheels(self):
#         return self.__no_of_wheels
#
#     def get_color(self):
#         return self.__color
#
#     def get_model_no(self):
#         return self.__model_no
#
#
# Driver Code:
# C1 = Vehicle()
# C1.set_color('Purple')
# C1.set_model_no('Ferrari')
# print("CAR:-",'\n',"Number of wheels:",C1.get_no_of_wheels(),'\n'
#       ,"Color:",C1.get_color(),'\n',"Model:",C1.get_model_no())
#
# QUESTION NO.7:
# class Engine:
#     __engine_no = ' F140'
#     __date_of_manufacture = '01-12-2009'
#
#     def set_engine_no(self, e):
#         self.__engine_no = e
#
#     def set_date_of_manufacture(self, d):
#         self.__date_of_manufacture = d
#
#     def get_engine_no(self):
#         return self.__engine_no
#
#     def get_date_of_manufacture(self):
#         return self.__date_of_manufacture
#
#
# Driver Code:
# E1 = Engine()
# E1.set_engine_no(' V12')
# E1.set_date_of_manufacture('1-12-2019')
# print("CAR:-",'\n',"Engine number:",E1.get_engine_no(), '\n',
#       "Date of manufacture:",E1.get_date_of_manufacture())
#
# QUESTION NO.8:
# class Int:
#     def __init__(self, var1=0, var2=0):
#         self.var1 = var1
#         self.var2 = var2
#
#     def set_integers_value(self, v1, v2):
#         self.var1 = v1
#         self.var2 = v2
#
#     def display(self):
#         print('variable_1 =', self.var1 ,'\n','variable_2 =', self.var2)
#
#
#Driver Code:
# I = Int()
# I.set_integers_value(5,9)
# I.display()
#
# QUESTION NO.9:
# class TollBooth:
#     pay = 0
#     non_pay = 0
#     def __init__(self, c=0, m=0):
#         self.total_no_of_cars = c
#         self.total_money = m
#
#     def paying_car(self):
#         self.total_no_of_cars += 1
#
#         TollBooth.pay += 1
#         self.total_money += 50
#         print('total paying cars:', self.pay ,'\n' , 'total cash:' , self.total_money)
#
#     def non_paying_car(self):
#         self.total_no_of_cars += 1
#         TollBooth.non_pay += 1
#         print('total non paying cars:' , self.non_pay)
#
#     def display(self):
#         print('total cars:' , self.pay + self.non_pay, '\n' , 'total paying cars:', self.pay ,
#         '\n' , 'total non paying cars:' , self.non_pay, '\n' , 'total cash:' , self.total_money * self.pay)
#
#
# Driver Code:
# T = TollBooth()
# T.paying_car()
# s = TollBooth()
# s.paying_car()
# s.non_paying_car()
# print(f'Choose an option to display result: \n 1.Paying cars result: \n'
#       f' 2.Non_paying cars result\n 3.Overall result')
# choice = input('Enter your choice:')
# if choice == '1':
#     print("total number of payed cars:",TollBooth.pay)
#
# elif choice == '2':
#     print("total number of non-payed cars:",TollBooth.non_pay)
#
# elif choice == '3':
#     print(T.display())
# else:
#     print("")
#
# QUESTION NO.10:
# class Time:
#     def __init__(self, h=0, m=0, s=0):
#         self.hour = h
#         self.minute = m
#         self.second = s
#
#     def display_time(self):
#         print(self.hour, ":" , self.minute , ":" , self.second)
#
#     def add_time(self, t):
#         self.second += t.second
#         if self.second >= 60:
#             self.second -= 60
#             self.minute += 1
#         self.minute += t.minute
#         if self.minute >= 60:
#             self.minute -= 60
#             self.hour += 1
#         self.hour += t.hour
#         if self.hour >= 24:
#             self.hour -= 24
#
#
# Driver Code:
# print('t1:',end=" ")
# t1 = Time(5,35,56)
# t1.display_time()
# print('t2:',end=" ")
# t2 = Time(24,56,45)
# t2.display_time()
# t1.add_time(t2)
# t1.display_time()
#
# QUESTION NO.11:
# class angle:
#     def __init__(self, deg, min, dir):
#         self.degree = deg
#         self.minute = min
#         self.direction = dir.upper()
#
#     def display(self):
#         print(str(self.degree)+chr(176)+str(self.minute)+"'"+self.direction)
#
#
# Driver Code:
# Q = angle(23, 65, 'W')
# Q.display()
# l = ''
# while True:
#     print(f"Do you want to change the angle value? \n If yes press 'Y' or 'N' for Exit")
#     choice = input("enter your choice:").upper()
#     if choice == 'Y':
#         a = int(input('enter value for degree:'))
#         b = float(input('enter minute:'))
#         c = str(input('enter direction:')).upper()
#         l = str(a)+chr(176)+str(b)+"'"+c
#         print(l)
#
#     else:
#         break
#
# QUESTION NO.12:
# class Tracker:
#     count = 0
#     def __init__(self):
#         self.serial_no = Tracker.count + 1
#         Tracker.count +=1
#
#     def report_serial(self):
#         print("I am object number", self.serial_no)
#
#
# Driver Code:
# tr1 = Tracker()
# tr1.report_serial()
# tr2 = Tracker()
# tr2.report_serial()
#
# QUESTION NO.13:
# class Ship:
#     count = 0
#     def __init__(self):
#         self.ship_counter = Ship.count + 1
#         Ship.count += 1
#
#     def ship_location(self, deg, min, dir):
#         self.degree = deg
#         self.minute = min
#         self.direction = dir.upper()
#
#     def location_display(self):
#         print("Ship number:",self.ship_counter,"\n","Location and position:",
#               str(self.degree)+chr(176)+str(self.minute)+"'"+str(self.direction))
#
#
# Driver Code:
# S1 = Ship()
# S2 = Ship()
# S3 = Ship()
# S1.ship_location(45,51.5,'n')
# S2.ship_location(75,25.5,'e')
# S3.ship_location(90,71.5,'w')
# S1.location_display()
# S2.location_display()
# S3.location_display()

# PRACTICE PB SET:2
# QUESTION NO.1:
# class Time:
#     def __init__(self, h = 0, m = 0, s =0):
#         self.hour = h
#         self.minute = m
#         self.second = s
#
#     def __str__(self):
#         return f'{self.hour}:{self.minute}:{self.second}'
#
#     def add_time(self, t):
#         self.second = t.second
#         if self.second >= 60:
#             self.second -= 60
#             self.minute += 1
#             self.minute += t.minute
#         if self.minute >= 60:
#             self.minute -= 60
#             self.hour += 1
#             self.hour += t.hour
#         if self.hour >= 24:
#             self.hour -= 24
#
#
## DRIVER CODE:
# t1 = Time(11, 59, 59)
# t2 = Time(20, 65, 75)
# print(t1)
# t1.add_time(t2)
# print(t1)
#
# QUESTION NO.2:
# class Basic_Salary:
#     def __init__(self,basic_salary):
#         self.basic_salary = basic_salary
#
#     def annual_basic_salary(self):
#         self.annual_basic_salary1 = self.basic_salary * 12
#         return self.annual_basic_salary1
#
#
# class Employee:
#     def __init__(self,basic_salary ,annual_bonus):
#         self.basic = Basic_Salary(basic_salary)
#         self.annual_bonus = annual_bonus
#
#     def annual_net_salary(self):
#
#         self.annual_net_salary1 = self.basic.annual_basic_salary() + self.annual_bonus
#         return f'annual net salary:{self.annual_net_salary1}'
#
#
## DRIVER CODE:
# e = Employee(5000,3000)
# print(e.annual_net_salary())
#
# QUESTION NO.3:
# class Point:
#     def __init__(self, x = 0, y = 0):
#         self.x = x
#         self.y = y
#
#     def setter(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'({self.x},{self.y})'
#
## DRIVER CODE:
# p=Point()
# p.setter(2,3)
# print(p)

# QUESTION NO.4:
# class Point:
#     def __init__(self,x=0 ,y=0):
#         self.x = x
#         self.y = y
#
#     def setCoordinates(self, x, y):
#         self.x = x
#         self.y = y
#
# class Distance:
#     def __init__(self):
#         self.p1 = Point(9,5)
#         self.p2 = Point(8,6)
#
#     def find_distance(self):
#         distance = ((self.p1.x - self.p2.x)**2 + (self.p1.y - self.p2.y)**2)**0.5
#         return  'Distance:' + str(distance) + 'm'
#
#
## DRIVER CODE:
# d = Distance()
# print(d.find_distance())

# QUESTION NO.5:
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def setCoordinates(self, x, y):
#         self.x = x
#         self.y = y
#
#     def getCoordinates(self):
#         return self.x, self.y
#
#
# class Distance:
#     def __init__(self, x1, y1, x2, y2):
#         self.p1 = Point(x1, y1)
#         self.p2 = Point(x2, y2)
#         print(f"{self.p1}\n{self.p2}")
#
#     def findDistance(self):
#         distance = ((self.p1.x - self.p2.x) ** 2 + (self.p1.y - self.p2.y) ** 2) ** 0.5
#         return distance
#
#     def __sub__(self, other):
#         if isinstance(other, Distance):
#             result = self.findDistance() - other.findDistance()
#             if result >= 0:
#                 return f"Distance: {result} units"
#             else:
#                 return ("Negative distances are not allowed.")
#         else:
#             raise ValueError("Cannot subtract non-Distance object from Distance.")
#
#
# DRIVER CODE:
# dist1 = Distance(1, 2, 4, 8)
# dist2 = Distance(2, 4, 1, 1)
# dist3 = dist1 - dist2
# print(dist3)
#
# QUESTION NO.6:
# class Point:
#     def __init__(self,x = 0 ,y = 0):
#         self.x = x
#         self.y = y
#
# class Distance_Finder(Point):
#     def find_distance(self, p):
#         Point().__init__(6  ,4)
#         self.p = p
#         distance = ((self.x - p.x)**2 +(self.y - p.y)**2)**0.5
#         return f'distance:{distance}m'
#
#
## DRIVER CODE:
# p1 = Point(5 ,9)
# d = Distance_Finder()
# print(d.find_distance(p1))
#
# QUESSTION NO.7:
# class DistanceFinder:
#     def findDistance(self, p):
#         dx = self.x - p.x
#         dy = self.y - p.y
#         return ((dx ** 2 + dy ** 2) ** 0.5)
#
#
# class Point(DistanceFinder):
#     def __init__(self, x = 0, y = 0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'({self.x}, {self.y})'
#
#     def setCoordinates(self, x, y):
#         self.x = x
#         self.y = y
#
#     def getCoordinates(self):
#         return self.x, self.y
#
#
# class Polygon(DistanceFinder):
#     def __init__(self):
#         self.points = []
#
#     def addPoint(self, point):
#         self.points.append(point)
#
#     def perimeter(self):
#         total_distance = 0
#         num_points = len(self.points)
#
#         for i in range(num_points):
#             point1 = self.points[i]
#             point2 = self.points[(i + 1) % num_points]
#
#             distance = point1.findDistance(point2)
#             total_distance += distance
#
#         return total_distance
#
#
## DRIVER CODE:
# square = Polygon()
# square.addPoint(Point(1, 1))
# square.addPoint(Point(1, 2))
# square.addPoint(Point(2, 2))
# square.addPoint(Point(2, 1))
# square_perimeter = square.perimeter()
# print("Perimeter of the square:", square_perimeter)
#
# triangle = Polygon()
# triangle.addPoint(Point(1, 0))
# triangle.addPoint(Point(2, 2))
# triangle.addPoint(Point(3, 0))
# triangle_perimeter = triangle.perimeter()
# print("Perimeter of the triangle:", triangle_perimeter)
#
# pentagon = Polygon()
# pentagon.addPoint(Point(2, 2))
# pentagon.addPoint(Point(3, 3))
# pentagon.addPoint(Point(6, 4))
# pentagon.addPoint(Point(5, 2))
# pentagon.addPoint(Point(4, 0))
# pentagon_perimeter = pentagon.perimeter()
# print("Perimeter of the pentagon:", pentagon_perimeter)
#
# QUESTION no.8:
# class Time:
#     def __init__(self, h=0, m=0, s=0):
#         self.hour = h
#         self.minute = m
#         self.second = s
#
#     def display_time(self):
#         print(self.hour, ":" , self.minute , ":" , self.second)
#
#     def add_time(self, t):
#         self.second += t.second
#         if self.second >= 60:
#             self.second -= 60
#             self.minute += 1
#         self.minute += t.minute
#         if self.minute >= 60:
#             self.minute -= 60
#             self.hour += 1
#         self.hour += t.hour
#         if self.hour >= 24:
#             self.hour -= 24
#
#     def __str__(self):
#         return str(self.hour) + ":" + str(self.minute) + ":" + str(self.second)
#
#     def __sub__(self, time):
#         return Time(self.hour - time.hour, self.minute - time.minute, self.second - time.second)
#
#     def __mul__(self, float=0.0):
#         if self.hour > 0:
#             self.hour *= float
#         elif self.hour == 0 and self.minute > 0:
#             self.minute *= float
#         else:
#             self.second *= float
#
#         return str(self.hour) + ":" + str(self.minute) + ":" + str(self.second)
#
#
# Driver Code:
# print('t1:',end=" ")
# t1 = Time(5,35,56)
# t1.display_time()
# print('t2:',end=" ")
# t2 = Time(23,56,45)
# t2.display_time()
# t1.add_time(t2)
# t = t2 - t1
# print(t)
# t1.display_time()
# t3 = Time(1,2,3)
# print(t3 * 2.3)
# t3=Time(0,2,3)
# print(t3 * 4)
# t3=Time(0,0,3)
# print(t3 * 4)

# QUESTION no.9:
# class Fraction:
#     def __init__(self, num = 0, den = 1):
#         self.numerator = num
#         self.denominator = den
#
#     def setter(self, n, d):
#         self.numerator = n
#         if d != 0:
#             self.denominator = d
#         else:
#             print('Invalid denominator value, setting to 1 instead.')
#
#     def findFactors(self, x):
#         factors = []
#         for i in range(1, x + 1):
#             if x % i == 0:
#                 factors.append(i)
#         return factors
#
#     def findHCF(self, a, b):
#         self.factor_a = self.findFactors(a)
#         self.factor_b = self.findFactors(b)
#         for i in range(len(self.factor_a) - 1, -1, -1):
#             if self.factor_a[i] in self.factor_b:
#                 return self.factor_a[i]
#         return 1
#
#     def simplify(self):
#         HCF = self.findHCF( self.numerator , self.denominator)
#         self.numerator = int(self.numerator / HCF)
#         self.denominator = int(self.denominator / HCF)
#
#     def __str__(self):
#         return f'{self.numerator}/{self.denominator}'
#
#     def __add__(self, f2):
#         if isinstance(f2, Fraction):
#             return ((self.numerator * f2.denominator) + (f2.numerator * self.denominator))\
#              , (self.denominator * f2.denominator)
#         else:
#             return 'Wrong argument, only fractions allowed.'
#
#     def __sub__(self, f2):
#         if isinstance(f2, Fraction):
#             return ((self.numerator * f2.denominator) - (f2.numerator * self.denominator))\
#              , (self.denominator * f2.denominator)
#         else:
#             return 'Wrong argument, only fractions allowed.'
#
#     def __mul__(self, f2):
#         if isinstance(f2, Fraction):
#             return (self.numerator * f2.numerator) ,(self.denominator * f2.denominator)
#         else:
#             return 'Wrong argument, only fractions allowed.'
#
#     def __truediv__(self, f2):
#         if isinstance(f2, Fraction):
#             return (self.numerator * f2.denominator) ,(self.denominator * f2.numerator)
#         else:
#             return 'Wrong argument, only fractions allowed.'
#
#     def __lt__(self, f2):
#         if isinstance(f2, Fraction):
#             return (self.numerator * f2.denominator) < (self.denominator * f2.numerator)
#         else:
#             return 'Wrong argument, only fractions allowed.'
#
#     def __le__(self, f2):
#         if isinstance(f2, Fraction):
#             return (self.numerator * f2.denominator) <= (self.denominator * f2.numerator)
#         else:
#             return 'Wrong argument, only fractions allowed.'
#
#     def __gt__(self, f2):
#         if isinstance(f2, Fraction):
#             return (self.numerator * f2.denominator) > (self.denominator * f2.numerator)
#         else:
#             return 'Wrong argument, only fractions allowed.'
#
#     def __ge__(self, f2):
#         if isinstance(f2, Fraction):
#             return (self.numerator * f2.denominator) >= (self.denominator * f2.numerator)
#         else:
#             return 'Wrong argument, only fractions allowed.'
#
#     def __eq__(self, f2):
#         if isinstance(f2, Fraction):
#             return (self.numerator * f2.denominator) == (self.denominator * f2.numerator)
#         else:
#             return 'Wrong argument, only fractions allowed.'
#
#     def __ne__(self, f2):
#         if isinstance(f2, Fraction):
#             return (self.numerator * f2.denominator) != (self.denominator * f2.numerator)
#         else:
#             return 'Wrong argument, only fractions allowed.'
#
#
#DRIVER CODE:
# f1 = Fraction(2,7)
# f2 = Fraction(9,5)
# f1.simplify()
# print(f1)
# f2.simplify()
# print(f2)
# print(f1 + f2)
# print(f1 - f2)
# print(f1 * f2)
# print(f1 / f2)
# print(f1 > f2)
# print(f1 >= f2)
# print(f1 < f2)
# print(f1 <= f2)
# print(f1 == f2)
# print(f1 != f2)

# PRACTICE PB SET#3:
# QUESTION NO.2:
# class Object:
#     def __init__(self) -> None:
#         super().__init__()
#         print("Object")
#
# class PhysicalObject(Object):
#     def __init__(self) -> None:
#         super().__init__()
#         print("PhysicalObject")
#
# class Vehicle(PhysicalObject):
#     def __init__(self) -> None:
#         super().__init__()
#         print("Vehicle")
#
# class GroundVehicle(Vehicle):
#     def __init__(self) -> None:
#         super().__init__()
#         print("GroundVehicle")
#
# class FlyingVehicle(Vehicle):
#     def __init__(self) -> None:
#         super().__init__()
#         print("FlyingVehicle")
#
# class FuelTruck(GroundVehicle):
#     def __init__(self) -> None:
#         super().__init__()
#         print("FuelTruck")
#
# class AirCraft(GroundVehicle, FlyingVehicle):
#     def __init__(self) -> None:
#         super().__init__()
#         print("AirCraft")
#
# class CommercialAircraft(AirCraft):
#     def __init__(self) -> None:
#         super().__init__()
#         print("CommercialAircraft")
#
# class Boeing707(CommercialAircraft):
#     def __init__(self) -> None:
#         super().__init__()
#         print("Boeing707")
#
#
# DRIVER CODE:
# boeing = Boeing707()
# print(Boeing707.__mro__)
# print(AirCraft.__mro__)
# print(FuelTruck.__mro__)
# print(GroundVehicle.__mro__)
# print(FlyingVehicle.__mro__)
# print(Vehicle.__mro__)
#
#
# QUESTION NO.3:
# class FancyPrint:
#     message = ""
#
#     @classmethod
#     def set_message(cls, value):
#         cls.message = value
#
#     @staticmethod
#     def FancyPrint():
#          print(FancyPrint.message.upper())
#
#
## DRIVER CODE:
# FancyPrint.set_message("Hello, world!")
# FancyPrint.FancyPrint()

# QUESTION NO.4:
# def makeFancy(func):
#     def wrapper() -> None:
#         print("*" * (len(FancyPrint.message) + 3))
#         func()
#         for x in range(0, 10, 3):
#             print("*" * (len(FancyPrint.message) + 3 - x))
#     return wrapper
#
# class FancyPrint:
#     message = ""
#
#     @classmethod
#     def setMessage(cls, value: str) -> None:
#         cls.message = value
#
#     @staticmethod
#     @makeFancy
#     def fancyPrint() -> None:
#         print(FancyPrint.message.upper())
#
#
## DRIVER CODE:
# mssg = FancyPrint()
# mssg.setMessage("CONGRATULATIONS!!")
# mssg.fancyPrint()
#
# QUESTION NO.5:
# class Polygon:
#     def __init__(self, noOfSides, sideLengthList):
#         self.noOfSides = noOfSides
#         self.sideLengthList = sideLengthList
#
#     def perimeter(self):
#         return sum(self.sideLengthList)
#
#     @property
#     def lengths(self):
#         return self.sideLengthList
#
#     @lengths.setter
#     def lengths(self, new_lengths):
#         self.sideLengthList = new_lengths
#
#
## DRIVER CODE:
# polygon = Polygon(4, [10, 10, 10, 10]) # Creating a square polygon
# print("No. of sides:", polygon.noOfSides)
# print("Side lengths:", polygon.lengths)
# print("Perimeter:", polygon.perimeter())
#
# polygon.lengths = [5, 7, 5, 7] # Changing the side lengths to a rectangle
# print("New side lengths:", polygon.lengths)
# print("New perimeter:", polygon.perimeter())

# QUESTION NO.6:
# """This will not work. An error occurs because when we access self.lengths within the perimeter method, it tries
#  to call the lengths property, which results in an AttributeError because the lengths property getter
#  is not defined.This will print the following error:
#  AttributeError: 'Polygon' object has no attribute "lengths". """
#
# QUESTION NO.7:
# from abc import ABC, abstractmethod
#
# class Polygon(ABC):
#     def __init__(self, noOfSides):
#         self.noOfSides = noOfSides
#         self._lengths = []
#
#     @property
#     @abstractmethod
#     def lengths(self):
#         pass
#
#     def perimeter(self):
#         return sum(self.lengths)
#
#
# class Square(Polygon):
#     def __init__(self, lengths):
#         super().__init__(2)
#         self._lengths = lengths
#
#     @property
#     def lengths(self):
#         return self._lengths
#
#
## DRIVER CODE:
# square = Square([3, 4])
# print("Square:")
# print("Number of sides:", square.noOfSides)
# print("Lengths of sides:", square.lengths)
# print("Perimeter:", square.perimeter())
#
# QUESTION NO.8:
# from abc import ABC, abstractmethod
#
# class Polygon(ABC):
#     def __init__(self, noOfSides):
#         self.noOfSides = noOfSides
#         self._lengths = []
#
#     @property
#     @abstractmethod
#     def lengths(self):
#         pass
#
#     def perimeter(self):
#         return sum(self.lengths)
#
#
# class Triangle(Polygon):
#     def __init__(self, lengths):
#         super().__init__(3)
#         self._lengths = lengths
#
#     @property
#     def lengths(self):
#         return self._lengths
#
#
##DRIVER CODE:
# base = 4
# height = 7
# hypotenuse = (base**2 + height**2)**0.5
# p = Triangle([base, height, hypotenuse]) # calculate hypotenuse
# print("Perimeter:", p.perimeter())
#
# QUESTION NO.9:
# from abc import ABC, abstractmethod
# import math
#
# class Polygon(ABC):
#     def __init__(self, noOfSides):
#         self.noOfSides = noOfSides
#         self._lengths = []
#
#     @property
#     @abstractmethod
#     def lengths(self):
#         pass
#
#     @abstractmethod
#     def area(self):
#         pass
#
#     def perimeter(self):
#         return sum(self.lengths)
#
#
# class Triangle(Polygon):
#     def __init__(self, lengths):
#         super().__init__(3)
#         self._lengths = lengths
#
#     @property
#     def lengths(self):
#         return self._lengths
#
#     def area(self):
#         a, b, c = self.lengths
#         s = (a + b + c) / 2 # Calculate semi-perimeter
#         return math.sqrt(s * (s - a) * (s - b) * (s - c)) # Heron's formula
#
#
## DRIVER CODE:
# base = 4
# height = 7
# hypotenuse = (base**2 + height**2)**0.5
# p = Triangle([base, height, hypotenuse])
# print("Perimeter:", p.perimeter())
# print("Area:", p.area())

# QUESTION NO.10:
from abc import ABC, abstractmethod

class Polygon(ABC):
    def __init__(self, noOfSides):
        self.noOfSides = noOfSides
        self._lengths = []

    @property
    @abstractmethod
    def lengths(self):
        pass

    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        return sum(self.lengths)


class Triangle(Polygon):
    def __init__(self, lengths):
        super().__init__(3)
        self._lengths = lengths

    @property
    def lengths(self):
        return self._lengths

    def area(self):
        a, b, c = self.lengths
        s = (a + b + c) / 2 # Calculate semi-perimeter
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5 # Heron's formula
        return area


class Rectangle(Polygon):
    def __init__(self, length, breadth):
        super().__init__(4)
        self._lengths = [length, breadth, length, breadth]

    @property
    def lengths(self):
        return self._lengths

    def area(self):
        length, breadth = self._lengths[0], self._lengths[1]
        return length * breadth


# DRIVER CODE:
rectangle = Rectangle(5, 8)
print("Rectangle:")
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())
