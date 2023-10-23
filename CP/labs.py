#value=0
#for i in range(1,6):
    #n=float(input(f'enter integer{i}:'))
    #value=value+n
#avg=float(value/5)
#print('AVERAGE=',avg)

#lab5
# while True:
#     print("Main Menu")
#     print("*" * 9)
#     print("1.Deposit Money\n2.Withdraw Money\n3.Login As Different User")
#     n = int(input("Enter Your choice!: "))
#     if n == 1 or n == 2 or n == 3:
#         print("Transaction Complete!")
#         print()
#         z = input("Do You want to Continue? [y/Y]: ")
#         if z.lower() == "n":
#             print("Thank You!")
#             break
#     else:
#         print("Enter a Valid Choice!")

#lab5
#l=[]
#n=int(input('enter no. of elements you want in list:'))
#for i in range(n):
    #elements=int(input(f'enter elements{i}='))
    #l.append(elements)
#print(l)
#largest_integer=l[0]
#for j in range(len(l)):
    #if l[j]>largest_integer:
       # largest_integer=l[j]
#print('largest integer:',largest_integer)

#lab9
# def out_circle(r1):
#     def in_circle(r):
#         Circumference=2*3.142*r
#         return Circumference
#
#     print(in_circle(9))
#     Area=3.142*r1**2
#     return Area
#
# print(out_circle(5))
#SIMPLE CALCULATOR:
def addition(n1,n2):
    return n1 + n2
def subtraction(n1,n2):
    return n1 - n2
def multiplication(n1,n2):
    return n1 * n2
def division(n1,n2):
    return n1 / n2
print("""select anyone given operations
1.addition\n2.subtraction\n3.multiplication\n4.division""")
n=int(input('enter you choice:'))
n1=int(input('n1='))
n2=int(input('n2='))
if n==1:
    print(f'{n1}+{n2}={addition(n1,n2)}')
elif n==2:
    print(f'{n1}-{n2}={subtraction(n1,n2)}')
elif n==3:
    print(f'{n1}*{n2}={multiplication(n1,n2)}')
elif n==4:
    print(f'{n1}/{n2}={division(n1,n2)}')
else:
    print('your choice is not valid')
