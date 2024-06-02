class Account:
    def __init__(self,owner,number,pin):
        self.owner = owner
        self.number = number
        self.__pin = pin
        self.__balance = 0
        self.__transactions = []

    def check_balance(self,pin):
        if pin ==self.__pin:
            return self.__balance
        else:
            return "wrong pin entered"

    def deposit(self, amount):
        self.__balance += amount
        self.__transactions.append(f" Deposited: {amount}")
        print(f"Deposited {amount} your new balance is {self.__balance}")
        return self.__balance

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount
            self.__transactions.append(f"Withdrew {amount}.")
            print(f"Withdrew {amount} your new balance is {self.__balance}")
        
        return self.__balance
    

    def view_account_details(self):
        print(f"Account Owner: {self.owner}")
        print(f"Account Number: {self.number}")
        print(f"Account Pin: {self.__pin}")
        print(f"Current Balance: {self.__balance}")

    def change_account_owner(self, new_owner):
        self.owner = new_owner
        print(f"Account owner updated to {new_owner}")

    def account_statement(self):
        print(f"Account Statement:")
        print(f"Account Owner: {self.owner}")
        print(f"Current Balance: {self.__balance}")

    def set_overdraft_limit(self, limit):
        self.overdraft_limit = limit
        print(f"Overdraft limit set to {limit}")

    def interest_calculation(self, rate):
        interest = self.__balance * rate
        self.__balance += interest
        self.__transactions.append(f"Interest calculated: {interest}.")
        print(f"Interest calculated at {interest} your new balance is {self.__balance}")

    def freeze_account(self):
        self.frozen = True
        self.__transactions.append("Account frozen.")
        print("Account frozen.")

    def unfreeze_account(self):
        self.frozen = False
        self.__transactions.append("Account unfrozen.")
        print("Account unfrozen.")

    def transaction_history(self):
        return self.__transactions

    def set_minimum_balance(self, minimum):
        self.minimum_balance = minimum
        print(f"Minimum balance set to {minimum}")

    def transfer_funds(self, other_account, amount):
        if amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.withdraw(amount)
            other_account.deposit(amount)
            print(f"Transferred {amount} to {other_account.owner}")

    def close_account(self):
        print("Account closed.")