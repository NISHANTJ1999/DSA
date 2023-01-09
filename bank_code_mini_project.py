class Customer:
    """ Bank project developed by Nishant"""
    Bank_name = "Nagpur Corporate Pvt.Ltd"

    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Your account has been credited with {amount} and "
              f"available balance is {self.balance}")

    def withdrawn(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance = self.balance - amount
            print(f" {amount}  has been debited from your bank account"
                  f"your available balance is {self.balance}")



print("WELCOME TO", Customer.Bank_name)

name = input("enter your name:")
c = Customer(name)

while True:
    print("please select the options")
    print()
    print(" d- deposit \n w- withdrawn  \n e- exit")

    option = input("select option: ")
    if option.lower() == 'd':
        amount = float(input("enter amount to be deposited : "))
        c.deposit(amount)

    elif option.lower() == 'w':
        amount = float(input("enter amount to be withdrawn : "))
        c.withdrawn(amount)

    elif option.lower() == 'e':
        print("Thanks for banking")
        break


    else:
        print("Invalid Input please select valid the option to proceed : ")








