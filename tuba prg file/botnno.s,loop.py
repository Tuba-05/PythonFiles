value=int(input('enter value:'))
print('factors of',value,'are:',end='')
for i in range(1,int(value/2)+1):
    if value%i==0 and value==i:
        print(i)
    elif value%i==0:
        print(i,end=',')
print(value)        
