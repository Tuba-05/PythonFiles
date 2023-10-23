num1=float(input("enter num1:"))
num2=float(input("enter num2:"))
num3=float(input("enter num3:"))
if num1==num2==num3:
    print("all valus are equal")
elif num1>=num2 and num1>=num3:
    print(num1,"is max value")
    if num2>num3:
        print(num3,"is min value")
    else:
        print(num2,"is min value")
elif num2>=num1 and num2>=num3:
    print(num2,"is max value")
    if num1>num3:
        print(num3,"is min value")
    else:
        print(num1,"is min value")
else:
    print(num3,"is max value")
    if num1>num2:
        print(num2,"is min value")
    else:
        print(num1,"is min value")
    
    
                 
