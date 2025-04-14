#import packs
from datetime import datetime
expenselist = []
incomelist = []
viewexplist = []
viewinclist = []

#function defining
#Age Verifier which is an added feature to make the program different
def agecheck():
    print()
    print("We need to confirm you are over 18 years old to continue.")
    age = input("Can you confirm your age? ")
    if age.isnumeric():
        age = int(age)
        if age >= 18:
            print()
            print("Thank you for confirming!")
        else:
            print()
            print("You are not over 18 years old, please try again soon!")
            exit()
    else:
        print()
        print("You have not entered a valid input, please try again.")
        agecheck()

#T&C Verifier
#Verifier which is an added feature to make the program different
def termscheck():
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
        print("Thank you for using our service, we hope you enjoyed it!")
        print("Goodbye!")
        exit()
    else:
        print()
        print("You have not entered a valid answer, please try again.")
        frontpage()

#income Options Page
def incomeoptions():
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
        deleteexpense()
    elif expans == "4":
        frontpage()
    else:
        print()
        print("You have not entered a valid answer, please try again.")
        expenseoptions()

#Main Body of the add an income function, contains nested If statements, while loops both nested and un-nested,
#for loops and try except for the date feature
def incomecalc():
    global incomelist
    global newincome
    global viewinclist
    while True:
        print()
        addincome = input("Add an income, Press Y to conitnue or N to go back. ")
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
            newincometype= input("Please select from the list the type of income"
                                      " and insert the number: ")
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
                    newincometype = input("Please select from the list the type of income"
                                      "and insert the number: ")
                    print()
            newincome["amount"] = input(float("Enter the amount of the income: "))
            print()
            incomelist.append(newincome)
            viewinclist.append(newincome.get("date"))
            viewinclist.append(newincome.get("type"))
            viewinclist.append(newincome.get("amount"))
            print(f"Income added successfully! This is your entry: {newincome.values()}")
        elif addincome.upper() == "N":
            print("You have chosen not to add an income.")
            print(f"Here is your list of incomes: {incomelist}")
            incomeoptions()
            break
        else:
            print("You have not entered a valid input, please use Y or N.")
            print()

#Main Body of the add an expense function, contains same loops and if statements as the income section, also contains
#the try and except for the date feature
def expensecalc():
    global expenselist
    global newexpense
    global viewexplist
    while True:
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
            print("1. Housing expenses (Rent, Mortgage, Loan, etc.)")
            print("2. Utilities expenses (Electricity, Water, Gas, etc.)")
            print("3. Food expenses (Food, Drinks, Restaurants, etc.)")
            print("4. Transport expenses (Car, Travel, Airplane, etc.)")
            print("5. Entertainment expenses (Movies, TV, Music, etc.)")
            print("6. Education expenses (School, University, etc.)")
            print("7. Health expenses (Medical, Dental, Blood, etc.)")
            print("8. Other expenses (Clothes, Subscriptions, etc.)")
            print()
            newexpensetype = input("Please select from the list the type of expense"
                                  " and insert the number: ")
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
                    newincometype = input("Please select from the list the type of expenses"
                                          "and insert the number: ")
            newexpense["amount"] = input(float("Enter the amount of the expense: "))
            expenselist.append(newexpense)
            viewexplist.append(newexpense.get("date"))
            viewexplist.append(newexpense.get("type"))
            viewexplist.append(newexpense.get("amount"))
            print(f"Expense added successfully! This is your entry: {newexpense}")
        elif addexpense.upper() == "N":
            print("You have chosen not to add an expense.")
            print(f"Here is your list of expense: {expenselist}")
            expenseoptions()
            break
        else:
            print("You have not entered a valid input, please use Y or N.")

#View The whole list of incomes
def viewincome():
    if viewinclist == []:
        print("You have not added any incomes yet, please go back and add an income before trying again!")
        incomeoptions()
    else:
        print(viewinclist)
        incomeoptions()

#View The whole list of expenses
def viewexpense():
    if viewexplist == []:
        print("You have not added any expenses yet, please go back and add an expense before trying again!")
        expenseoptions()
    else:
        print(viewexplist)
        expenseoptions()

#Main Body of the delete an income function, uses the try and except for the date feature as verification.
#uses a for loop to run through an unlimted number of incomes to search for the correct dictionary to delete
def deleteincome():
    if incomelist == []:
        print("You have not added any incomes yet, please go back and add an income before trying again!")
        incomeoptions()
    else:
        print("Please enter the date of the income you would like to delete.")
    print()
    deldate = input("Date dd/mm/yyyy: ")
    print()
    delinc = input("How much was the income for that you want to delete?")
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

#Main Body of the delete an Expense function, uses the try and except for the date feature as verification.
#uses a for loop to run through an unlimted number of expenses to search for the correct dictionary to delete
def deleteexp():
    print("Please enter the date of the expense you would like to delete.")
    deldate = input("Date dd/mm/yyyy: ")
    delexp = input("How much was the income for that you want to delete?")
    try:
        date = datetime.strptime(deldate, "%d/%m/%Y")
    except ValueError:
        print("You have not entered a valid date, please try again.")
        deleteexp()
    for newexpense in expenselist:
        if newexpense["date"] == deldate and newexpense["amount"] == delexp:
            expenselist.remove(newexpense)
            print(f"Expense deleted successfully! This is your remaining Expenses: {expenselist}")
            break

#An added function to make the program different, lets the user calculate the amount of tax on an item for sale.
#only used for UK purposes and provides information on the current tax rate, price before vat, price after vat
#and the total amount of VAT on the item
def VATUK():
    UKSalesTax = 20
    print()
    print(f"The UK Sales Tax rate is {UKSalesTax}%")
    print("Please enter the amount of the item.")
    amountb4vat = input("Amount: ")
    print()
    amountb4vat = float(amountb4vat)
    amountaftervat = amountb4vat / 1.2
    vatamount = amountb4vat - amountaftervat
    print("Calculating VAT on an Item (UK only)...")
    print(f"The amount of VAT is {vatamount}")
    print(f"The total amount of the item is {amountaftervat + vatamount}")
    print()
    exit()

#Main body of the comparisons function, allows the user to view the sum of all the incomes put together, view the sum
#of all the expenses put together, work out the remaining balance after total income is taken away from total expenses.
#float() was added as if the user entered the amount as a decimal the program would crash when working out totals.
def comparisons():
    totalincome = sum(float(newincome["amount"]) for newincome in incomelist)
    totalexpense = sum(float(newexpense["amount"]) for newexpense in expenselist)
    while True:
        print("What would you like to know or compare?")
        print()
        print("1. Total Income Amount")
        print()
        print("2. Total Expense Amount")
        print()
        print("3. Total Leftover (Total Income - Total Expense)")
        print()
        print("4. Return to the main menu.")
        print()
        compans = input("What would you like to do? (1, 2, 3, 4): ")
        if compans == "1":
            print(f"Total income amount is {totalincome}")
        elif compans == "2":
            print(f"Total expense amount is {totalexpense}")
        elif compans == "3":
            totalleftover = totalincome - totalexpense
            print(f"Total leftover is {totalleftover}")
        elif compans == "4":
            frontpage()
            break
        else:
            print()
            print("You have not entered a valid answer, please try again.")

#Introduction
print("     Welcome to Your Finances!")
print("    Please enter your full name")
print()

#Recieve user details
name = input("Your Name: ")
name = name.title()
print()
print(f"Hello {name}, Nice to meet you!")

#runs the functions that Checks user is above 18 and agrees with terms and conditions of the app
agecheck()
termscheck()

#front page of program, starts the main program which interconnects all functions.
frontpage()
