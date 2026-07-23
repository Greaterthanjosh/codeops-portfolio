class Account:
    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.account_number = number
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self.__balance:
            raise ValueError("Insufficient funds")

        self.__balance -= amount

    def statement(self):
        print("\n------ Addis Bank Account Statement ------")
        print(f"Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.__balance} ETB")
        print("------------------------------------------")


# Test the program

account1 = Account("Eyasu Yebeltal", "100001", 5000)

account1.statement()

print("\nDepositing 1500 ETB...")
account1.deposit(1500)
account1.statement()

print("\nWithdrawing 2000 ETB...")
account1.withdraw(2000)
account1.statement()

print("\nAttempting to withdraw 10000 ETB...")

try:
    account1.withdraw(10000)
except ValueError as e:
    print("Error:", e)

print("\nAttempting to deposit -500 ETB...")

try:
    account1.deposit(-500)
except ValueError as e:
    print("Error:", e)