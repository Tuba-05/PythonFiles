""" BANKING SYSTEM """

from abc import ABC, abstractmethod
import re
import random
from datetime import datetime


def generate_account_number():
    """Generates a random 9-digit account number."""

    account_number = random.randint(100000000, 9999999999)
    return str(account_number)


class Bank:
    def __init__(self):
        """BANK INFO"""
        self.bank_code = 'my_bank555$'
        self.bank_address = 'address'
        self.bank_name = 'BANK'

    def get_bank_info(self):
        return f'{self.bank_code}\n{self.bank_name}\n{self.bank_address}'


class User:
    def login_(self):
        """ The function allows choices like login account and create account."""

        print(f'log in or create account\n press 1 for log in and 2 for create account')
        choice = int(input('Enter your choice:'))

        # user Login account
        if choice == 1:
            print(f"are you a customer or an Administrator?\nPress 1 for Administrator "
                  f"and 2 for customer.")
            login_choice = int(input('enter here:'))

            # Login user is Admin
            if login_choice == 1:
                admin = Administrator()
                admin.login()
                admin.get_records()

            # Login user is Customer
            elif login_choice == 2:
                acc_type = int(input('1.Checking Account\n2.Saving Account\n'
                                     '3.LOAN\n4.Delete account\nEnter your account type number:'))
                if acc_type == 1:
                    ch = CheckingAccount()
                    file_name = 'CheckingAccountRecords.txt'
                    ch.login(file_name)
                    ch.set_credit_limit(500)
                    ch.set_overdraft_fee(10)

                    print('Enter your choice:')
                    print('1. Deposit money in account.\n2. Withdraw money from account.'
                          '\n3. Display your account information.')
                    chk_acc_choice = input('Enter your choice:')

                    if chk_acc_choice == '1':
                        ch.deposit_amount()
                        ch.get_account_balance()
                        obj_ = ch.transaction_history_()
                        ch = FileSaver()
                        ch.transaction_history(obj_)

                    elif chk_acc_choice == '2':
                        ch.withdraw_amount()
                        ch.get_account_balance()
                        obj_ = ch.transaction_history_()
                        ch = FileSaver()
                        ch.transaction_history(obj_)

                    elif chk_acc_choice == '3':
                        ch.get_account_info()
                        ch.get_account_balance()
                        obj_ = ch.transaction_history_()
                        ch = FileSaver()
                        ch.transaction_history(obj_)

                    else:
                        print('Invalid choice.')

                elif acc_type == 2:
                    sv = SavingAccount()
                    file_name = 'SavingAccountRecords.txt'
                    sv.login(file_name)
                    print('Enter your choice:\n1.Apply for interest.\n2.deposit money.\n3.Withdraw money.')
                    sv_acc_choice = input('Enter your choice:')

                    if sv_acc_choice == '1':
                        sv.apply_interest()
                        sv.deposit_amount()
                        sv.get_account_balance()
                        obj_ = sv.transaction_history_()
                        sv = FileSaver()
                        sv.transaction_history(obj_)

                    elif sv_acc_choice == '2':
                        sv.deposit_amount()
                        sv.get_account_balance()
                        obj_ = sv.transaction_history_()
                        sv = FileSaver()
                        sv.transaction_history(obj_)

                    elif sv_acc_choice == '3':
                        sv.withdraw_amount()
                        sv.get_account_balance()
                        obj_ = sv.transaction_history_()
                        sv = FileSaver()
                        sv.transaction_history(obj_)

                    else:
                        print('Invalid choice.')

                elif acc_type == 3:
                    ln = Loan()
                    file_name = 'LoanRecords.txt'
                    ln.login(file_name)
                    ln.debit_monthly_interest()
                    ln.get_account_balance()
                    ln.transaction_history_()
                    obj_ = ln.transaction_history_()
                    ln = FileSaver()
                    ln.transaction_history(obj_)

                elif acc_type == 4:
                    customer = Customer()
                    customer.delete_account()

                # if login customer put invalid choice or wants to exit
                else:
                    print('Your choice is invalid.\nKindly restart.')

        # if customer wants to create new account
        elif choice == 2:
            print('Account type:\n1.Checking Account\n2.Saving Account\n*OR*\n3.Apply for loan')
            account_type = input('Enter your account type:')

            if account_type == '1':
                ch1 = CheckingAccount()
                ch1.info()
                ch1.new_account_deposit_amount()
                ch1.set_credit_limit(500)
                ch1.set_overdraft_fee(10)
                ch1.get_account_balance()
                obj_ = ch1.transaction_history_()
                ch1 = FileSaver()
                ch1.checking_account_records()
                ch1.transaction_history(obj_)

            elif account_type == '2':
                sv = SavingAccount()
                sv.info()
                print('Enter your choice:\n1.Apply for interest.\n2.deposit money')
                sv_acc_choice = input('Enter your choice:')

                if sv_acc_choice == '1':
                    sv.new_account_deposit_amount()
                    sv.apply_interest()
                    sv.get_account_balance()
                elif sv_acc_choice == '2':
                    sv.new_account_deposit_amount()
                    sv.get_account_balance()

                else:
                    print('Invalid choice.')

                obj_ = sv.transaction_history_()
                sv = FileSaver()
                sv.saving_account_records()
                sv.transaction_history(obj_)

            elif account_type == '3':
                ln = Loan()
                ln.info()
                ln.set_loan_info()
                ln.get_account_balance()
                obj_ = ln.transaction_history_()
                ln = FileSaver()
                ln.loan_records()
                ln.transaction_history(obj_)

            else:
                print('Invalid Choice.\nKindly restart.')

        # if user choice is invalid
        else:
            print('Your choice is invalid.\n Kindly restart.')


# if user is customer
class Customer(User):
    Customer_account_no = ''
    records = []

    def info(self):
        """ The takes information about user customer who is creating new account."""

        # taking customer's: user_id, account_no and user_name
        self.__customer_user_name = input('Enter yor name in letters:').lower()
        while not ('a' <= self.__customer_user_name <= 'z'):

            print("You entered an int instead of str.")

        else:
            Customer.records.append(self.__customer_user_name)

        # taking customer's: password
        m = 0
        while m == 0:
            self.__password = input("Enter password for your account:")

            if len(self.__password) >= 7 and re.match("^(?=.([a-z-A-Z])(?=.\d)(?=.*[@#$%^&+=]))", self.__password):
                print("INVALID")

            else:
                m += 1
                print("Password has been created")
                Customer.records.append(self.__password)
                break

        # taking customer's: email_id
        while True:
            self.__customer_email_id = input('Enter your gmail id :')

            if '@gmail.com' in self.__customer_email_id:
                Customer.records.append(self.__customer_email_id)
                break

            else:
                print('The e-mail id you entered is invalid.')

        # taking customer's: country code
        while True:
            try:
                self.__country_code = int(input('enter your country code in numbers:'))
                assert len(str(self.__country_code)) != 0 and 1 <= len(str(self.__country_code)) <= 3

            except ValueError:
                print("You country code should be in numbers 'xx' or 'x'.")

            except AssertionError:
                print("Your code length should in between 1 to 3.")

            else:
                Customer.records.append('+' + str(self.__country_code))
                break

        # taking customer's: phone number
        while True:
            try:
                self.phone_no = int(input('Enter your phone number:'))
                self.__customer_phone_no = str(self.__country_code) + str(self.phone_no)
                Customer.records.append(self.__customer_phone_no)
                break

            except ValueError:
                print("The value you have entered is not a number.")

        # taking customer's: address(area, city and country)
        print('Kindly enter your address.\nIt must contain your area,city and country')
        while True:
            self.__country = input('enter your country name:').lower()

            if self.__country != (0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9) \
                    and (('a' <= self.__country <= 'z') or ('A' <= self.__country <= 'Z')):
                Customer.records.append(self.__country)
                break

            else:
                print("kindly enter your country.")

        city = input('Enter your city name:').lower()
        area = input('Enter your area name:').lower()

        while not ('a' <= city <= 'z') and not('a' <= area <= 'z'):
            print('Kindly enter your correct city and area.')

        else:
            self.__customer_address = self.__country + ',' + city + ',' + area
            Customer.records.append(self.__customer_address)

        # taking customer's: gender
        while True:
            print('choose Male or Female.')
            self.__gender = input("enter your gender: ").lower()
            if self.__gender == 'male' or self.__gender == 'female':
                Customer.records.append(self.__gender)
                break

            else:
                print('Kindly give appropriate answer.')

        # taking customer's: age
        class Error(Exception):
            pass

        try:
            age = float(input('enter your age:'))
            if age < 18:
                raise Error

            else:
                self.__customer_age = str(age) + ' yrs'
                Customer.records.append(self.__customer_age)

        except Error:
            print("You are under aged or minor.\nSo we can not open an account for you.")
            exit()

        except ValueError:
            print("The value you have entered is not an age.")

        Error()
        print('You have successfully created an account.')
        self.__customer_account_no = generate_account_number()
        Customer.records.append(self.__customer_account_no)
        print('Your account number is', self.__customer_account_no)
        Customer.Customer_account_no = self.__customer_account_no

    def login(self, file):
        """ The function works when user is loging his account,"""

        self.__customer_account_no = input('enter your account number:')
        self.bank_records_file = open(file, 'r+')
        self.file = self.bank_records_file.read()
        self.bank_records_file.seek(0)

        # searching customer's: user_id, account_no and password
        for records in self.bank_records_file:  # range = no. of lines
            for data in eval(records):
                if (eval(records)[-2]) == self.__customer_account_no:
                    print('Successfully login.')
                    print(records)
                    print(type(records))
                    Customer.records = eval(records)
                    Customer.Customer_account_no = self.__customer_account_no
                    break  # to break the otherwise it will print records on the basis of no. of index of list

            # if these statements would inside in nested loop it will print multiple times
            if self.__customer_account_no not in self.file:  # if user enter invalid user id
                print('Invalid user id.')
                break  # to break 3 times

    def delete_account(self):
        """Delete the account and its records"""

        self.__customer_account_no = input('Enter your account number:')

        # Call the delete_customer_records method of FileSaver class
        file_saver = FileSaver()
        file_saver.delete_customer_records(self.__customer_account_no)

        print('Your account and records have been deleted.')


# if user is admin
class Administrator(User):
    def login(self):
        """ The function takes about admin who is loging his account."""

        self.__administrator_user_id = input('Enter your id:')
        self.__administrator_user_name = input('Enter your name:')
        self.__administrator_password = input('Enter your account password:')

        # searching admin info
        self.admin_file = open('Admin.txt', 'r+')
        a = self.admin_file.readline()
        b = self.admin_file.readline()
        self.admin_file.seek(0)

        # loging admin account
        for records in self.admin_file:  # loop iterates 2 times
            for item in eval(records):  # nested loop iterates 3 times
                if (eval(records)[2]) == self.__administrator_password and \
                        (eval(records)[1]) == self.__administrator_user_name and \
                        (eval(records)[0]) == self.__administrator_user_id:
                    print('Successfully login.')
                    break  # to break 3 times

                else:
                    print(end='')

            # if user enters two different inputs of both admin ids
            if (self.__administrator_user_id in b) and (self.__administrator_user_name in a):
                print('OOPs.')
                break
            if (self.__administrator_user_id in a) and (self.__administrator_user_name in b):
                print('OOPs.')
                break

            # if user enters invalid id
            if (self.__administrator_user_id not in a) and (self.__administrator_user_id not in b):
                print('invalid user id.')

            # if user enters invalid name
            if (self.__administrator_user_name not in a) and (self.__administrator_user_name not in b):
                print('invalid user name.')

            # if user enters invalid account password
            if (self.__administrator_password not in a) and (self.__administrator_password not in b):
                print('invalid user password.')
                break  # to break 2 times

    def get_records(self):
        """ The function will return all bank records."""

        self.bank_records_file1 = open('CheckingAccountRecords.txt', 'r').read()
        self.bank_records_file2 = open('SavingAccountRecords.txt.txt', 'r').read()
        self.bank_records_file3 = open('LoanRecords.txt', 'r').read()

        for items in self.bank_records_file1:
            print(items + '\n')

        for items in self.bank_records_file2:
            print(items + '\n')

        for items in self.bank_records_file3:
            print(items + '\n')


# Customer who has an account
class Account(ABC):
    bank_balance = 0

    def info(self):
        """ The function will take info about customer."""

        c = Customer()
        c.info()
        self.__new_amount_deposit = 'new_amount_deposit'
        self.deposit_amount_ = 'deposit_amount'
        self.withdraw_amount_ = 'withdraw_amount'

    def new_account_deposit_amount(self):
        """The function takes money as input to save in account only when user customer is creating new account."""

        while True:
            try:
                self.t = datetime.today()
                self.__new_amount_deposit = int(input('enter the amount you want put in your  account:'))
                Account.bank_balance = self.__new_amount_deposit
                Customer.records.append(str(Account.bank_balance))
                self.transaction_amount = self.__new_amount_deposit
                self.transaction_history = f'Deposit amount:{self.transaction_amount}, Time:{self.t},' \
                                           f'Total balance:{Account.bank_balance}'
                break

            except ValueError:
                print("The amount of money you have entered is invalid.")

    def withdraw_amount(self):
        """The function works when a customer wants to withdraw money from his account."""
        pass

    def deposit_amount(self):
        """The function works when a customer wants to withdraw money from his account."""
        pass

    def get_account_info(self):
        """The function returns info of a customer."""

        print(Customer.records)

    @abstractmethod
    def get_account_balance(self):
        return Account.bank_balance

    def transaction_history_(self):
        """The function has transaction history of an account"""

        return self.transaction_history


# if user wants to take loan
class Loan(Account):
    principal_amount = 0
    interest_rate = 8.6
    loan_duration = 0
    __loan_balance = 0

    def info(self):
        """The function takes information about the loan from the user."""

        super().info()

    def login(self, file):
        """ The function works when user is loging his account,"""

        l_ = Customer()
        l_.login(file)

    def set_loan_info(self):
        """The function sets the loan details entered by the user."""

        self.t = datetime.today()
        self.__principal_amount = float(input('Enter the principal amount: '))
        self.__loan_duration = int(input('Enter the loan duration (in months): '))
        self.__loan_balance = self.principal_amount
        Customer.records.append(str(self.__loan_balance))
        self.transaction_amount = self.__loan_balance
        self.transaction_history = f'Loan duration:{self.__loan_duration}, Loan Balance left:' \
                                   f'{self.transaction_amount}, Time:{str(self.t)}'


    def debit_monthly_interest(self):
        """The function deducts the monthly interest from the loan balance."""

        monthly_interest = (self.interest_rate / 100) * self.__loan_balance
        self.__loan_balance -= monthly_interest
        self.initial_loan = int(Customer.records[-1])
        file_ = open('LoanRecords.txt').read()
        for records in file_:
            self.t = datetime.today()
            if Customer.records == records:
                Customer.records[-1] = str(self.__loan_balance)
                self.transaction_amount = self.__loan_balance
                self.transaction_history = f'Loan duration:{self.__loan_duration},Initial Loan Balance:{self.initial_loan} ' \
                                           f'Loan Balance left:{self.transaction_amount}, Time:{str(self.t)}'
            else:
                print('')

    def get_account_balance(self):
        """The function prints the current loan balance."""

        Account.bank_balance = Customer.records[-1]
        return f'Loan Balance: {Account.bank_balance}'

    def transaction_history_(self):
        """The function has transaction history of an account"""

        return self.transaction_history


class CheckingAccount(Account):
    def info(self):
        """The function takes information about user's checking account."""

        super().info()
        self.credit_limit = 0
        self.overdraft_fee = 0

    def login(self, file):
        """ The function works when user is loging his account,"""

        ch = Customer()
        ch.login(file)

    def set_credit_limit(self, limit):
        """The function sets the credit limit for the user's checking account"""

        self.credit_limit = limit

    def set_overdraft_fee(self, fee):
        """The function sets overdraft fee when user's balance goes to negative."""

        self.overdraft_fee = fee

    def withdraw_amount(self):
        """The function works when a customer wants to withdraw money from his checking account."""

        Account.bank_balance = int(Customer.records[-1])
        self.t = datetime.today()
        file_ = open('CheckingAccountRecords.txt').read()
        for records in file_:
            self.t = datetime.today()
            self.__withdraw_amount = int(input('Enter the amount you want to withdraw from your current account:'))
            if Customer.records == records:
                # if withdrawal amount is less than or equal to account balance:
                if self.__withdraw_amount <= Account.bank_balance:
                    Account.bank_balance -= self.__withdraw_amount
                    Customer.records[-1] = Account.bank_balance
                    print('Withdrawal successful.')
                    self.transaction_amount = self.__withdraw_amount
                    self.transaction_history = f'withdrawal amount:{self.transaction_amount}, Time:{str(self.t)},' \
                                               'Total Balance:{Account.bank_balance}'

                #  if withdrawal amount is greater than account balance
                elif self.__withdraw_amount <= Account.bank_balance + self.credit_limit:
                    self.t = datetime.today()
                    overdraft_choice = input('Withdrawal amount exceeds account balance. '
                                                'Do you want to proceed with overdraft? (y/n):').lower()

                    if overdraft_choice == 'y':  # if customer wants to withdraw
                        self.__overdraft_amount = self.__withdraw_amount - Account.bank_balance
                        self.new_amount = Account.bank_balance - self.__withdraw_amount - self.overdraft_fee
                        Account.bank_balance = self.new_amount
                        Customer.records[-1] = Account.bank_balance
                        print('Withdrawal successful. Overdraft amount:', self.__overdraft_amount)
                        self.transaction_amount = self.__overdraft_amount
                        self.transaction_history = f'Overdraft amount:{self.transaction_amount}, Time:{str(self.t)},' \
                                                    f'Total Balance:{Customer.records[-1]}'

                    else:
                        print('Withdrawal canceled.')

            else:
                print('Insufficient funds.')

    def deposit_amount(self):
        """The function works when a customer wants to withdraw money from his account."""

        Account.bank_balance = int(Customer.records[-1])
        file_ = open('CheckingAccountRecords.txt').read()
        for records in file_:
            self.t = datetime.today()
            self.__deposit_amount = int(input('Enter the amount you want to deposit:'))
            if Customer.records == records:
                Account.bank_balance += self.__deposit_amount
                Customer.records[-1] = Account.bank_balance
                self.transaction_amount = self.__deposit_amount
                self.transaction_history = f'Overdraft amount:{self.transaction_amount}, Time:{str(self.t)},' \
                                           f'Total Balance:{Account.bank_balance}'
                print('Deposit successful.')
            break

    def get_account_balance(self):
        """The function prints the current account balance."""

        print(f'Current Account Balance: {Account.bank_balance}')

    def transaction_history_(self):
        """The function has transaction history of an account"""

        return self.transaction_history

class SavingAccount(Account):
    def info(self):
        """The function takes information about user's saving account."""

        super().info()
        self.interest_rate = 0

    def login(self, file):
        """ The function works when user is loging his account,"""

        sv = Customer()
        sv.login(file)

    def deposit_amount(self):
        """The function works when a customer wants to withdraw money from his account."""

        Account.bank_balance = int(Customer.records[-1])
        file_ = open('SavingAccountRecords.txt').read()
        for records in file_:
            self.t = datetime.today()
            self.__deposit_amount = int(input('Enter the amount you want to deposit:'))
            if Customer.records == records:
                Account.bank_balance += self.__deposit_amount
                (eval(records)[-1]) = str(Account.bank_balance)
                self.transaction_amount = self.__deposit_amount
                self.transaction_history = f'Overdraft amount:{self.transaction_amount}, Time:{str(self.t)},' \
                                       f'Total Balance:{Account.bank_balance}'
                print('Deposit successful.')
            break

    def apply_interest(self):
        """The function updates the account balance according to the bank's applied interest rate."""

        self.interest_rate = 0.05  # Assuming interest rate is 5%
        Account.bank_balance = int(Customer.records[-1])
        self.new_amount = int(Account.bank_balance * self.interest_rate)
        Account.bank_balance += self.new_amount
        Customer.records[-1] = Account.bank_balance

    def withdraw_amount(self):
        """The function works when a customer wants to withdraw money from their savings account."""

        Account.bank_balance = int(Customer.records[-1])
        file_ = open('SavingAccountRecords.txt').read()
        for records in file_:
            self.t = datetime.today()
            self.__withdraw_amount = int(input('Enter the amount you want to withdraw from your saving account:'))
            if Customer.records == records:
                if self.__withdraw_amount <= Account.bank_balance:
                    Account.bank_balance -= self.__withdraw_amount
                    Customer.records[-1] = Account.bank_balance
                    self.transaction_amount = self.__withdraw_amount
                    self.transaction_history = f'Overdraft amount:{self.transaction_amount}, Time:{str(self.t)}, \
                                                Total Balance:{Account.bank_balance}'
                    print('Withdrawal successful.')
                else:
                    print("Insufficient funds in your savings account.")
                break  # to break the loop

    def get_account_balance(self):
        """The function prints the saving account balance."""

        return f'Saving Account Balance: {Account.bank_balance}'

    def transaction_history_(self):
        """The function has transaction history of a saving account"""

        return self.transaction_history


# Saving all bank records in a file
class FileSaver(SavingAccount, CheckingAccount, Loan, Customer):

    def saving_account_records(self):
        """ The function saves all info related customers of saving account."""

        self.bank_records_file = open('SavingAccountRecords.txt', 'a+')
        self.bank_records_file.write(str(Customer.records) + '\n')
        self.acc_no =  f'Account number:{Customer.Customer_account_no}'

    def checking_account_records(self):
        """ The function saves all info related customers of checking account."""

        self.bank_records_file = open('CheckingAccountRecords.txt', 'a+')
        self.bank_records_file.write(str(Customer.records) + '\n')
        self.acc_no =  f'Account number:{Customer.Customer_account_no}'

    def loan_records(self):
        """ The function saves all info related customers who take loan."""

        self.bank_records_file = open('LoanRecords.txt', 'a+')
        self.bank_records_file.write(str(Customer.records) + '\n')
        self.acc_no =  f'Account number:{Customer.Customer_account_no}'

    def transaction_history(self, obj_):
        """The function keeps all records of transaction history."""

        self.bank_records_file = open('TransactionHistory.txt', 'a+')
        self.acc_no = f'Account number:{Customer.Customer_account_no}'
        self.transaction = obj_
        self.bank_records_file.write(str(self.acc_no)+ '=>' + str(self.transaction) + '\n')

    def delete_customer_records(self, customer_account_no):
        """Delete the records of a particular customer from the file"""

        file_list = ['CheckingAccountRecords.txt', 'SavingAccountRecords.txt', 'LoanRecords.txt']
        for files in file_list:
            # Open the file in read mode and read all lines
            with open(files, 'r') as file:
                lines = file.readlines()

            # Open the file in write mode and write all lines except the one to be deleted
            with open(files, 'w') as file:
                for line in lines:
                    if customer_account_no not in line:
                        file.write(line)

        print(f"Records of customer with account number {customer_account_no} deleted.")


u = User()
u.login_()
