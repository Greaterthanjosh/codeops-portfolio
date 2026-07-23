class BankConfig:

    _instance = None

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super().__new__(cls)

            cls._instance.interest_rate = 0.05
            cls._instance.overdraft_limit = 1000

        return cls._instance



class Account:

    def __init__(self, owner, number, balance=0):

        self.owner = owner
        self.account_number = number
        self.__balance = balance
        self.observers = []


    @property
    def balance(self):
        return self.__balance


    def subscribe(self, observer):
        self.observers.append(observer)


    def _notify(self, message):

        for observer in self.observers:
            observer.update(message)



    def deposit(self, amount):

        if amount <= 0:
            raise ValueError("Amount must be positive")

        self.__balance += amount

        self._notify(
            f"{self.owner} deposited {amount} ETB"
        )



    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self.__balance:
            raise ValueError("Insufficient funds")

        self.__balance -= amount

        self._notify(
            f"{self.owner} withdrew {amount} ETB"
        )


    def statement(self):

        print("\n----- Account Statement -----")
        print(f"Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance:.2f} ETB")



class SavingsAccount(Account):

    def __init__(self, owner, number, balance=0):

        super().__init__(owner, number, balance)

        self.config = BankConfig()


    def add_interest(self):

        interest = self.balance * self.config.interest_rate

        self.deposit(interest)



    def statement(self):

        print("\n----- Savings Account -----")
        print(f"Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance:.2f} ETB")
        print(
            f"Interest Rate: {self.config.interest_rate * 100}%"
        )



class CurrentAccount(Account):

    def __init__(self, owner, number, balance=0):

        super().__init__(owner, number, balance)

        self.config = BankConfig()



    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Amount must be positive")


        if amount > self.balance + self.config.overdraft_limit:
            raise ValueError(
                "Overdraft limit exceeded"
            )


        self.deposit(-amount)


    def statement(self):

        print("\n----- Current Account -----")
        print(f"Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance:.2f} ETB")
        print(
            f"Overdraft Limit: {self.config.overdraft_limit} ETB"
        )



# Factory Pattern

class AccountFactory:


    @staticmethod
    def create(kind, owner, number, balance=0):

        if kind == "savings":

            return SavingsAccount(
                owner,
                number,
                balance
            )


        elif kind == "current":

            return CurrentAccount(
                owner,
                number,
                balance
            )


        else:

            raise ValueError(
                "Unknown account type"
            )



# Observer Pattern

class SMSAlert:

    def update(self, message):

        print(
            f"SMS ALERT: {message}"
        )



class AuditLog:

    def update(self, message):

        print(
            f"AUDIT LOG: {message}"
        )



# Testing


if __name__ == "__main__":


    savings = AccountFactory.create(
        "savings",
        "Almaz Bekele",
        "200001",
        8000
    )


    current = AccountFactory.create(
        "current",
        "Dawit Alemu",
        "300001",
        2000
    )


    sms = SMSAlert()
    audit = AuditLog()


    savings.subscribe(sms)
    savings.subscribe(audit)

    current.subscribe(sms)
    current.subscribe(audit)



    savings.add_interest()


    current.withdraw(3000)



    accounts = [
        savings,
        current
    ]


    print("\n===== Addis Bank Account Family =====")


    for acc in accounts:
        acc.statement()



    config1 = BankConfig()
    config2 = BankConfig()


    print(
        "\nSame Config:",
        config1 is config2
    )