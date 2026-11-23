class BankAccount:
    def __init__(self,accountName, accountNumber, balance):
        self.accountName = accountName
        self.accountNumbber = accountNumber
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f" Account Holder: {self.accountName} ")
        print(f" Account Number: {self.accountNumbber}") 
        print(f" Deposit: ${amount} ")

    def get_balance(self):
        return self.balance


    def check_balance(self, amount):
        if amount <= self.balance:
            print("You have sufficient balance")
        else:
            print("sufficient balance")

            

b1 = BankAccount("Ghislaine", 400411305254 ,2000)


b1.deposit(2000)

print("New balance:", b1.get_balance())

b1.check_balance(5000)

    