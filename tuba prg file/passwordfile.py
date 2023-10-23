t=input('Enter password:')
if (len(t)>=7 and len(t)<=15):      
    if ('1' in t or '3' in t or '5' in t):
        if ('@' in t or '#' in t or '$' in t):
            print('password is valid')
        else:
            print('character is invalid')
    else:
         print('digit is invalid')
else:
    print('length is invalid')
