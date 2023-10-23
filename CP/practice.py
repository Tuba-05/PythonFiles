
#QUESTION 6
# a.print([x + 1 for x in [2, 4, 6, 8]]) = [3,5,7,9]
# b.print([10*x for x in range(5, 10)]) = [50,60,70,80,90]
# c.print([x for x in range(10, 21) if x % 3 == 0]) = [12,15,18]
# d.print([(x, y) for x in range(3) for y in range(4)]) = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)]
# e.print([(x, y) for x in range(3) for y in range(4) if (x + y) % 2 == 0]) = [(0, 0), (0, 2), (1, 1), (1, 3), (2, 0), (2, 2)]

#QUESTION 4
#Original  List       Target  list
# [2, 4, 6, 8, 10][2, 4, 6, 8, 10, 12, 14, 16, 18, 20]    =  l[5:]=[12,14,16,18]
# [2, 4, 6, 8, 10][-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10]  =  l[:0]=[-10,-8,-6,-4,-2,0]
# [2, 4, 6, 8, 10][2, 3, 4, 5, 6, 7, 8, 10]   =   l[1:3]=[3,4,5,6,7]
# [2, 4, 6, 8, 10][2, 4, 6, 'a', 'b', 'c', 8, 10]  =  l[3:3]=['a','b','c']
# [2, 4, 6, 8, 10][2, 4, 6, 8, 10]  =  l
# [2, 4, 6, 8, 10][]  =  l[:0]
# [2, 4, 6, 8, 10][10, 8, 6, 4, 2]   =   l[::-1]
# [2, 4, 6, 8, 10][2, 4, 6]  =  l[:3]
# [2, 4, 6, 8, 10][6, 8, 10]  =  l[2:]
# [2, 4, 6, 8, 10][2, 10]  =  l=l[:1]+l[-1:]
# [2, 4, 6, 8, 10][4, 6, 8]  =  l[1:4]

#QUESTION "Provide a list comprehension expression for each of the following lists."
#a.[1, 4, 9, 16, 25]  =  print([(i**2)for i in range(1,6)])
#b.[0.25, 0.5, 0.75, 1.0, 1.25. 1.5]  =  print([(0.25*i)for i in range(1,7)])
#c.[('a', 0), ('a', 1), ('a', 2), ('b', 0), ('b', 1), ('b', 2)]  =  print([(x,y)for x in ['a','b']for y in range(3)])

#QUESTION21. What happens when an executing program attempts to retrieve a value using a key that is not present in the dictionary? ANSWER :error

#QUESTION23. Given the following dictionary:
# d = {3:0, 5:1, 10:1, 8:2, 15:4}
#Indicate what each of the following code fragments will print:
# a. print(d) = {3: 0, 5: 1, 10: 1, 8: 2, 15: 4}
# b.for x in d:
#     print(x)
#     3
#     5
#     10
#     8
#     15
# c.for x in d.keys():
#     print(x)
#     3
#     5
#     10
#     8
#     15
# d.for x in d.values():
#     print(x)
#     0
#     1
#     1
#     2
#     4

#QUESTION8. Write code to add up and print all the positive values in a list of integers. For example, a list containing the elements
#[3,-3,5,2,-1,2] would evaluate to 12, since 3+5+2+2 = 12. The code prints zero if the list is empty.
# given_list=[3,-3,5,2,-1,2]
# count=0
# new_list=[]
# for x in given_list:
#     if x>0:
#         count+=1
#         new_list.append(x)
# SUM=sum(new_list)
# print(f'{count} numbers are positive\nsum of positive numbers:{SUM}')
#  PROGRAM RESULT [ 4 numbers are positive \n sum of positive numbers:12]

# QUESTION9.Write code that counts and prints the even numbers in a list of integers. For example, a list containing the elements 3;5;4;-1;
# and 0, would evaluate to 2, since there are only two even numbers: 4 and 0. The code prints zero if the list is empty.
# list_=[3,5,4,-1,0]
# h=[]
# count=0
# for y in list_:                  #RESULT:
#      if y>=0 and y%2==0:         2numbers are even which are [4, 0]
#          count+=1
#          h.append(y)
# print(f'{count}numbers are even which are {h}')

#QUESTION10.Write code that accepts two parameters, a list of numbers and a number x. The code should print, in order, all the
#elements in the list that are at least as large as the number x.
# x=int(input('enter number:'))
# list=input('enter list of numbers separated by spaces:')
# list=list.split()
# print(list)
# new_list=[]
# count=0                                                     #RESULT:
# for j in list:                                              enter number:25
#     if int(j)>=x:                                           enter list of numbers separated by spaces:9 15 29 33 45
#         count+=1                                            enter list of numbers separated by spaces:9 15 29 33 45
#         new_list.append(j)                                  3 numbers are as larges as 25
# new_list.sort()                                             numbers list are ['29', '33', '45']
# print(f'{count} numbers are as larges as {x}\n numbers list are {new_list}')

#MATRIX OR 2D LISTS:
# matrix=[]
# n=int(input('enter no. of rows:'))
# m=int(input('enter no. of colums:'))
# for row in range(n):
#      res_matrix = []
#      for coloum in range(m):
#          k=int(input())
#          res_matrix.append(k)
#      matrix.append(res_matrix)
# print(matrix)
# for row in range(n):
#      for colum in range(m):
#          print(matrix[row][colum], end=' ')
#      print()


# matrix=[]
# print('enter a 3x3 matrix')
# n=int(input())
# for r in range(n):
#     m=[]
#     for c in range(n):
#         v=int(input(f'enter value for rows{c}'))
#         m.append(v)
#     matrix.append(m)
#     m=[]
# print(matrix)


#Q12.Write code to print a matrix in matrix form (except the square brackets) on the screen
# matrix = [[2, 4, 6], [3, 5, 7], [1, 8, 9]]
# for r in matrix:
#     for c in r:
#         print(c, end=" ")
#     print()
# L=[]
# for i in range(3):
#     l=[]
#     n=input('enter values')
#     l.append(n)
#     L.append(l)
# print(L)
# for r in L:
#     for c in r:
#         print(c,end=' ')
#     print()

#Q13/14.Write code to increment a matrix, storing the result in matrix.
#for new matrix
# m=[[2,4,6],[1,3,5],[0,7,9]]
# matrix=[]
# for row in m:
#     res_matrix=[]
#     for colum in row:
#         res_matrix.append(colum + 1)
#     matrix.append(res_matrix)
# print(matrix)

#for same matrix:
#m = [[2, 4, 6], [1, 3, 5], [0, 7, 9]]
#for row in range(len(m)):
#    for colum in range(len(m[row])):
#        m[row][colum]=m[row][colum] + 1
#print(m)


#Q15/16.Write code to add two matrices of similar dimensions, storing the result in a "NEW/SAME" matrix.
#for new matrix
# matrix=[]                                            #RESULT
# m1=[[0,2],[4,6]]                                     #[1, 5, 9, 13]
# m2=[[1,3],[5,7]]
# for i in range(len(m1)):
#      m=[]
#      for j in range(len(m1[0])):
#          m=m1[i][j] + m2[i][j]
#          matrix.append(m)
# print(matrix)
#for same matrix:
# r_matrix=[[0,0],[0,0]]                      #RESULT:
# m1=[[0,2],[4,6]]                            #[[1, 5], [9, 13]]
# m2=[[1,3],[5,7]]
# for i in range(len(m1)):
#      for j in range(len(m1[0])):
#          r_matrix[i][j] = m1[i][j] + m2[i][j]
# print(r_matrix)


# Q17. Write code to transpose a matrix, storing the results in a new matrix.
# matrix=[]
# M=[[1,3,5],[2,4,6],[0,7,9]]                       #RESULT:
# for i in range(len(M)):                          #[[1, 2, 0], [3, 4, 7], [5, 6, 9]]
#      m=[]
#      for j in range(len(M[0])):
#         m.append(M[j][i])
#      matrix.append(m)
# print(matrix)


#Q18.Write code to multiply two matrices of similar dimensions, storing the result in a new matrix
#for new matrix
# matrix=[]                                            #RESULT
# m1=[[0,2],[4,6]]                                     #[0, 6, 20, 42]
# m2=[[1,3],[5,7]]
# for i in range(len(m1)):
#       m=[]
#       for j in range(len(m1[0])):
#           m=m1[i][j] * m2[i][j]
#           matrix.append(m)
# print(matrix)
#for same matrix:
# r_matrix=[[0,0],[0,0]]                      #RESULT:
# m1=[[0,2],[4,6]]                            #[[0, 6], [20, 42]]
# m2=[[1,3],[5,7]]
# for i in range(len(m1)):
#       for j in range(len(m1[0])):
#           r_matrix[i][j] = m1[i][j] * m2[i][j]
# print(r_matrix)


# i=0
# while i <= 10:
#     print((10-i)*' '+((1 + 2*i)*'*'))
#     i += 1

# count=0
# for i in range(1,9):
#     for j in range(1,i+1):
#         count += 1
#         print(count,end=' ')
#     print()

# import time
#
# def calcTime(func):
#     def wrapper():
#         begin = time.time()
#         func()
#         end = time.time()
#         print(f"Run time: {end - begin} seconds")
#     return wrapper
#
# @calcTime
# def longloop():
#     print("Enter anything to exit")
#     input()
#
# longloop()
