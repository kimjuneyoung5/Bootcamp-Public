class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
        print("New account is successfully created for {0} with account balance of {1}".format(self.name, self.account_balance))
    
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received
        return self

    # decrease the user's balance by the amount specified
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    # print the user's name and account balance 
    def display_user_balance(self):
        print("User: {0}, Balance: {1}".format(self.name, self.account_balance))
        return self
        
    # bonus: transfer money method
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self



guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
june = User("June Young Kim", "june@python.com")
june.make_deposit(300).make_deposit(200).make_deposit(1000).make_withdrawal(500).display_user_balance()
guido.make_deposit(200).make_deposit(500).make_withdrawal(300).make_withdrawal(100).display_user_balance()
monty.make_deposit(100).make_withdrawal(10).make_withdrawal(10).display_user_balance()
june.transfer_money(monty, 200).display_user_balance()
monty.display_user_balance()