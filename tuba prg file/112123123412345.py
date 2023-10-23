n=int(input('enter value of n:'))
count=0
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
        count+=1
    print( )  
