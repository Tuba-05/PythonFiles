#q=[]
#n=int(input('enter#of choices:'))
#for i in range(n):
    #Q=(f'Q{i+1}')
    #q.append(Q)
#print(q)
#m=n
#ch=[]
#for j in range(m):
    #v=input(f'enter values{j}')
    #ch.append(v)
#print(ch)
#d=dict(zip(q,ch))
#print(d)

#alternate way
#n=int(input('enter  number of questions:'))
#D={}
#for i in range (1,n+1):
    #m=input(f'enter answers of Q{i}:')
    #D[('Q'+str(i))]=m
#print(D)

#lab13:
#f=open('C://Users//AA//Desktop//tuba.txt','r')
#count=0
#for lines in f:
    #words=lines.split()
    #count+=len(words)
#f.close()
#print('number of words=',count)

#to print words of file separated by commas
#f=open('C://Users//AA//Desktop//tuba.txt')
#t=f.read()
#t=t.split(',')
#print(t)

#to print words of file separated by commas
#f=open('C://Users//AA//Desktop//tuba.txt')
#for i in f:
    #print(i,end='')

# to print longest word in file
# f=open('C://Users//AA//Desktop//tuba.txt')
# t=f.read().split()
# longest_word=t[0]
# for i in t:
#     if len(i)>len(longest_word):
#         longest_word=i
# print(i)





