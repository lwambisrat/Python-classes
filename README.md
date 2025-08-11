# Bank Account Management System

This project implements Bank Account Management System in Python with two main classes: Account and Transaction. The system demonstrates core banking functionalities such as deposits, withdrawals, transfers, loan management, interest calculation, account freezing, enforcing minimum balances, and generating account statements. The code is designed with strong encapsulation to protect sensitive data such as account numbers and balances.


# Table of content

- Installation

- Usage

- Features

- Technologies


# Installation

- clone the repository    = git clone git@github.com:lwambisrat/Python-classes.git
- display the repository   =cd Python-classes
-create file               =touch bank_management_system.py
- finally type              =code .

# Features

- Transaction Tracking:  

  Every account activity (deposit, withdrawal, transfer, loan, interest, etc.) is stored as a `Transaction` instance with details such as date, time, narration, amount, and transaction type.

- Encapsulation:

  Sensitive account attributes like account number and balance are private. They are only accessible or modifiable via class methods.

- Deposit:
  
  Add funds to the account. Only positive amounts are accepted. Each deposit is recorded as a transaction.

- Withdraw:
  
  Withdraw funds, ensuring the account is not overdrawn and the minimum balance is maintained. Each withdrawal is recorded as a transaction.

- Transfer Funds:
  
  Transfer money from one account to another, with proper transaction records for both accounts.

- Loan Management:
    
  Request and repay loans. Outstanding loan balances are tracked and included in balance calculations.

- Interest Calculation:
    
  Apply a 5% interest to the account balance, recorded as a transaction.

- Freeze/Unfreeze Account:
  
  Temporarily block all activities on the account for security reasons.

- Minimum Balance Enforcement:
    
  Set a minimum required balance. Withdrawals are denied if they would drop the account below this threshold.

- Account Statement:  

  Generate a detailed printout of all transactions.

- Account Management:
   
  View account details, change the account owner, and close the account (resetting all balances and clearing transactions).

  # Usage
  
- open vs code

- open new terminal and type python3

- from bank_account import Account

- create new object from Account class a1 = Account("Lwam", "123456789")

- create another object from Account class a2 = Account("Hewan", "987654321")

- Then run the code

- print(a1.deposit(500))                # Deposit funds

- print(a1.withdraw(100))               # Withdraw funds

- print(a1.transfer_funds(200, a2))     # Transfer funds to Hewan

- a1.account_statement()                # Print Lwam's account statement

- print(a1.calculate_interest())        # Apply interest

- print(a1.freeze_account())            # Freeze Lwam's account

- print(a1.deposit(50))                 # Attempt deposit while frozen (should fail)

- print(a1.unfreeze_account())          # Unfreeze account

- print(a1.deposit(50))                 # Deposit after unfreezing

- print(a1.set_minimum_balance(100))    # Set minimum balance

- print(a1.withdraw(400))               # Attempt withdrawal violating minimum balance (should fail)

- print(a1.close_account())             # Close account and clear all transactions

- a1.account_statement()                # Print account statement after closing


# Tchnologies
- python3
