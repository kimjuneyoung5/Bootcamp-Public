class BankAccount:  # don't forget to add some default values for these parameters!
    def __init__(self, accounts, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance
        self.account = accounts
        print("New bank account is made")


    def deposit(self, amount, account):
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

class User(BankAccount):		# here's what we have so far
    def __init__(self, name, email, accounts, int_rate, balance):
        self.name = name
        self.email = email
        BankAccount.__init__(self, accounts, int_rate, balance)
        print("New account is successfully created for {0} with account balance of {1}".format(self.account, self.balance))
    
    # adding the deposit method
    def make_deposit(self, amount , accounts):	# takes an argument that is the amount of the deposit
    	self.deposit(amount, accounts)
        print(self.balance)	# the specific user's account increases by the amount of the value received
        return self

    # decrease the user's balance by the amount specified
    def make_withdrawal(self, amount, account):
        self.withdraw(amount)
        print(self.account.balance)
        return self

    # print the user's name and account balance 
    def display_user_balance(self):
        print("User: {0}, Balance: {1}".format(self.name, self.balance))
        return self
        
    # bonus: transfer money method
    def transfer_money(self, account, other_user, other_acc, amount):
        self.make_withdrawal(amount, account)
        other_user.make_deposit(amount, other_acc)
        print(self.balance)
        return self


june = User("june", "june@gmail.com", "checking", 0.01, 0)
june = User("june", "june@gmail.com", "saving", 0.1, 0)
june.deposit(500,"checking")
june.display_account_info()