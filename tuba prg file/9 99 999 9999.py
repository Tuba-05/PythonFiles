n=int(input('enter value of n:'))
sum=0
print('series:',end='')
for i in range(1,n+1):
    sum=sum+int('9'*i)
    if i==n:
        print('9'*i)
    else:
        print('9'*i,end='+')
print('sum of series:',sum)         
    
