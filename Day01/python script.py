class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def statement(self):
        print(f"{self.owner}: {self.balance} ETB")


Almaz = Account("Almaz", 1500)
Almaz.deposit(500)
Almaz.balance += 500
Almaz.statement()    
Almaz.withdraw(200)
Almaz.statement()