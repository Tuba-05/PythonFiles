value=int(input('enter no.:'))
print('factors of',value,'are:',end='')
for i in range(1,value+1):
    if value%i==0 and i==value:
     print(i)
    elif value%i==0:
      print(i,end=',')  
         
       
