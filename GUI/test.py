# import re #  bultin pkg module: regular expressions, its primary function is to offer a serach where
# it takes a string
# import random
# from datetime import datetime

# l=['276', '873', '897328', '8733']
# print(l)
# acc = 7664
# l[-1] = acc
# print(l)

file_ = open('SavingAccountRecords.txt').readlines()
for lines in file_:
      print(eval(lines))

      print(type(eval(lines)))

# def login():
#     """ The function works when user is loging his account,"""
#
#     __customer_account_no = input('enter your account number:')
#     bank_records_file = open('CheckingAccountRecords.txt', 'r+')
#     file = bank_records_file.read()
#     bank_records_file.seek(0)
#
#    # searching customer's: user_id, account_no and password
#     for records in bank_records_file:  # range = no. of lines
#         for data in eval(records):
#             if (eval(records)[-2]) == __customer_account_no:
#                 print('Successfully login.')
#                 print(records)
#                 print(type(records))
#                 Customer.records = eval(records)
#                 break  # to break the otherwise it will print records on the basis of no. of index of list
#
#         if records == Customer.records:
#             del records
#             break
#
# login()

# class Loan:
#
#     principal_amount = 0
#     interest_rate = 8.6
#     loan_duration = 0
#     __loan_balance = 0
#
#     def set_loan_info(self):
#         """The function sets the loan details entered by the user."""
#
#         self.t = datetime.today()
#         self.__principal_amount = float(input('Enter the principal amount: '))
#         self.__loan_duration = int(input('Enter the loan duration (in months): '))
#         self.__loan_balance = self.__principal_amount
#         Customer.records.append(self.__loan_balance)
    #
    # def transaction(self):
    #     self.transaction_history = f'Loan duration:{self.__loan_duration}, Loan Balance left:' \
    #                                f'{self.__loan_balance}, Time:{str(self.t)}'
    #
    # def debit_monthly_interest(self):
    #     """The function deducts the monthly interest from the loan balance."""
    #
    #     self.t = datetime.today()
    #     monthly_interest = (self.interest_rate / 100) * self.__loan_balance
    #     self.__loan_balance -= monthly_interest
    #     Customer.records.append(str(self.__loan_balance))
    #     Customer.records.pop(-2)
        # self.transacation = self.__loan_balance
        # self.transaction_history = f'Loan duration:{self.__loan_duration}, Loan Balance left:' \
        #                            f'{self.transacation}, Time:{str(self.t)}'
    #
    # def print_loan_balance(self):
    #     """The function prints the current loan balance."""
    #
    #     return f'Loan Balance: {self.transaction_history}'
    # def loan_records(self):
    #     """ The function saves all info related customers who take loan."""
    #
    #     self.bank_records_file = open('LoanRecords.txt', 'a+')
    #     self.bank_records_file.write(str(Customer.records) + '\n')
#

# class Transaction:
#     def transaction_history_(self, obj_):
#         """The function keeps all records of transaction history."""
#
#         self.bank_records_file = open('TransactionHistory.txt', 'a+')
#         self.transaction = obj_
#         print(self.transaction)
#         self.bank_records_file.write(str(self.transaction) + '\n')
#
#
# l = Loan()
# l.set_loan_info()
# l.debit_monthly_interest()
# l.loan_records()
# obj_ = l.print_loan_balance()
# l =Transaction()
# l.transaction_history_(obj_)

# def set_loan_info():
#     """The function sets the loan details entered by the user."""
#
#     t = datetime.today()
#     principal_amount = float(input('Enter the principal amount: '))
#     loan_duration = int(input('Enter the loan duration (in months): '))
#     loan_balance = principal_amount
#     transaction_time = 'principle amount:', principal_amount, 'Loan duration:', loan_duration, \
#         'Loan balance:', loan_balance, 'time:'+ str(t)
#     print(transaction_time)
#     bank_records_file = open('TransactionHistory.txt', 'a+')
#     transaction = transaction_time
#     bank_records_file.write(str(transaction))
#
# set_loan_info()
# print(datetime.today())
# def generate_account_number():
#     '''Generates a random 9 digit account number'''
#     account_number=random.randint(100000000,9999999999)
#     return str(account_number)
# a = generate_account_number()
# print(a)

records=[]
# while True:
#     print('It must contain your area,city and country')
#     country = input('Enter your country name:')
#     city = input('Enter your city name:')
#     area = input('Enter your area name:')
#     customer_address = country + ',' + city + ',' + area
#
#     if re.match('^(?=.*\d)',customer_address):
#         print("kindly enter your full and correct address.")
#
#     else:
#         records.append(customer_address)
#         print(records)
#         break



# def validate_password(password):
#     #check minimum length
#     if len(password)<7:
#        return False
#     #check alphanumeric and special character requirements
#     if not re.match("^(?=.*([a-z-A-Z])(?=.*\d)(?=.*[@#$%^&+=]))" , password):  # ?= ==> syntax of re module
#         return False
#     return True
# password=input("Enter your password")
# if validate_password(password):
#     print("Password is valid")
# else:
#     print("Password too weak create another one")
#
# password=input("Enter your password")
# while not (True):
# m=0
# while m==0:
#     password=input("Enter your password")
#     if len(password)<7 or not re.match("^(?=.*([a-z-A-Z])(?=.*\d)(?=.*[@#$%^&+=]))" , password):
#         print("INVALID")
#     else:
#         m+=1
#         print("Password has been crated")

def delete():
    account_no_ = input('')
    f = open ('CurrentAccountRecords.txt', 'r')
    f = f.read()
#     for records in f:
#         if account_no_ in eval(records):

# records = [] #
#
# while True:
#     print('Note:length of your password must be 7 characters including alphanumeric'
#           '& special characters.')
#     p = input('Enter your account password:')
#     if len(p) >= 7:
#         if '0'<=p<='9' in p:
#             if 'A'<='Z' or 'a'<='z' in p:
#                 if '@' or '#' or '$' or '%' or '*' in p:
#                     records.append(p)
#                     break
#
#     else:
#         print("Create another password")

# while (True):
#     try:
#         m = int(input('enter your country code in numbers:'))
#         assert len(str(m)) != 0 and 1<= len(str(m)) <=2
#     except:
#         print("You country code should '+xx' or '+x' . ")
#     else:
#         l = "+" + str(m)
#         records.append(l)
#         break

# while (True):
#     try:
#         m = input('enter your country name:')
#         assert m != (0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9) and \
#                ('a'<=m <= 'z')
#     except:
#         print("Your country name must be in letters!!!")
#     else:
#         records.append(m)
#         break

# while (True):
#     try:
#         m = input("enter your gender: Male or Female.\n").lower()
#         if m == 'male' or m == 'female':
#             records.append(m)
#             break
#     except:
#         print('Kindly give appropriate answer.')

# class Error(Exception):
#     pass
# try:
#     age = float(input('enter your age:'))
#     if age < 18:
#         raise Error
#     else:
#         pass
# except Error:
#     print("You are under aged.")
# except ValueError:
#     print("The value you have entered is not an age.")
# Error()
# m = str(age) + ' yrs'
# records.append(m)

# while (True):
#     p = input('Enter your account password:\nNote:'
#     'length of your password must be 7 characters including alphanumeric & special characters. \n')
#     if len(p) >= 7 and (('a'<='z') or ('A'<='Z'))and('0'<='9')and('@'or'#'or'$'or'%'or'*'):
#         records.append(p)
#         break
#     else:
#         print("Create another password PLZ!")
# print(records)
# l =['taiba','fhfhj','5676648','4536245']
# l.pop(-2)
# print(l)


class Customer:
    count = 0
    account_no = 0
    records = []

    # def Customer_info():
    #     .__customer_user_name = input('Enter yor name in letters:').lower()
    #     while not('a'<=.__customer_user_name<='z'):
    #             print("You entered an int instead of str.")
    #
    #     else:
    #         .__customer_user_id = int(Customer.count + 1)
    #         a = Customer.count + 1
    #         .__customer_account_no = str('A') + str(int(Customer.account_no + 1))
    #         b = Customer.account_no + 1
    #         Customer.records.append(.__customer_user_id)
    #         Customer.records.append(.__customer_account_no)
    #         Customer.records.append(.__customer_user_name)
    #         Customer.count = a
    #         Customer.account_no = b

    # def login():
    #     """ The function works when user is loging his account,"""
    #
    #     .__customer_user_id = input('Enter your id:')
    #     .__account_no = input('enter your account number:')
    #     .__customer_password = input('enter your password:')
    #     .bank_records_file = open('CurrentAccountRecords.txt', 'r+')
    #     .file = .bank_records_file.read()
    #     .bank_records_file.seek(0)
    #
        # searching customer's: user_id, account_no and password
        # for records in .bank_records_file: # range = no. of lines
        #     for data in eval(records):
        #         if (eval(records)[0]) == .__customer_user_id and (eval(records)[1]) == .__account_no\
        #         and (eval(records)[3]) == .__customer_password:
        #             print('Successfully login.')
        #             print(records)
        #             print(type(records))
        #             a= eval(records)
        #             a.pop(7)
        #             print(a)
        #             print(a[0])
        #             break # to break the otherwise it will print records on the basis of no. of index of list
            # if these statements would inside in nested loop it will print multiple times
            # if user enter invalid user id
            # if .__customer_user_id not in .file:
            #     print('Invalid user id.')
            # if user enter invalid account number
            # if .__account_no not in .file:
            #     print('Invalid account number.')
            # if user enter invalid password
            # if .__customer_password not in .file:
            #     print("Invalid password.")
            #     break  # to break 3 times


# c = Customer()
# c.login()

# c.Customer_info()
# print(Customer.records)
# Customer.records=[]

# class Administrator:
#     def administrator_info():
#         .__administrator_user_id = input('Enter your id:')
#         .__administrator_user_name = input('Enter your name:')
#         .__administrator_password = input('Enter your account password:')
#         .admin_file = open('Admin.txt', 'r+')
#         a = .admin_file.readline()
#         b = .admin_file.readline()
#         .admin_file.seek(0)
        ## loging admin account
        # for records in .admin_file: # loop iterates 2 times
        #     for item in eval(records): # nested loop iterates 3 times
        #         if  (eval(records)[2]) == .__administrator_password and (eval(records)[1]) == \
        #         .__administrator_user_name and (eval(records)[0]) == .__administrator_user_id:
        #             print('Successfully login.')
        #             print(records)
        #             break # to break 3 times
        #         else:
        #             print(end='')
            ## if user enters two different inputs of both admin ids
            # if (.__administrator_user_id in b) and (.__administrator_user_name in a):
            #     print('OOPs.')
            #     break
           # # if user enters invalid id
           #  if (.__administrator_user_id in a) and (.__administrator_user_name in b):
           #      print('OOPs.')
           #      break
            ## if user enters invalid name or id
            # if (.__administrator_password not in b) and (.__administrator_password not in b):
            #    print('invalid user password.')
            # if (.__administrator_user_id not in a) and (.__administrator_user_id not in b):
            #     print('invalid user id.')
            # if (.__administrator_user_name not in a) and (.__administrator_user_name not in b):
            #     print('invalid user name.')
            #     break # to break 2 times
# c = Administrator()
# c.administrator_info()

# class Checking_Account(Account):
#     def _init_():
#         super().__init__()
#         .overdraft_fee = 0
#
#
# def withdraw_amount():
#     """The function works when a customer wants to withdraw money from their checking account."""
#     Account.bank_balance = int(Customer.records[-1])
#     .withdraw_amount = int(input('Enter the amount you want to withdraw:'))
#
#     if .withdraw_amount <= Account.bank_balance:
#         .New_amount = Account.bank_balance - .withdraw_amount
#         Account.bank_balance = .New_amount
#         Customer.records.append(Account.bank_balance)
#         Customer.records.pop(-2)
#     else:
#         print("Insufficient funds in your checking account.")
#         .overdraft_choice = input("Do you want to proceed with an overdraft? (Y/N): ").upper()
#
#         if .overdraft_choice == 'Y':
#             .New_amount = Account.bank_balance - .withdraw_amount - Checking_Account.overdraft_fee
#             Account.bank_balance = .New_amount
#             Customer.records.append(Account.bank_balance)
#             Customer.records.pop(-2)
#             print("Overdraft fee charged:", Checking_Account.overdraft_fee)
#         else:
#             print("Withdrawal canceled.")
#
#
# class SavingAccount(Account):
#     def __init__():
#         super().__init__()
#         .interest_rate = 0
#
#     def deposit_amount():
#         Account.bank_balance = int(Customer.records[-1])
#         .deposit_amount = int(input('enter money you want to deposit:'))
#         .new_amount = Account.bank_balance + .deposit_amount
#         Account.bank_balance = .new_amount
#         Customer.records.append(Account.bank_balance)
#         Customer.records.pop(-2)
#
#     def apply_interest():
#         .interest_rate = 0.05  # Assuming interest rate is 5%
#         Account.bank_balance = int(Customer.records[-1])
#         .new_amount = Account.bank_balance + (Account.bank_balance * .interest_rate)
#         Account.bank_balance = .new_amount
#         Customer.records.append(Account.bank_balance)
#         Customer.records.pop(-2)
