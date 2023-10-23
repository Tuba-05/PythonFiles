side1=int(input("side1:"))
side2=int(input("side2:"))
side3=int(input("side3:"))
if side1==side2==side3:
    print("triangle is quilateral")
elif side1==side2 or side1==side3 or side2==side3:
    print("triangle is isosceles")
elif side1!=side2!=side3:
    print("triangle is scalene")
