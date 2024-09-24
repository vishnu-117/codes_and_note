from singele_inheritance import Account


class LoanAccount:
    def __init__(self, loan_amount):
        self.loan_amount = loan_amount
    
    def repay_loan(self, amount):
        self.loan_amount -= amount
        print(f"Repaid {amount}, remaining loan is: {self.loan_amount}")


class BusinessAccount(Account, LoanAccount):
    def __init__(self, account_number, balance, loan_amount):
        Account.__init__(self, account_number, balance)
        LoanAccount.__init__(self, loan_amount)
    
    def display_status(self):
        print(f"Account: {self.account_number}, Balance: {self.balance}, Loan: {self.loan_amount}")


business = BusinessAccount("KKR", 100000, 10000)
business.deposit(100000)
business.repay_loan(50000)
business.display_status()