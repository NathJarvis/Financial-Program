#import packs
from datetime import datetime
import sqlite3
import os

currency = ""

#function defining
#Setup the database connection and create tables if they don't exist
def setup_database():
    # Check if database directory exists, if not create it
    if not os.path.exists('data'):
        os.makedirs('data')
    
    # Connect to the database (will create if it doesn't exist)
    conn = sqlite3.connect('data/finance.db')
    cursor = conn.cursor()
    
    # Create income table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS income (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        type TEXT NOT NULL,
        amount REAL NOT NULL
    )
    ''')
    
    # Create expense table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS expense (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        type TEXT NOT NULL,
        amount REAL NOT NULL
    )
    ''')
    
    # Commit changes and close connection
    conn.commit()
    conn.close()

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

'''Main Body of the add an income function, now saves income to the database'''
def incomecalc():
    while True:
        print()
        print("*-------------------------Add Income---------------------------*")
        print()
        addincome = input("Add an income, Press Y to continue or N to go back. ")
        print()
        if addincome.upper() == "Y":
            date = input("Enter the date of the income (dd/mm/yyyy): ")
            print()
            try:
                date = datetime.strptime(date, "%d/%m/%Y")
            except ValueError:
                print("You have not entered a valid date, please try again.")
                incomecalc()
            formatted_date = date.strftime("%d/%m/%Y")
            
            print("1. Active income (Wage, Salary, Benefits, etc.)")
            print("2. Portfolio income (Interest, Dividends, etc.)")
            print("3. Passive income (Investments, Rental, etc.)")
            print("4. Other income (Gifts, Savings, etc.)")
            print()
            newincometype= input("Please select from the list the type of income and insert the number: ")
            print()
            
            income_type = ""
            while True:
                if newincometype == "1":
                    income_type = "Active income"
                    break
                elif newincometype == "2":
                    income_type = "Portfolio income"
                    break
                elif newincometype == "3":
                    income_type = "Passive income"
                    break
                elif newincometype == "4":
                    income_type = "Other income"
                    break
                else:
                    print("You have not entered a valid number, please try again.")
                    print()
                    newincometype = input("Please select from the list the type of income and insert the number: ")
                    print()
            
            amount = input(f"Enter the amount of the income: {currency}")
            amount = float(amount)
            print()
            
            # Save to database
            conn = sqlite3.connect('data/finance.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO income (date, type, amount) VALUES (?, ?, ?)", 
                          (formatted_date, income_type, amount))
            conn.commit()
            conn.close()
            
            print(f"Income added successfully! This is your entry: {formatted_date}, {income_type}, {amount}")
        elif addincome.upper() == "N":
            print("You have chosen not to add an income.")
            incomeoptions()
            break
        else:
            print("You have not entered a valid input, please use Y or N.")
            print()

'''Main Body of the add an expense function, now saves expense to the database'''
def expensecalc():
    while True:
        print()
        print("*-------------------------Add Expense--------------------------*")
        print()
        addexpense = input("Add an Expense, Press Y to conitnue or N to go back. ")
        print()
        if addexpense.upper() == "Y":
            date = input("Enter the date of the Expense (dd/mm/yyyy): ")
            try:
                date = datetime.strptime(date, "%d/%m/%Y")
            except ValueError:
                print()
                print("You have not entered a valid date, please try again.")
                print()
                expensecalc()
            formatted_date = date.strftime("%d/%m/%Y")
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
            
            expense_type = ""
            while True:
                if newexpensetype == "1":
                    expense_type = "Housing expenses"
                    break
                elif newexpensetype == "2":
                    expense_type = "Utilities expenses"
                    break
                elif newexpensetype == "3":
                    expense_type = "Food expenses"
                    break
                elif newexpensetype == "4":
                    expense_type = "Transport expenses"
                    break
                elif newexpensetype == "5":
                    expense_type = "Entertainment expenses"
                    break
                elif newexpensetype == "6":
                    expense_type = "Education expenses"
                    break
                elif newexpensetype == "7":
                    expense_type = "Health expenses"
                    break
                elif newexpensetype == "8":
                    expense_type = "Other expenses"
                    break
                else:
                    print("You have not entered a valid number, please try again.")
                    print()
                    newexpensetype = input("Please select from the list the type of expense and insert the number: ")
                    print()
            
            amount = input(f"Enter the amount of the expense: {currency}")
            print()
            amount = float(amount)
            
            # Save to database
            conn = sqlite3.connect('data/finance.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO expense (date, type, amount) VALUES (?, ?, ?)", 
                          (formatted_date, expense_type, amount))
            conn.commit()
            conn.close()
            
            print(f"Expense added successfully! This is your entry: {formatted_date}, {expense_type}, {amount}")
        elif addexpense.upper() == "N":
            print("You have chosen not to add an expense.")
            expenseoptions()
            break
        else:
            print("You have not entered a valid input, please use Y or N.")

#View The list of incomes from database
def viewincome():
    print()
    print("*-------------------------View Income--------------------------*")
    print()
    
    # Connect to database and get all incomes
    conn = sqlite3.connect('data/finance.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM income")
    incomes = cursor.fetchall()
    conn.close()
    
    if not incomes:
        print("You have not added any incomes yet, please go back and add an income before trying again!")
    else:
        print("ID | Date | Type | Amount")
        print("-" * 50)
        for income in incomes:
            print(f"{income[0]} | {income[1]} | {income[2]} | {currency}{income[3]}")
    
    print()
    incomeoptions()

#View The list of expenses from database
def viewexpense():
    print()
    print("*-------------------------View Expense-------------------------*")
    print()
    
    # Connect to database and get all expenses
    conn = sqlite3.connect('data/finance.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expense")
    expenses = cursor.fetchall()
    conn.close()
    
    if not expenses:
        print("You have not added any expenses yet, please go back and add an expense before trying again!")
    else:
        print("ID | Date | Type | Amount")
        print("-" * 50)
        for expense in expenses:
            print(f"{expense[0]} | {expense[1]} | {expense[2]} | {currency}{expense[3]}")
    
    print()
    expenseoptions()

'''Delete an income function using database'''
def deleteincome():
    print()
    print("*-------------------------Delete income------------------------*")
    print()
    
    # Connect to database and get all incomes
    conn = sqlite3.connect('data/finance.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM income")
    incomes = cursor.fetchall()
    
    if not incomes:
        print("You have not added any incomes yet, please go back and add an income before trying again!")
        conn.close()
        incomeoptions()
        return
    
    print("Current incomes:")
    print("ID | Date | Type | Amount")
    print("-" * 50)
    for income in incomes:
        print(f"{income[0]} | {income[1]} | {income[2]} | {currency}{income[3]}")
    
    print()
    income_id = input("Enter the ID of the income you want to delete: ")
    try:
        income_id = int(income_id)
        
        # Check if the income exists
        cursor.execute("SELECT * FROM income WHERE id = ?", (income_id,))
        income = cursor.fetchone()
        
        if income:
            # Delete the income
            cursor.execute("DELETE FROM income WHERE id = ?", (income_id,))
            conn.commit()
            print(f"Income with ID {income_id} deleted successfully!")
        else:
            print(f"No income found with ID {income_id}")
    
    except ValueError:
        print("Please enter a valid numeric ID")
    
    conn.close()
    incomeoptions()

'''Delete an expense function using database'''
def deleteexp():
    print()
    print("*------------------------Delete Expense------------------------*")
    print()
    
    # Connect to database and get all expenses
    conn = sqlite3.connect('data/finance.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expense")
    expenses = cursor.fetchall()
    
    if not expenses:
        print("You have not added any expenses yet, please go back and add an expense before trying again!")
        conn.close()
        expenseoptions()
        return
    
    print("Current expenses:")
    print("ID | Date | Type | Amount")
    print("-" * 50)
    for expense in expenses:
        print(f"{expense[0]} | {expense[1]} | {expense[2]} | {currency}{expense[3]}")
    
    print()
    expense_id = input("Enter the ID of the expense you want to delete: ")
    try:
        expense_id = int(expense_id)
        
        # Check if the expense exists
        cursor.execute("SELECT * FROM expense WHERE id = ?", (expense_id,))
        expense = cursor.fetchone()
        
        if expense:
            # Delete the expense
            cursor.execute("DELETE FROM expense WHERE id = ?", (expense_id,))
            conn.commit()
            print(f"Expense with ID {expense_id} deleted successfully!")
        else:
            print(f"No expense found with ID {expense_id}")
    
    except ValueError:
        print("Please enter a valid numeric ID")
    
    conn.close()
    expenseoptions()

'''VAT Calculator function'''
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
            print("Example: 10.00 or 9.99 or 0.50")
    vatamount = amountb4vat - amountaftervat
    print()
    print("Calculating VAT on an Item (UK only)...")
    print()
    print(f"The amount of VAT is £{vatamount}")
    print(f"The total amount of the item is £{amountaftervat + vatamount}")
    frontpage()

#Comparisons function
def comparisons():
    print()
    print("*----------------------View Comparisons-----------------------*")
    print()
    
    # Connect to database
    conn = sqlite3.connect('data/finance.db')
    cursor = conn.cursor()
    
    # Check if there are any incomes and expenses
    cursor.execute("SELECT COUNT(*) FROM income")
    income_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM expense")
    expense_count = cursor.fetchone()[0]
    
    if income_count == 0 or expense_count == 0:
        print("You need to add both an income and expense to select this option, please go back and add both before trying again!")
        conn.close()
        frontpage()
        return
    
    # Get highest and lowest values
    cursor.execute("SELECT MAX(amount) FROM income")
    highestincome = cursor.fetchone()[0]
    
    cursor.execute("SELECT MAX(amount) FROM expense")
    highestexpense = cursor.fetchone()[0]
    
    cursor.execute("SELECT MIN(amount) FROM income")
    lowestincome = cursor.fetchone()[0]
    
    cursor.execute("SELECT MIN(amount) FROM expense")
    lowestexpense = cursor.fetchone()[0]
    
    # Get total amounts
    cursor.execute("SELECT SUM(amount) FROM income")
    totalincome = cursor.fetchone()[0]
    
    cursor.execute("SELECT SUM(amount) FROM expense")
    totalexpense = cursor.fetchone()[0]
    
    totalleftover = totalincome - totalexpense
    
    conn.close()
    
    while True:
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
        compans = input("What would you like to do? (1, 2, 3, 4, 5): ")
        print()
        if compans == "1":
            print(f"Total income amount is {currency}{totalincome}")
            print(f"Highest income amount is {currency}{highestincome}")
            print()
        elif compans == "2":
            print(f"Total expense amount is {currency}{totalexpense}")
            print(f"Highest expense amount is {currency}{highestexpense}")
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

# Setup the database first
setup_database()

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
