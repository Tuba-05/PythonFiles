value=int(input('enter value:'))
count=0
for i in range(2,value):
    if value%i==0:
        count+=1
        print(value,' is not a prime number')
        break

if count!=1:
    print(value,' is a prime number')



