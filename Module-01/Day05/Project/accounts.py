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
        print("\n----- Account Statement -----")
        print(f"Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance:.2f} ETB")


class SavingsAccount(Account):
    def __init__(self, owner, number, balance=0, rate=0.05):
        super().__init__(owner, number, balance)
        self.rate = rate

    def add_interest(self):
        interest = self.balance * self.rate
        self.deposit(interest)

    def statement(self):
        print("\n----- Savings Account -----")
        print(f"Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance:.2f} ETB")
        print(f"Interest Rate: {self.rate * 100:.1f}%")


class CurrentAccount(Account):
    def __init__(self, owner, number, balance=0, overdraft=1000):
        super().__init__(owner, number, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self.balance + self.overdraft:
            raise ValueError("Overdraft limit exceeded")

        # Access the parent's private balance using deposit()
        self.deposit(-amount)

    def statement(self):
        print("\n----- Current Account -----")
        print(f"Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance:.2f} ETB")
        print(f"Overdraft Limit: {self.overdraft:.2f} ETB")


# Create accounts

account = Account("Eyasu Yebeltal", "100001", 5000)

savings = SavingsAccount(
    "Almaz Bekele",
    "200001",
    8000,
    0.08
)

current = CurrentAccount(
    "Dawit Alemu",
    "300001",
    2000,
    1500
)

# Savings account earns interest

savings.add_interest()

# Current account uses overdraft

try:
    current.withdraw(3000)
except ValueError as e:
    print(e)

# Polymorphism

accounts = [
    account,
    savings,
    current
]

print("\n===== Addis Bank Account Family =====")

for acc in accounts:
    acc.statement()