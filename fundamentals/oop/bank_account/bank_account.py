class BankAccount:  # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self

    def withdraw(self, amount):
        # your code here
        self.balance -= amount
        return self

    def display_account_info(self):
        # your code here
        print("Balance: ${0}".format(self.balance))
        return self

    def yield_interest(self):
        # your code here
        self.balance += (self.int_rate * self.balance)
        return self

    def __repr__(self):
        return "Interest: {0}, Balance: {1}.".format(self.int_rate, self.balance)

june = BankAccount(0.05,0)
guido = BankAccount(0.01,0)
june.deposit(300).deposit(500).deposit(1000).withdraw(100).yield_interest().display_account_info()
guido.deposit(1000).deposit(2000).withdraw(500).withdraw(300).withdraw(100).withdraw(50).yield_interest().display_account_info()
print(june)