# name='xyz'
# def change_name(new_name):
#   global name "if we want to change global variable"
#   name=new_name
# print(name)
# change_name('abc')
# print(name)

# FIBONACCI SERIES: USING RECURSION"A FUNCTION IS CALLED INSIDE ITS OWN FUCTION"
# def fibonacci_(n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return (fibonacci_(n-1)+fibonacci_(n-2))
# n=int(input('enter range:'))
# print('Fibonacci Series:',end='')
# for i in range(1,n+1):
#     print(fibonacci_(i),end=' ')

# SUM USING RECURSION:
# def sum(n):
#     for i in range(n):
#       if n == 0 or n == 1:
#         return 1
#       else:
#         return n + sum(n-1)
#
# n=int(input('enter number'))
# print(sum(n))

# FACTORIAL USING RECURSION:
# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
# n=int(input('enter number for factorial:'))
# print(fact(n))

# Q.7
# from random import randrange
# def fun1(n):
#     result = 0
#     while n:
#         result += n
#         n -= 1
#     return result
# def fun2(stars):
#     for i in range(stars + 1):
#         print(end="*")
#     print()
# def fun3(x, y):
#     return 2*x*x + 3*y
# def fun4(n):
#     return 10 <= n <= 20
# def fun5(a, b, c):
#     return randrange(0, 2)

# 1. print(fun1(5))                 # RESULT 15
# 2. print(fun1())                  # ERROR
# 3. print(fun1(5, 2))              # ERROR
# 4. print(fun2(5))                 # RESULT # ******
                                             # None
# 5. fun2(5)                        # ******
# 6. fun2(0)                        # *
# 7. fun2(-2)                       # NULL/EMPTY
# 8. print(fun3(5, 2))              # RESULT 56
# 9. print(fun3(5.0, 2.0))          # RESULT 56.0
# 10.print(fun3('A', 'B'))          # ERROR
# 11.print(fun3(5.0))               # ERROR
# 12.print(fun3(5.0, 0.5, 1.2))     # ERROR
# 13.print(fun4(15))                # RESULT: TRUE
# 14.print(fun4(5))                 # RESULT: FALSE
# 15.print(fun4(5000))              # RESULT: FALSE
# 16.print(fun5())                  # ERROR
# 17.print(fun5(4))                 # ERROR
# 18.print(fun3(fun1(3), 3))        # RESULT 81
# 19.print(fun3(3, fun1(3)))        # RESULT 36
# 20.print(fun1(fun1(fun1(3))))     # RESULT 231

# Q8:
# def proc(n):
#      if n > 1:
#          return 1
#      else:
#          return proc(n/2)

# a.print(proc(0))    # b.print(proc(1))
# c.print(proc(2))    # d.print(proc(3))
# e.print(proc(5))    # f.print(proc(10))
# ALL ANSWERS = 1

# Q.9:
# def sum(m=0, n=0, r=0):
#     return m + n + r
# print(sum())            # RESULT 0
# print(sum(4))           # RESULT 4
# print(sum(4, 5))        # RESULT 9
# print(sum(5, 4))        # RESULT 9
# print(sum(1, 2, 3))     # RESULT 6
# print(sum(2.6, 1.0, 3)) # RESULT 6.6

# Q.10:
# def sum1(n):
#     s = 0
#     while n > 0:
#         s += 1
#         n -= 1
#     return s
# def sum2():
#     global val
#     s = 0
#     while val > 0:
#         s += 1
#         val -= 1
#     return s
# def sum3():
#     s = 0
#     for i in range(val, 0, -1):
#         s += 1
#     return s
# def main():
#     global val
#     val = 5
#     print(sum1(5))
#     print(sum2())
#     print(sum3())
# main() # Call main function

# Q11. Consider the following very simple module, found in the file mymod.py:
""" Provides the increment function, increment. """
# def increment(x):
#     """ Increments x by 1 and returns the result. """
#     return x + 1
# a. import mymod print(increment(4)) # Supposed to print 5
# b. import from mymod import increment print(increment(4)) # Supposed to print 5
# c. import mymod print(mymod.increment(4)) # Supposed to print 5
# d. from mymod import increment print(mymod.increment(4)) # Supposed to print 5
#""" C is coreect option """
# import mymod
# print(mymod.incerment(4))
# from mymod import increment
# print(increment(4))
# Q.12 to find hypontaneous:
# def pytha_(B,P):
#     H=((B)**2 + (P)**2)**0.5
#     return H
# B=4
# P=3
# print(pytha_(B,P))

# Q.13 slope and distance between the points
# def point(x1,y1,x2,y2):
#     y=(y2 - y1)**2
#     x=(x2 - x1)**2
#     distance = (y + x)**0.5
#     if x1 == x2:
#         print('slope is infinity')
#         return distance
#     else:
#         slope = (y2 - y1) / (x2 - x1)
#         return slope , distance
# x1=float(input('x1:'))
# x2=float(input('x2:'))
# y1=float(input('y1:'))
# y2=float(input('y2:'))
# print(point(x1,y1,x2,y2))

# COUNTDOWN!!!
# def countdown(n):
#     if n == 0:
#         print('BLAST OFF')
#         return
#     print(n)
#     if n == 3:
#         print('BOOM!!! \nSCARED YOU')
#     countdown(n-1)
# countdown(5)

# Q.14:Write a function selected_prime that prints all the prime numbers less than 1,000 that contain the digit 2 or digit 3 (or both).Organize your code to use two functions:
# the first one takes an integer as argument,returns True if the number is prime and False otherwise;the second function checks if an integer contains the digits 2 or 3 or both
# def is_prime(num):
#     count=0
#     for i in range(1 , num+1):
#         if num % i ==0:
#             count += 1
#     return count == 2
#
# def is_value(num):
#     return "2" in str(num) or "3" in str(num)
#
# def select_prime():
#     for i in range(1,1001):
#         if is_prime(i) and is_value(i):
#             print(i)
# select_prime()


# Q15.Write function lastF that takes as input two strings of the form'FirstName'and'LastName',respectively,and returns a string of the form
# 'LastName, F.'.Only the initial should be output for the first name.Test Data: >> > lastF('Albert', 'Camus')'Camus, A.'
# def lastF(F_name,L_name):
#     F = a[0:1]
#     return L_name , F
# a=input('first name')
# b=input('last name')
# print(lastF(a,b))

# Q16.Implement function avg that takes as input a list that contains lists of numbers.Each number list represents the grades
# a particular student received for a course.For example, here is an input list for a class of four students:
#The function avg should print,one per line,every student’s average grade.You may assume that every list of grades is nonempty,
# but you may not assume that every student has the same number of grades.Test
#Data: >> > avg([[95, 92, 86, 87], [66, 54], [89, 72, 100], [33, 0, 0]])
# 90.0
# 60.0
# 87.0
# 11.0
# def avg(lst):
#    for numbers in lst:
#        sum = 0
#        for grades in numbers:
#            sum += grades
#        print(sum/len(numbers))
# avg(lst=[[95,92,86,87],[66,54],[89,72,100],[33,0,0]])

# Write a function that prints a multi-digit decimal number digit-wise,
# starting from higher order digit.
# def func(x):
#     if x < 10:
#         print(x)
#         return
#     func(x//10)
#     print(x % 10)
# func(54341)
#    """ OR """
# def digits(num):
#     for i in range(len(str(num))-1,-1,-1):
#         n=num//10**i
#         print(n)
#         n=n*10**i
#         num-=n
# digits(4523123323)

# SUM using while loop:
# def while_func():
#     total=0
#     i=1
#     n=int(input('enter range for series sum:'))
#     while i <= n:
#         total += i
#         i += 1
#     print(total)
# while_func()

