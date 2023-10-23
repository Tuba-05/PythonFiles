n=int(input('enter n:'))
count=0
for i in range(0,n):
    count+=1
    print(' '*(n-i)+'*'*(2*i+1))
