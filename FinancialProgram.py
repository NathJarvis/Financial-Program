#import packs
from datetime import datetime

#function defining
#Age Verifier
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
        print("You have not entered a valid age, please try again.")
        agecheck()

#T&C Verifier
def termscheck():
    print("Please read and agree to the terms and conditions of the app.")
    print("You can find them here: https://www.example.com/termsandconditions")
    print()
    agree = input("Do you agree to the terms and conditions? (Y/N) ")
    if agree.upper() == "Y":
        print()
        print("Thank you for agreeing to the terms and conditions!")
    else:
        print()
        print("You have not agreed to the terms and conditions, we can therefore not allow you to continue. Please try again later!")
        exit()

#Front Page function
def frontpage():
    print("What would you like to do today?")
    print()
    print("1. View your income Options")
    print()
    print("2. View your expenses Options")
    print()
    print("3  Work out VAT on an Item (UK only)")
    print()
    answer = int(input("Answer (1, 2 ,3): "))
    if answer == 1:
        incomeoptions()
    elif answer == 2:
        expenseoptions()
    elif answer == 3:
        VATUK()
    else:
        print()
        print("You have not entered a valid answer, please try again.")
        frontpage()

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

def incomecalc():
    global incomelist
    incomelist = []
    while True:
        addincome = input("Add an income, Press Y to conitnue or N to go back. ")
        if addincome.upper() == "Y":
            newincome = {}
            date = input("Enter the date of the income (dd-mm-yyyy): ")
            try:
                date = datetime.strptime(date, "%d-%m-%Y")
            except ValueError:
                print("You have not entered a valid date, please try again.")
                incomecalc()
            newincome["date"] = date.strftime("%d-%m-%Y")
            newincome["type"] = input("Enter the type of income: ")
            newincome["amount"] = input("Enter the amount of the income: ")
            incomelist.append(newincome)
            print(f"Income added successfully! This is your entry: {newincome}")
        elif addincome.upper() == "N":
            print("You have chosen not to add an income.")
            print(f"Here is your list of incomes: {incomelist}")
            frontpage()
            break
        else:
            print("You have not entered a valid input, please use Y or N.")

def viewincome():
    print(incomelist)
    incomeoptions()

def viewexpense():
    print(expenselist)
    expenseoptions()

def deleteincome():
    print("Please enter the date of the income you would like to delete.")
    deldate = input("Date dd-mm-yyyy: ")
    delinc = input("How much was the income for that you want to delete?")
    try:
        date = datetime.strptime(deldate, "%d-%m-%Y")
    except ValueError:
        print("You have not entered a valid date, please try again.")
        deleteincome()
    for newincome in incomelist:
        if newincome["date"] == deldate and newincome["amount"] == delinc:
            incomelist.remove(newincome)
            print(f"Income deleted successfully! This is your remaining Incomes: {incomelist}")
            break

def deleteexp():
    print("Please enter the date of the expense you would like to delete.")
    deldate = input("Date dd-mm-yyyy: ")
    delexp = input("How much was the income for that you want to delete?")
    try:
        date = datetime.strptime(deldate, "%d-%m-%Y")
    except ValueError:
        print("You have not entered a valid date, please try again.")
        deleteexp()
    for newexpense in expenselist:
        if newexpense["date"] == deldate and newexpense["amount"] == delexp:
            expenselist.remove(newexpense)
            print(f"Expense deleted successfully! This is your remaining Expenses: {expenselist}")
            break


def expensecalc():
    global expenselist
    expenselist = []
    while True:
        addexpense = input("would you like to add an expense? (Y/N) ")
        if addexpense.upper() == "Y":
            newexpense = {}
            date = input("Enter the date of the Expense (dd-mm-yyyy): ")
            try:
                date = datetime.strptime(date, "%d-%m-%Y")
            except ValueError:
                print("You have not entered a valid date, please try again.")
                incomecalc()
            newexpense["date"] = date.strftime("%d-%m-%Y")
            newexpense["type"] = input("Enter the type of expense: ")
            newexpense["amount"] = input("Enter the amount of the expense: ")
            expenselist.append(newexpense)
            print(f"Expense added successfully! This is your entry: {newexpense}")
        elif addexpense.upper() == "N":
            print("You have chosen not to add an expense.")
            print(f"Here is your list of expense: {expenselist}")
            frontpage()
            break
        else:
            print("You have not entered a valid input, please use Y or N.")

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


#Introduction
print("     Welcome to Your Finances!")
print("    Please enter your full name")
print()

#Recieve user details
name = input("Your Name: ")
name = name.title()
print()
print(f"Hello {name}, Nice to meet you!")

#Check user is above 18 and agrees with terms and conditions of the app
agecheck()
termscheck()

#front page of program
frontpage()




