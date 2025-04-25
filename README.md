A simple yet powerful command-line application to track personal finances, including income, expenses, and financial analysis.

## Features
- Track Income: Record various types of income (Active, Portfolio, Passive, Other)
- Track Expenses: Record various types of expenses (Housing, Utilities, Food, Transport, Entertainment, Education, Health, Other)
- Data Persistence: All financial records stored in SQLite database
- Financial Analysis: View comparisons between income and expenses
- UK VAT Calculator: Calculate VAT amounts on purchases
- User Authentication: Basic age verification and terms acceptance
- Currency Support: Choose between £, $, €, or other currencies

## Installation
1. Make sure you have Python 3.x installed
2. No additional packages are required as this project uses only Python standard libraries

## Usage
Run the application by executing the main Python file:

python finance_tracker.py

Follow the interactive prompts to:
1. Enter your name
2. Complete age verification (must be 18+)
3. Accept terms and conditions
4. Choose your preferred currency
5. Navigate the menu to manage your finances

## Main Menu Options
1. Income Options
    - Add income (with date, type, and amount)
    - View recorded income
    - Delete income entries

2. Expense Options
    - Add expenses (with date, type, and amount)
    - View recorded expenses
    - Delete expense entries

3. VAT Calculator (UK)
    - Calculate VAT amounts on purchases

4. Financial Analysis
    - View total income and highest income amount
    - View total expenses and highest expense amount
    - Check your balance (income minus expenses)
    - Compare highest and lowest income/expenses

5. Exit
    - Safely exit the application

## Data Storage
The application automatically creates a data directory and stores all information in a SQLite database file (finance.db).
## Project Structure
- finance_tracker.py - Main application file
- data/finance.db - SQLite database (created on first run)

## Requirements
- Python 3.x
- SQLite (included in Python standard library)

