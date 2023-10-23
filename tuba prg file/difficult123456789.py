value=int(input('enter value:'))
count=0
for i in range(1,value+1):
    for j in range(1,i+1):
        count+=1
        print(count,end='')
    print()    
        
