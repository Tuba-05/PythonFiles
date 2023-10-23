"""BAKE SHOP CODE"""
Employee1_hours_worked = 2
Employee2_hours_worked = 3
Employee1_wage_rate_per_hour = 3000
Employee2_wage_rate_per_hour = 3000


def employees_():
    """ function calculates wages and bonus of employees. It also adds working hours for employees. """
    def employee_wages():
        """ function calculates wages of employees. """
        global Employee1_hours_worked, Employee2_hours_worked, Employee1_wage_rate_per_hour, \
            Employee2_wage_rate_per_hour
        employee1_wage = (Employee1_hours_worked * Employee1_wage_rate_per_hour)
        employee2_wage = (Employee2_hours_worked * Employee2_wage_rate_per_hour)
        print(f"First employee wage is {employee1_wage} rupees and"
              f" Second employee wage is {employee2_wage} rupees.")

        def employees_bonus(s, r):
            """ function calculates bonus of employees if the condition fulfills. """
            nonlocal employee1_wage, employee2_wage
            if s <= 3 or r <= 3:
                employee1_bonus = employee1_wage + 1000
                employee2_bonus = employee2_wage + 1000
                print(f"First employee bonus is {employee1_bonus} rupees and"
                      f" Second employee bonus is {employee2_bonus} rupees.")
            else:
                print('No bonus for both employees.')

        print(" For bonus of both employees please enter the current number of rolls and samosas in the stock.")
        employees_bonus(s=int(input('Enter samosas_left:')), r=int(input('Enter rolls_left:')))

    def add_hours():
        """ function adds working hours for employees. """
        employee1_hours_worked = int(input('enter first employee working hours:'))
        employee2_hours_worked = int(input('enter second employee working hours:'))
        print(f"New working hours for First employee is {employee1_hours_worked} "
              f"and for Second employee is {employee2_hours_worked}.")

    print('Choose options\n 1. Calculate wages\n 2. Add hours worked\n 3. EXIT')
    choice_ = input("Enter your choice:")
    if choice_ == '1':
        employee_wages()
    elif choice_ == '2':
        add_hours()
    else:
        print('THANK YOU FOR VISITING\nEXIT')


def food():
    """ function helps in buying food items in food shop. """
    samosas_in_stock = 25
    rolls_in_stock = 25
    samosa_unit_price = 20
    roll_unit_price = 30
    total_bill = 0
    print('Choose an option\n 1. Add items to the stock\n 2. Want to order something')
    option = input('Enter your option:')
    if option == '1':
        print('How many samosa and roll, you want to add in the current stock?')
        add_samosa = int(input('Enter number of samosas you want to add in stock:'))
        add_roll = int(input('Enter number of rolls you want to add in stock:'))
        samosas_in_stock += add_samosa
        rolls_in_stock += add_roll
        print(f'Total number of samosas = {samosas_in_stock} and rolls = {rolls_in_stock} in the stock.')
    elif option == '2':
        print(' How many rolls and samosas you want to order?')
        samosa_order = int(input('Enter number of samosa you want to buy:'))
        roll_order = int(input('Enter number of roll you want to buy:'))
        total_bill += (samosa_order * samosa_unit_price) + (roll_order * roll_unit_price)
        samosas_left = samosas_in_stock - samosa_order
        rolls_left = rolls_in_stock - roll_order
        print(f"Now {samosas_left} number of samosas left in stock and {rolls_left} number of rolls left in "
              f"stock.\nYour total bill is {total_bill} rupees.")
    else:
        print(" THANK YOU FOR VISITING\nEXIT ")
    print('If you want to visit boutique press "Y" for yes')
    customer_reply = input().lower()
    if customer_reply == "y":
        boutique()
    else:
        print('THANK YOU FOR VISITING\nEXIT')


def boutique():
    """ function helps in buying clothes. """
    pant_shirt_in_stock = 15
    shalwar_kameez_in_stock = 25
    pant_shirt_unit_price = 3500
    shalwar_kameez_unit_price = 5000
    total_bill = 0
    print('Choose an option\n 1. Add items to the stock\n 2. Want to order something')
    option = input('Enter your option:')
    if option == '1':
        print('How many pair of pant shirt and shalwar kameez, you want to add in the current stock?')
        add_pant_shirt = int(input('Enter number of pant shirt you want to add in stock:'))
        add_shalwar_kameez = int(input('Enter number of shalwar kameez you want to add in stock:'))
        pant_shirt_in_stock += add_pant_shirt
        shalwar_kameez_in_stock += add_shalwar_kameez
        print(f'Total number of pant shirt = {pant_shirt_in_stock} and '
              f'shalwar kameez = {shalwar_kameez_in_stock} in the stock.')
    elif option == '2':
        print(' How many pant shirts and shalwar kameez you want to order?')
        pant_shirt_order = int(input('Enter number of pant shirt you want to buy:'))
        shalwar_kameez_order = int(input('Enter number of shalwar kameez you want to buy:'))
        pant_shirt_left = pant_shirt_in_stock - pant_shirt_order
        shalwar_kameez_left = shalwar_kameez_in_stock - shalwar_kameez_order
        total_bill += (pant_shirt_order * pant_shirt_unit_price) + (shalwar_kameez_order * shalwar_kameez_unit_price)
        print(f"Now {pant_shirt_left} number of pant shirt left in stock and {shalwar_kameez_left} number of shalwar "
              f"kameez left in stock.\nYour total bill is {total_bill} rupees.")
    else:
        print(" THANK YOU FOR VISITING\nEXIT ")
    print('If you want to visit food shop press "Y" for yes')
    customer_reply = input().lower()
    if customer_reply == "y":
        food()
    else:
        print('THANK YOU FOR VISITING\nEXIT')


def main():
    """ function helps in access food shop, boutique or employee payment. """
    print('Welcome to Bake Shop.\n Where do you want to visit'
          '\n 1. Food shop\n 2. Boutique\n 3. Want to check employees payment\n 4. EXIT')
    choice = input('Enter your choice:')
    if choice == '1':
        food()
    elif choice == '2':
        boutique()
    elif choice == '3':
        employees_()
    else:
        print(" THANK YOU FOR VISITING\n EXIT ")


main()
