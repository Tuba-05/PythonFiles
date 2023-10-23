value=int(input("enter value:"))
times=int(input("how many times?"))
print('times table of',value,':')
for i in range(1,times+1):
    print(value,'x',i,'=',value*i)
