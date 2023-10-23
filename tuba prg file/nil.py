BS=int(input('enter basic salary:'))
HRA=int(input('enter house rent allowance:'))
DA=int(input('enter dearness allowance:'))
GS=int(input('enter gross salary:'))
DD=int(input('enter deductions:'))
GS=(BS)+(HRA)+(DA)
NetSalary=(GS)+(DD)
if (BS and HRA and DA and GS and DD)<0:
    print()
    exit
elif BS<=10000:
    print('(HRA=20%,DA=80%,DD=2%)of BS')
elif BS<=20000:
    print('(HRA=25%,DA=90%,DD=4%)of BS')
elif  BS>20000:
    print('(HRA=30%,DA=95%,DD=10%)of BS')
