# Class Exercise
# Create a BankAccount class with methods: deposit(), withdraw(), check_balance().

class BankAccount():
    def __init__(self,name,current_balance):
        self.current_balance=current_balance
        self.name=name
        self.transaction_history=[]
    def deposit(self,amount):
        new_balance=self.current_balance+amount
        print(f'Hi {self.name}!, Your current balance after deposit is ${new_balance:.2f}')
        self.current_balance =new_balance
        self.transaction_history.append(f"Deposited:{amount:.2f}")
    def withdraw(self,amount):
        if amount<=self.current_balance:
            new_balance=self.current_balance- amount
            print(f'Hi {self.name}!, Your current balance after withdraw is = ${new_balance:.2f} ')
            self.current_balance = new_balance
            self.transaction_history.append(f"withdraw:{amount:.2f}")
        else:
            print(f"Hi {self.name}!, You dont have sufficient balance, I cannot process your transaction")
    def check_balance(self):
        print(f'Hi {self.name}!, Your current balance is = ${self.current_balance:.2f}')
    def check_history(self):
        print(f"Hi {self.name}!, Your transaction history is {self.transaction_history}")


BA=BankAccount("Shweta",5000)
BA.check_balance()
BA.deposit(1000)
BA.check_balance()
BA.withdraw(100000)
BA.withdraw(100)
BA.check_balance()
BA.check_history()
