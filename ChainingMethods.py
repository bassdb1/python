

# Creating a class and give it a user

class User:

# the first parameter of every method within a class is 'self'

    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
        
    #adding the deposit method
    #... The first parameter of 'every method' within a class
    #... should be 'self'
    def make_deposit(self,amount): # takes the 'amount' argument
        self.account_balance += amount # the specific users account increases by the amount of the value recieved

         # adding 'return self' so I can do 'Chaining Methods'
        return self

    #adding the 'make_withdrawl' method
    def make_withdrawl(self,amount):
        self.account_balance -= amount # the # the specific users account decreases by the amount withdrawn

         # adding 'return self' so I can do 'Chaining Methods'
        return self

    #adding the 'display user balance' method
    def display_user_balance(self):
        self.account_balance

# New Instances of the class 'User'
guido = User("Guido van Rossum", "guido@puthon.com") # New user added
monty = User("Monty Python", "monty@python.com") # New user added
david = User("David Bass", "dbass@yahoo.com")

# First User

# Make a deposit for Guido' using 'make deposit' method
guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(50)


print("Guido's account balance after deposit is: " + str(guido.account_balance))

#Make withdrawl using the 'make withdrawl' method
guido.make_withdrawl(200)

print("Guido's account balance after withdrawl is: " + str(guido.account_balance))

# Second User

# Make a deposit for Monty' using 'make deposit' method
monty.make_deposit(1000)
monty.make_deposit(2500)



print("Monty's account balance after deposit is: " + str(monty.account_balance))

#Make withdrawl using the 'make withdrawl' method
monty.make_withdrawl(2000)
monty.make_withdrawl(50)
print("Guido's account balance after withdrawl is: " + str(monty.account_balance))

# Third User

# Make a deposit for David' using 'make deposit' method
david.make_deposit(1000)

print("David's account balance after deposit is: " + str(david.account_balance))

#Make withdrawl using the 'make withdrawl' method
david.make_withdrawl(50).make_withdrawl(250).make_withdrawl(600)




print("David's account balance after withdrawl is: " + str(david.account_balance))
