n=int(input('enter no.'))
fact=1
if n==0:
    print('0!=1')
elif n>=1:
    for i in range(n,0,-1):
        fact=fact*i
    print(n,'!=',fact)
else:
    print('kindly enter +ve value')
    
    
        
