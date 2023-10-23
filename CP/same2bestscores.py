l=[86,86,85,85,85,83,23,45,84,1,2,0]
max1=l[0]
for i in range(len(l)):
    if max1<l[i]:
        max1=l[i]
max2=l[-1]
for j in range(len(l)):
    if max2<l[j]:
        max2=l[j]
print('first best score=',max1,'\n','second best score=',max2)

# G=['mobile','laptop',100,'camera',310.28,'speakers',27.00,'television',100,'laptop case','camera lens']
# s=[]
# l=[]
# for x in G:
#     if type(x)==str:
#         s.append(x)
#     else:
#         l.append(x)
# print(s,'\n',l)
# l.sort()
# s.sort()
# print(s,'\n',l)
# l.reverse()
# s.reverse()
# print(s,'\n',l)
