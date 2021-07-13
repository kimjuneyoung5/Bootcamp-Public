class User:		# here's what we have so far
    def __init__(self, name, email, accounts):
        self.name = name
        self.email = email
        self.account = BankAccount(accounts ='')
        print("New account is successfully created for {0} with account balance of {1}".format(self.name, self.account.balance))
    
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account.deposit(amount)	# the specific user's account increases by the amount of the value received
        return self

    # decrease the user's balance by the amount specified
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    # print the user's name and account balance 
    def display_user_balance(self):
        print("User: {0}, Balance: {1}".format(self.name, self.account.balance))
        self.account.display_account_info()
        return self
        
    # bonus: transfer money method
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self
        
class BankAccount:  # don't forget to add some default values for these parameters!
    def __init__(self, accounts, int_rate=0.01, balance=0): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance
        self.accounts = accounts

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

june = User("june", "june@gmail.com", "checking")
june = User("june", "june@gmail.com", "saving")