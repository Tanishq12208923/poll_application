class Bank:
    '''This class denotes a Bank entity and all its related operations'''
    def __init__(self):
        self.all_accounts = {}
        
        ''' Example of `self.all_accounts` dictionary
        {
            "103": account_obj1
            "104": account_obj2
        }
        '''
        
    def get_account(self, acc_no):
        return self.all_accounts[acc_no]
    
    def add_account(self, account): # here `account` parameter is an Class Account's object
        self.all_accounts[account.acc_no] = account
    
    def del_account(self, acc_no):
        # deleting the account linked with the account_number
        del self.all_accounts[acc_no]

    
class Account:
    def __init__(self, acc_no, initial_balance):
        self.acc_no = acc_no # we can keep account number as string
        self.balance = initial_balance
        # print(f"Account Initiated - Acc_no: {acc_no}, Initial_Balance: {initial_balance}")
        print("Account Initiated - Acc_no: {}, Initial_Balance: {}".format(acc_no, initial_balance))
    
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient balance")
            return
        self.balance -= amount
        print(f'{amount} withdrawn. Current Balance: {self.balance}')
    
    def deposit(self, amount):
        self.balance += amount
        print(f'{amount} deposited. Current Balance: {self.balance}')
    
    
class Customer:
    def __init__(self, name):
        self.name = name
        self.my_accounts = {}
        
    def add_account(self, account): # here `account` parameter is an Class Account's object
        self.my_accounts[account.acc_no] = account
    
    def get_account(self, acc_no):
        return self.my_accounts[acc_no]
    



# Initialize the bank
my_bank = Bank()

# Create some accounts
account_1 = Account("123", 100)  # Account number "123" with initial balance of 100
account_2 = Account("456", 200)  # Account number "456" with initial balance of 200

# Add accounts to the bank
my_bank.add_account(account_1)
my_bank.add_account(account_2)

# Initialize a customer
customer_1 = Customer("Alice")

# Add accounts to the customer
customer_1.add_account(account_1)
customer_1.add_account(account_2)

# Perform some operations
account = my_bank.get_account("123")
if account:
    account.deposit(50)
    account.withdraw(30)

account = customer_1.get_account("456")
if account:
    account.deposit(100)
    account.withdraw(50)
