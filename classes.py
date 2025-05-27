
# Deposit: method to deposit funds, store the deposit and return a message with the new balance to the customer. It should only accept positive amounts.
# Withdraw: method to withdraw funds, store the withdrawal and return a message with the new balance to the customer. An account cannot be overdrawn.
# Transfer Funds: Method to transfer funds from one account to an instance of another account.
# Get Balance: Method to calculate an account balance from deposits and withdrawals.
# Request Loan: Method to request a loan amount.
# Repay Loan: Method to repay a loan with a given amount.
# View Account Details: Method to display the account owner's details and current balance.
# Change Account Owner: Method to update the account owner's name.
# Account Statement: Method to generate a statement of all transactions in an account. (Print using a for loop).
# Interest Calculation: Method to calculate and apply an interest to the balance. Use 5% interest. 
# Freeze/Unfreeze Account: Methods to freeze and unfreeze the account for security reasons.
# Set Minimum Balance: Method to enforce a minimum balance requirement. You cannot withdraw if your balance is less than this amount.Close Account: Method to close the account and set all balances to zero and empty all transactions.


class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = [] 
        self.loan_balance = 0
        self.is_frozen = False
        self.min_balance = 0
    def deposit(self, amount):
        if self.is_frozen:
            return "Dear Customer your account is frozen.  Cannot perform deposits."
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +${amount}")
            return f"You have successfully deposited ${amount}.  Your current balance is: ${self.balance}.Thank you for banking with CBK."
        else:
            return "Invalid deposit amount. Amount must be positive."
    def withdraw(self, amount):
        if self.is_frozen:
            return "Dear Customer your account is frozen.  Cannot perform deposits."
        if amount > 0:
            if self.balance - amount >= self.min_balance:  
                self.balance -= amount
                self.transactions.append(f"Withdrawal: -${amount}")
                return f"You have successfully withdrawn ${amount} from your CBK account. Your current balance is : ${self.balance}"
            else:
                return "Your withdrawal request could not be processed. Insufficient funds in your account.Please check your available balance and try again."
        else:
            return "Invalid withdrawal amount. Amount must be positive."
    def transfer_funds(self, to_account, amount):
        if self.is_frozen:
            return "Dear Customer your account is frozen.  Cannot perform transfer."
        if amount > 0:
            if self.balance - amount >= self.min_balance:
                self.balance -= amount
                to_account.deposit(amount) 
                self.transactions.append(f"Transfer to {to_account.account_number}: -${amount}")
                return f"You have successfully transferred ${amount} to account number {to_account.account_holder}.Thank you for banking with CBK."
            else:
                return "Transfer amount exceeds minimum balance requirement."
        else:
            return "Invalid transfer amount. Amount must be positive."
    def get_balance(self):
        balance = 0
        for transaction in self.transactions:
            parts = transaction.split(":")
            transaction_type = parts[0].strip()  
            amount = float(amount_str.replace("$", "").replace("+", "").replace("-", ""))
            sign = -1 if "-" in amount_str else 1
            if transaction_type == "Deposit":
                balance += amount
            elif transaction_type == "Withdrawal" or "Transfer to":
                balance -= amount
        return balance + self.balance  
    def request_loan(self, amount):
        if self.is_frozen:
            return "Account is frozen. Cannot request a loan."
        if amount > 0:
            self.loan_balance += amount
            self.balance += amount  
            self.transactions.append(f"Loan Received: +${amount}")
            return f"Loan of ${amount} approved. New balance: ${self.balance}, Loan balance: ${self.loan_balance}"
        else:
            return "Invalid loan amount. Amount must be positive."
    def repay_loan(self, amount):
        if self.is_frozen:
            return "Account is frozen. Cannot repay loan."
        if amount > 0:
            if self.loan_balance >= amount:
                self.loan_balance -= amount
                self.balance -= amount
                self.transactions.append(f"Loan Repayment: -${amount}")
                return f"Repaid ${amount} of loan. Remaining loan balance: ${self.loan_balance}. New account balance: ${self.balance}"
            else:
                return "Repayment amount exceeds loan balance."
        else:
            return "Invalid repayment amount. Amount must be positive."
    def view_account_details(self):
        return f"Account Details: Account Number: {self.account_number}\n Account Holder: {self.account_holder}\n Current Balance: ${self.balance}\n Loan Balance: ${self.loan_balance}"
    def change_account_owner(self, new_owner):
        self.account_holder = new_owner
        return f"Account owner updated to {new_owner}"
    def account_statement(self):
        statement = "Account Statement:\n"
        for transaction in self.transactions:
            statement += transaction + "\n"
        return statement
    def calculate_interest(self):
        interest_rate = 0.05
        interest = self.balance * interest_rate
        self.balance += interest
        self.transactions.append(f"Interest Applied: +${interest:.2f}") # Limit to two decimal places
        return f"Interest of ${interest:.2f} applied. New balance: ${self.balance}"
    def freeze_account(self):
        if not self.is_frozen:
            self.is_frozen = True
            return "Your account has been frozen."
        else:
            return " Your account is already frozen."
    def unfreeze_account(self):
        if self.is_frozen:
            self.is_frozen = False
            return "Your account has been unfrozen."
        else:
            return "Your account is not frozen."
    def set_minimum_balance(self, min_balance):
        if min_balance >= 0:  
            self.min_balance = min_balance
            return f"Minimum balance set to ${min_balance}"
        else:
            return "Invalid minimum balance. Amount must be non-negative."
    def close_account(self):
        self.balance = 0
        self.loan_balance = 0
        self.transactions = []
        return "Account closed. All balances set to zero and transactions cleared."
    def __str__(self):
        return f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder}\nBalance: ${self.balance}\nLoan Balance: ${self.loan_balance}\nFrozen: {self.is_frozen}\nMin. Balance: ${self.min_balance}"
# 
account1 = BankAccount("12345", "Alice Smith", 1000)
account2 = BankAccount("67890", "Bob Johnson", 500)
print(account1.deposit(200))
print(account1.withdraw(100))
print(account1.transfer_funds(account2, 300))
print(account1.request_loan(500))
print(account1.repay_loan(200))
print(account1.view_account_details())
print(account1.change_account_owner("Alice Johnson"))
print(account1.account_statement())
print(account1.calculate_interest())
print(account1.freeze_account())
print(account1.unfreeze_account())
print(account1.set_minimum_balance(100)) # Set a $100 minimum balance
print(account1.withdraw(1050))  # Attempt to withdraw below the minimum
print(account1.close_account())
print(account1)  # Display the account details after closing