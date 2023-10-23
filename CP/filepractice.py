#Q1.The cryptography function crypto takes as input a string (i.e., the name of a file in the current directory). The
# function should print the file on the screen with this modification: Every occurrence of string 'secret' in the file should
# be replaced with string 'xxxxxx'.

# def crypto(a):
#    file = open(a, "r+")
#    info_of_file = file.read().replace('secret', 'xxxxxx')
#    file.seek(0)
#    file.write(info_of_file)
#    print(info_of_file)
#    file.close()
#
# crypto(a=input("Enter file name with extension: "))

#Q2.The function censor takes the name of a file (a string) as input. The function should open the file, read it, and then write
#it into file censored.txt with this modification: Every occurrence of a four-letter word in the file should be replaced with
#string 'xxxx'. Note that this function produces no output, but it does create file censored.txt in the current folder.
# def censor(a):
#    file=open(a,'r+')
#    f=file.read().split()
#    w=input('enter new file with extension')
#    new_file=open(w,'w+')
#    for i in f:
#       if len(i)==4:
#          word_x=len(i)
#          c=new_file.read().replace('word_x','xxxx')
#          h=new_file.write(c + " ")
#       if len(i)!=4:
#          h=new_file.write(i + " ")
#    print(new_file)
#    new_file.close()
# a=input('enter file with extension')
# censor(a)
#Q3 Write a function fcopy that takes as input two file names (as strings) and copies the content of the first file into the second line by line.
# def fcopy():
#    a=input('first file:')
#    b=input('second file:')
#    first_file=open(a,'r+')
#    second_file=open(b,'w+')
#    f=first_file.read()
#    for i in f:
#       s=second_file.write(i)
#    print()
# fcopy()

#Q5.Implement function duplicate that takes as input the name (a string) of a file in the current directory and returns
#True if the file contains duplicate words and False otherwise.
# def duplicate():
#    a=input('file:')
#    file=open(a,'r')
#    words_of_list=file.read().split()
#    unique_words=[]
#    print(words_of_list)
#    check = False
#    for i in words_of_list:
#       if i not in words_of_list:
#          unique_words.append(i)
#          print(check)
#       else:
#          check = True
#    print(check)
#    file.close()
#
# duplicate()

#Q4.Implement function distribution that takes as input the name of a file( as astring).This one - line file will contain letter
# grades separated by blanks.Your function should print the distribution of grades.TestData: >> distribution('grades.txt')
# 6 students got A           # 2 students got B-
# 2 students got A-          # 4 students got C
# 3 students got B+          # 1 students got C-
# 2 students got B           # 2 students got F
# def distribution(a):
#      f=open(a, 'r')                                                 #RESULT:
#      words=f.read().split()                                         #3students got A
#      grades=[]                                                      #1students got B
#      for word in words:                                             #2students got C
#          if word not in grades:                                     #1students got D
#              grades.append(word)                                    #1students got A-
#      for grade in grades:                                           #1students got F
#          print(f"{words.count(grade)}students got {grade}")         #1students got B+
# distribution('grades.txt')



