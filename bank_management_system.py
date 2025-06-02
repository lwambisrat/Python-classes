

#Create a new class Transaction to store all transactions with attributes for date and time, narration, amount, transaction type etc.
#The Account class should have a new attribute called transactions which will store every transaction that happens in the account
#Each transaction should be stored as an instance of the Transaction
#The get balance method should use the transactions list to compute the current balance
#Add encapsulation to the Account class to have sensitive attributes like balance and account number only accessible via given class methods. 
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




from datetime import datetime

class Transaction:
    def __init__(self, amount, narration, transaction_type):
        self.date_time = datetime.now()
        self.amount = amount
        self.narration = narration
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.date_time.strftime('%Y-%m-%d %H:%M:%S')} | {self.transaction_type} | {self.narration} | Amount: {self.amount}"

class Account:
    def __init__(self, owner, account_number, min_balance=0):
        self.owner = owner
        self.__account_number = account_number
        self.__transactions = []
        self.__min_balance = min_balance
        self.__is_frozen = False
        self.__loan = 0

    def account_number(self):
        return self.__account_number
    def transactions(self):
        return self.__transactions.copy()

    def deposit(self, amount, narration="Deposit"):
        if self.__is_frozen:
            return "Account is frozen. Cannot deposit."
        if amount <= 0:
            return "Deposit amount must be positive."
        self.__transactions.append(Transaction(amount, narration, "Deposit"))
        return f"Deposit successful. New balance: {self.get_balance()}"

    def withdraw(self, amount, narration="Withdrawal"):
        if self.__is_frozen:
            return "Account is frozen. Cannot withdraw."
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if self.get_balance() - amount < self.__min_balance:
            return "Insufficient funds or minimum balance requirement not met."
        self.__transactions.append(Transaction(-amount, narration, "Withdrawal"))
        return f"Withdrawal successful. New balance: {self.get_balance()}"

    def transfer(self, amount, target_account, narration="Transfer"):
        if self.__is_frozen:
            return "Account is frozen. Cannot transfer."
        if not isinstance(target_account, Account):
            return "Target must be an Account instance."
        if amount <= 0:
            return "Transfer amount must be positive."
        if self.get_balance() - amount < self.__min_balance:
            return "Insufficient funds or minimum balance requirement not met."
        self.__transactions.append(Transaction(-amount, narration, "Transfer Out"))
        target_account._Account__transactions.append(Transaction(amount, narration, "Transfer In"))
        return f"Transferred {amount} to {target_account.owner}. New balance: {self.get_balance()}"

    def get_balance(self):
        return sum(t.amount for t in self.__transactions) - self.__loan

    def request_loan(self, amount):
        if self.__is_frozen:
            return "Account is frozen. Cannot request loan."
        if amount <= 0:
            return "Loan amount must be positive."
        self.__loan += amount
        self.__transactions.append(Transaction(amount, "Loan granted", "Loan"))
        return f"Loan of {amount} approved. Outstanding loan: {self.__loan}"

    def repay_loan(self, amount):
        if self.__is_frozen:
            return "Account is frozen. Cannot repay loan."
        if amount <= 0:
            return "Repayment amount must be positive."
        if amount > self.__loan:
            return "Repayment exceeds outstanding loan."
        self.__loan -= amount
        self.__transactions.append(Transaction(-amount, "Loan repayment", "Loan Repayment"))
        return f"Loan repayment successful. Outstanding loan: {self.__loan}"

    def view_account_details(self):
        return {
            "Owner": self.owner,
            "Account Number": self.__account_number,
            "Current Balance": self.get_balance(),
            "Minimum Balance": self.__min_balance,
            "Loan Outstanding": self.__loan,
            "Status": "Frozen" if self.__is_frozen else "Active"
        }

    def change_account_owner(self, new_owner):
        self.owner = new_owner
        return f"Account owner changed to {new_owner}."

    def account_statement(self):
        print("Account Statement:")
        for txn in self.__transactions:
            print(txn)

    def apply_interest(self):
        if self.__is_frozen:
            return "Account is frozen. Cannot apply interest."
        interest = self.get_balance() * 0.05
        self.__transactions.append(Transaction(interest, "Interest applied", "Interest"))
        return f"Interest of {interest} applied. New balance: {self.get_balance()}"

    def freeze_account(self):
        self.__is_frozen = True
        return "Account frozen."

    def unfreeze_account(self):
        self.__is_frozen = False
        return "Account unfrozen."

    def set_minimum_balance(self, amount):
        if amount < 0:
            return "Minimum balance cannot be negative."
        self.__min_balance = amount
        return f"Minimum balance set to {amount}."

    def close_account(self):
        self.__transactions.clear()
        self.__loan = 0
        return "Account closed. All balances set to zero."
acc1 = Account("Lwam", "001")
acc2 = Account("Hewan", "002")
print(acc1.deposit(1000))
print(acc1.withdraw(200))
print(acc1.transfer(100, acc2))
acc1.account_statement()