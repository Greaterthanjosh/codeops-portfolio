# day07/registry.py


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

        # Stack for transaction history
        self.history = []


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

            raise ValueError(
                "Amount must be positive"
            )


        self.__balance += amount


        self.history.append(
            {
                "type": "deposit",
                "amount": amount
            }
        )


        self._notify(
            f"{self.owner} deposited {amount} ETB"
        )



    def withdraw(self, amount):

        if amount <= 0:

            raise ValueError(
                "Amount must be positive"
            )


        if amount > self.__balance:

            raise ValueError(
                "Insufficient funds"
            )


        self.__balance -= amount


        self.history.append(
            {
                "type": "withdraw",
                "amount": amount
            }
        )


        self._notify(
            f"{self.owner} withdrew {amount} ETB"
        )



    def undo_last(self):

        if not self.history:

            print("No transactions to undo")
            return



        transaction = self.history.pop()


        if transaction["type"] == "deposit":

            self.__balance -= transaction["amount"]


        elif transaction["type"] == "withdraw":

            self.__balance += transaction["amount"]


        print(
            f"Undid {transaction['type']} of {transaction['amount']} ETB"
        )



    def statement(self):

        print("\n----- Account Statement -----")
        print(f"Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance:.2f} ETB")



class SavingsAccount(Account):

    def __init__(self, owner, number, balance=0):

        super().__init__(
            owner,
            number,
            balance
        )

        self.config = BankConfig()



    def add_interest(self):

        interest = (
            self.balance *
            self.config.interest_rate
        )

        self.deposit(interest)



class CurrentAccount(Account):

    def __init__(self, owner, number, balance=0):

        super().__init__(
            owner,
            number,
            balance
        )

        self.config = BankConfig()



    def withdraw(self, amount):

        if amount > self.balance + self.config.overdraft_limit:

            raise ValueError(
                "Overdraft exceeded"
            )


        self._Account__balance -= amount


        self.history.append(
            {
                "type": "withdraw",
                "amount": amount
            }
        )



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



class AccountRegistry:


    def __init__(self):

        self.by_number = {}

        self.order = []



    def add(self, acc):

        self.by_number[
            acc.account_number
        ] = acc


        self.order.append(
            acc.account_number
        )



    def find(self, number):

        return self.by_number.get(number)



    def list_all(self):

        return [
            self.by_number[number]
            for number in self.order
        ]



class SMSAlert:

    def update(self, message):

        print(
            "SMS:",
            message
        )



class AuditLog:

    def update(self, message):

        print(
            "AUDIT:",
            message
        )



if __name__ == "__main__":


    registry = AccountRegistry()



    acc1 = AccountFactory.create(
        "savings",
        "Eyasu",
        "1001",
        5000
    )


    acc2 = AccountFactory.create(
        "current",
        "Almaz",
        "1002",
        3000
    )



    registry.add(acc1)

    registry.add(acc2)



    acc1.deposit(1000)

    acc1.withdraw(500)



    print("\nCurrent balance:")

    print(
        acc1.balance
    )



    acc1.undo_last()



    print(
        "After undo:"
    )

    print(
        acc1.balance
    )



    print("\nFind account:")

    found = registry.find("1002")

    print(
        found.owner
    )



    print("\nAll accounts:")

    for account in registry.list_all():

        account.statement()