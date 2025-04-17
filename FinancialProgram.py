#import packs
from datetime import datetime
expenselist = []
incomelist = []
currency = ""

#function defining
#Age Verifier which is an added feature to make the program different
def agecheck():
    print()
    print("*----------------------Age Verification------------------------*")
    print()
    print("We need to confirm you are over 18 years old to continue.")
    age = input("Can you confirm your age?: ")
    if age.isnumeric():
        age = int(age)
        if age >= 18:
            print()
            print("Thank you for confirming!")
        else:
            print()
            print("You are not over 18 years old, please try again soon!")
            print()
            print("*----------------------------Exit-----------------------------*")
            exit()
    else:
        print()
        print("You have not entered a valid input, please try again.")
        agecheck()

#T&C Verifier
#Verifier which is an added feature to make the program different
def termscheck():
    print()
    print("*-------------------Terms & conditions-------------------------*")
    print()
    print("Please read and agree to the terms and conditions of the app.")
    print("You can find them here: https://www.FinancialProgram.com/t&Cs")
    print()
    agree = input("Do you agree to the terms and conditions? (Y/N) ")
    if agree.upper() == "Y":
        print()
        print("Thank you for agreeing to the terms and conditions!")
    else:
        print()
        print("You have not agreed to the terms and conditions, we can therefore not allow you to continue. Please try again later!")
        exit()

#Front Page function allowing the user to select what they want to do, allows the user to exit the program.
def frontpage():
    print()
    print("*-------------------------Front Page---------------------------*")
    print()
    print("What would you like to do today?")
    print()
    print("1. View your income Options")
    print()
    print("2. View your expenses Options")
    print()
    print("3  Work out VAT on an Item (UK only)")
    print()
    print("4. View totals and comparisons")
    print()
    print("5. Exit the app")
    print()
    answer = int(input("Answer (1, 2, 3, 4, 5): "))
    if answer == 1:
        incomeoptions()
    elif answer == 2:
        expenseoptions()
    elif answer == 3:
        VATUK()
    elif answer == 4:
        comparisons()
    elif answer == 5:
        print()
        print("Thank you for using our service, we hope you enjoyed it!")
        print("Goodbye!")
        print()
        print("*----------------------------Exit-----------------------------*")
        exit()
    else:
        print()
        print("You have not entered a valid answer, please try again.")
        frontpage()

#income Options Page
def incomeoptions():
    print()
    print("*-------------------------Income Options-----------------------*")
    print()
    print("Here are your income options:")
    print()
    print("1. Add an Income.")
    print()
    print("2. View your Incomes already added.")
    print()
    print("3. Delete an Income.")
    print()
    print("4. Return to the main menu.")
    print()
    incans = input("What would you like to do? (1, 2, 3, 4): ")
    if incans == "1":
        incomecalc()
    elif incans == "2":
        viewincome()
    elif incans == "3":
        deleteincome()
    elif incans == "4":
        frontpage()
    else:
        print()
        print("You have not entered a valid answer, please try again.")
        incomeoptions()

#Expense Options Page
def expenseoptions():
    print()
    print("*------------------------Expense Options-----------------------*")
    print()
    print("Here are your expense options:")
    print()
    print("1. Add an expense.")
    print()
    print("2. View your expenses already added.")
    print()
    print("3. Delete an expense.")
    print()
    print("4. Return to the main menu.")
    print()
    expans = input("What would you like to do? (1, 2, 3, 4): ")
    if expans == "1":
        expensecalc()
    elif expans == "2":
        viewexpense()
    elif expans == "3":
        deleteexp()
    elif expans == "4":
        frontpage()
    else:
        print()
        print("You have not entered a valid answer, please try again.")
        expenseoptions()

'''Main Body of the add an income function, contains nested If statements, while loops both nested and un-nested,
for loops and try except for the date feature'''
def incomecalc():
    global incomelist
    global newincome
    while True:
        print()
        print("*-------------------------Add Income---------------------------*")
        print()
        addincome = input("Add an income, Press Y to continue or N to go back. ")
        print()
        if addincome.upper() == "Y":
            newincome = {}
            date = input("Enter the date of the income (dd/mm/yyyy): ")
            print()
            try:
                date = datetime.strptime(date, "%d/%m/%Y")
            except ValueError:
                print("You have not entered a valid date, please try again.")
                incomecalc()
            newincome["date"] = date.strftime("%d/%m/%Y")
            print("1. Active income (Wage, Salary, Benefits, etc.)")
            print("2. Portfolio income (Interest, Dividends, etc.)")
            print("3. Passive income (Investments, Rental, etc.)")
            print("4. Other income (Gifts, Savings, etc.)")
            print()
            newincometype= input("Please select from the list the type of income and insert the number: ")
            print()
            while True:
                if newincometype == "1":
                    newincome["type"] = "Active income"
                    break
                elif newincometype == "2":
                    newincome["type"] = "Portfolio income"
                    break
                elif newincometype == "3":
                    newincome["type"] = "Passive income"
                    break
                elif newincometype == "4":
                    newincome["type"] = "Other income"
                    break
                else:
                    print("You have not entered a valid number, please try again.")
                    print()
                    newincometype = input("Please select from the list the type of income and insert the number: ")
                    print()
            newincome["amount"] = input(f"Enter the amount of the income: {currency}")
            newincome["amount"] = float(newincome["amount"])
            print()
            incomelist.append(newincome)
            print(f"Income added successfully! This is your entry: {newincome['date'], newincome['type'], newincome['amount']}")
        elif addincome.upper() == "N":
            print("You have chosen not to add an income.")
            print(f"Here is your list of incomes: {incomelist}")
            incomeoptions()
            break
        else:
            print("You have not entered a valid input, please use Y or N.")
            print()

'''Main Body of the add an expense function, contains same loops and if statements as the income section, also contains
the try and except for the date feature'''
def expensecalc():
    global expenselist
    global newexpense
    while True:
        print()
        print("*-------------------------Add Expense--------------------------*")
        print()
        addexpense = input("Add an Expense, Press Y to conitnue or N to go back. ")
        print()
        if addexpense.upper() == "Y":
            newexpense = {}
            date = input("Enter the date of the Expense (dd/mm/yyyy): ")
            try:
                date = datetime.strptime(date, "%d/%m/%Y")
            except ValueError:
                print()
                print("You have not entered a valid date, please try again.")
                print()
                expensecalc()
            newexpense["date"] = date.strftime("%d/%m/%Y")
            print()
            print("1. Housing expenses (Rent, Mortgage, Loan, etc.)")
            print("2. Utilities expenses (Electricity, Water, Gas, etc.)")
            print("3. Food expenses (Food, Drinks, Restaurants, etc.)")
            print("4. Transport expenses (Car, Travel, Airplane, etc.)")
            print("5. Entertainment expenses (Movies, TV, Music, etc.)")
            print("6. Education expenses (School, University, etc.)")
            print("7. Health expenses (Medical, Dental, Blood, etc.)")
            print("8. Other expenses (Clothes, Subscriptions, etc.)")
            print()
            newexpensetype = input("Please select from the list the type of expense and insert the number: ")
            print()
            while True:
                if newexpensetype == "1":
                    newexpense["type"] = "Housing expenses"
                    break
                elif newexpensetype == "2":
                    newexpense["type"] = "Utilities expenses"
                    break
                elif newexpensetype == "3":
                    newexpense["type"] = "Food expenses"
                    break
                elif newexpensetype == "4":
                    newexpense["type"] = "Transport expenses"
                    break
                elif newexpensetype == "5":
                    newexpense["type"] = "Entertainment expenses"
                    break
                elif newexpensetype == "6":
                    newexpense["type"] = "Education expenses"
                    break
                elif newexpensetype == "7":
                    newexpense["type"] = "Health expenses"
                    break
                elif newexpensetype == "8":
                    newexpense["type"] = "Other expenses"
                    break
                else:
                    print("You have not entered a valid number, please try again.")
                    print()
                    newexpensetype = input("Please select from the list the type of expense and insert the number: ")
                    print()
            newexpense["amount"] = input(f"Enter the amount of the expense: {currency}")
            print()
            newexpense["amount"] = float(newexpense["amount"])
            expenselist.append(newexpense)
            print(f"Expense added successfully! This is your entry: {newexpense['date'], newexpense['type'], newexpense['amount']}")
        elif addexpense.upper() == "N":
            print("You have chosen not to add an expense.")
            print(f"Here is your list of expense: {expenselist}")
            expenseoptions()
            break
        else:
            print("You have not entered a valid input, please use Y or N.")

#View The whole list of incomes
def viewincome():
    print()
    print("*-------------------------View Income--------------------------*")
    print()
    if incomelist == []:
        print("You have not added any incomes yet, please go back and add an income before trying again!")
        incomeoptions()
    else:
        print(incomelist)
        incomeoptions()

#View The whole list of expenses
def viewexpense():
    print()
    print("*-------------------------View Expense-------------------------*")
    print()
    if expenselist == []:
        print("You have not added any expenses yet, please go back and add an expense before trying again!")
        expenseoptions()
    else:
        print(expenselist)
        expenseoptions()

'''Main Body of the delete an income function, uses the try and except for the date feature as verification.
uses a for loop to run through an unlimted number of incomes to search for the correct dictionary to delete'''
def deleteincome():
    print()
    print("*-------------------------Delete income------------------------*")
    print()
    if incomelist == []:
        print("You have not added any incomes yet, please go back and add an income before trying again!")
        incomeoptions()
    else:
        print("Please enter the date of the income you would like to delete.")
    print()
    deldate = input("Date dd/mm/yyyy: ")
    print()
    delinc = input("How much was the income for that you want to delete? ")
    delinc = float(delinc)
    print()
    try:
        date = datetime.strptime(deldate, "%d/%m/%Y")
    except ValueError:
        print("You have not entered a valid date, please try again.")
        print()
        deleteincome()
    for newincome in incomelist:
        if newincome["date"] == deldate and newincome["amount"] == delinc:
            incomelist.remove(newincome)
            print(f"Income deleted successfully! This is your remaining Incomes: {incomelist}")
            break
    incomeoptions()
'''Main Body of the delete an Expense function, uses the try and except for the date feature as verification.
uses a for loop to run through an unlimted number of expenses to search for the correct dictionary to delete'''
def deleteexp():
    print()
    print("*------------------------Delete Expense------------------------*")
    print()
    if expenselist == []:
        print("You have not added any expenses yet, please go back and add an expense before trying again!")
        expenseoptions()
    else:
        print("Please enter the date of the expense you would like to delete.")
    print()
    deldate = input("Date dd/mm/yyyy: ")
    print()
    delexp = input("How much was the expense for that you want to delete? ")
    delexp = float(delexp)
    print()
    try:
        date = datetime.strptime(deldate, "%d/%m/%Y")
    except ValueError:
        print("You have not entered a valid date, please try again.")
        print()
        deleteexp()
    for newexpense in expenselist:
        if newexpense["date"] == deldate and newexpense["amount"] == delexp:
            expenselist.remove(newexpense)
            print(f"Expense deleted successfully! This is your remaining Expenses: {expenselist}")
            break
    expenseoptions()

'''An added function to make the program different, lets the user calculate the amount of tax on an item for sale.
only used for UK purposes and provides information on the current tax rate, price before vat, price after vat
and the total amount of VAT on the item'''
def VATUK():
    uksalestax = 20
    print()
    print("*-------------------Sales Tax Calculator (UK)-------------------*")
    print()
    print(f"The UK Sales Tax rate is {uksalestax}%")
    print("Please enter the amount of the item.")
    print()
    while True:
        amountb4vat = float(input("Amount: £"))
        try:
            amountaftervat = amountb4vat / 1.2
            break
        except TypeError or ValueError:
            print("You have not entered a valid number, please try again.")
            print("Please enter the amount of the item with the decimal point.")
            print("Exaample: 10.00 or 9.99 or 0.50")
    vatamount = amountb4vat - amountaftervat
    print()
    print("Calculating VAT on an Item (UK only)...")
    print()
    print(f"The amount of VAT is £{vatamount}")
    print(f"The total amount of the item is £{amountaftervat + vatamount}")
    frontpage()

'''Main body of the comparisons function, allows the user to view the sum of all the incomes put together, view the sum
of all the expenses put together, work out the remaining balance after total income is taken away from total expenses.
float() was added as if the user entered the amount as a decimal the program would crash when working out totals.'''
def comparisons():
    if incomelist == [] or expenselist == []:
        print()
        print("You need to add both an income and expense to select this option, please go back and add both before trying again!")
        frontpage()
    else:
        print()
    highestincome = max(income["amount"] for income in incomelist)
    highestexpense = max(expense["amount"] for expense in expenselist)
    lowestincome = min(income["amount"] for income in incomelist)
    lowestexpense = min(expense["amount"] for expense in expenselist)
    totalincome = sum(income["amount"] for income in incomelist)
    totalexpense = sum(expense["amount"] for expense in expenselist)
    totalleftover = totalincome - totalexpense
    while True:
        print("*----------------------View Comparisons-----------------------*")
        print()
        print("What would you like to know or compare?")
        print()
        print("1. Total Income Amount, and highest Income Amount inputted")
        print()
        print("2. Total Expense Amount, and highest Expense Amount inputted")
        print()
        print("3. Total Leftover (Total Income - Total Expense)")
        print()
        print("4. Highest and lowest income and expenses amounts")
        print()
        print("5. Return to the main menu")
        print()
        compans = input("What would you like to do? (1, 2, 3, 4): ")
        print()
        if compans == "1":
            print(f"Total income amount is {currency}{totalincome}")
            print()
        elif compans == "2":
            print(f"Total expense amount is {currency}{totalexpense}")
            print()
        elif compans == "3":
            print(f"Total leftover is {currency}{totalleftover}")
            print()
        elif compans == "4":
            print(f"Highest income amount is {currency}{highestincome}")
            print(f"Highest expense amount is {currency}{highestexpense}")
            print()
            print(f"Lowest income amount is {currency}{lowestincome}")
            print(f"Lowest expense amount is {currency}{lowestexpense}")
            print()
        elif compans == "5":
            frontpage()
            break
        else:
            print()
            print("You have not entered a valid answer, please try again.")
            print()

#Introduction
print()
print("*-----------------------Your Finances!-------------------------*")
print()
print("                 Welcome to Your Finances!")
print("                Please enter your full name")
print()

#Recieve user details
name = input("Your Name: ")
name = name.title()
print()
print(f"Hello {name}, Nice to meet you!")
print()

#runs the functions that Checks user is above 18 and agrees with terms and conditions of the app
agecheck()
termscheck()

'''Added feature to let user select a currency which is implemented later down the line in inputs and for when the
comparisons display the amounts'''
print("Lets find out what currency you use!")
print()
print("1. £")
print("2. $")
print("3. €")
print("4. Other")
print()
currency_input = input("Please select the currency sign you use (1, 2, 3, 4): ")
print()
while True:
    if currency_input == "1":
        currency = "£"
        break
    elif currency_input == "2":
        currency = "$"
        break
    elif currency_input == "3":
        currency = "€"
        break
    elif currency_input == "4":
        currency = ""
        break
    else:
        print()
        print("You have not entered a valid number, please try again.")
        print()
        currency_input = input("Please select the currency sign you use (1, 2, 3, 4): ")
        print()

#front page of program, starts the main program which interconnects all functions.
frontpage()
