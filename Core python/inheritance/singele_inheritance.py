class Account:

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, new balance is: {self.balance}")
    
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"withdraw {amount}, new balance is: {self.balance}")


class SavingAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest_amount(self):
        interest_amount = self.balance * self.interest_rate
        self.deposit(interest_amount)
        print(f"Interest of {interest_amount} added, new balance is {self.balance}")

saving = SavingAccount('VTU117', 1000, 0.08)
saving.deposit(500)
saving.add_interest_amount()        