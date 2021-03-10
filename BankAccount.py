
# New BankAccount Class

class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

# Deposit Method - note, I add self to balance because I am getting it from 'BankAccount

    def deposit(self, amount):
        self.balance += amount # the specific users account increases by the amount of the value recieved
        return self

# Withdraw Method - note, I add self to balance because I am getting it from 'BankAccount
    def withdraw(self, amount):
        if  amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance -5
        else:
            self.balance -= amount # the # the specific users account decreases by the amount withdrawn
        return self

# Display Method - note, I add self to balance because I am getting it from 'BankAccount
        
    def display_account_info(self):
        print("Balance: "+  str(self.balance))
        return self

# Yield_Interest Method - note, I add self to balance because I am getting it from 'BankAccount
        
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * self.int_rate
        return self
      
# New Instances of the 'BankAccount' class
harper = BankAccount(0.01, 5000) # New user added
berkleigh =  BankAccount(0.01, 2000) # New user added



# Make a deposit for 'Harper' using 'make deposit' method and a withdrawl
harper.deposit(100).deposit(200).deposit(50).withdraw(25).yield_interest().display_account_info()


# Make a deposit for 'Berkleigh' using 'make deposit' method and a withdrawl
berkleigh.deposit(100).deposit(200).withdraw(250).withdraw(250).withdraw(25).withdraw(50).yield_interest().display_account_info()