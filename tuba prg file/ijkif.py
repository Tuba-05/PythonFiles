i=int(input("enter i:"))
j=int(input("enter j:"))
k=int(input("enter k:"))
#i,j,k are numbers
if i<j:
    if j<k:
        i=j
    else:
        j=k
else:
    if j>k:
        j=i
    else:
        i=k
print("i=",i,"j=",j,"k=",k,)        
