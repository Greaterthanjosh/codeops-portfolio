# day08/registry.py


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

        # Transaction stack
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

            print("No transaction available")

            return


        transaction = self.history.pop()


        if transaction["type"] == "deposit":

            self.__balance -= transaction["amount"]


        elif transaction["type"] == "withdraw":

            self.__balance += transaction["amount"]



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

        if amount <= 0:

            raise ValueError(
                "Amount must be positive"
            )


        if amount > self.balance + self.config.overdraft_limit:

            raise ValueError(
                "Overdraft limit exceeded"
            )


        self._Account__balance -= amount


        self.history.append(
            {
                "type": "withdraw",
                "amount": amount
            }
        )


        self._notify(
            f"{self.owner} withdrew {amount} ETB"
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

        # O(1) lookup
        self.by_number = {}

        # insertion order
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



    # Day 8 addition 1
    # Balance leaderboard

    def top_by_balance(self, n=5):

        accounts = sorted(
            self.by_number.values(),
            key=lambda a: a.balance,
            reverse=True
        )

        return accounts[:n]



    # Day 8 addition 2
    # Binary Search

    def binary_search(self, items, target):

        left = 0

        right = len(items) - 1


        while left <= right:

            middle = (left + right) // 2


            if items[middle] == target:

                return middle


            elif items[middle] < target:

                left = middle + 1


            else:

                right = middle - 1


        return -1



    def find_by_number(self, number):

        sorted_numbers = sorted(
            self.by_number.keys()
        )


        index = self.binary_search(
            sorted_numbers,
            number
        )


        if index == -1:

            return None


        return self.by_number[
            sorted_numbers[index]
        ]



    # Day 8 addition 3
    # Recursive transaction total

    def total_transactions(self, number):

        account = self.find_by_number(number)


        if account is None:

            return 0



        def recursive_sum(history):

            if len(history) == 0:

                return 0


            return (
                history[0]["amount"]
                +
                recursive_sum(history[1:])
            )


        return recursive_sum(
            account.history
        )





class SMSAlert:

    def update(self, message):

        print(
            "SMS ALERT:",
            message
        )





class AuditLog:

    def update(self, message):

        print(
            "AUDIT LOG:",
            message
        )





# Testing


if __name__ == "__main__":


    registry = AccountRegistry()



    acc1 = AccountFactory.create(
        "savings",
        "Eyasu",
        "1003",
        5000
    )


    acc2 = AccountFactory.create(
        "current",
        "Almaz",
        "1001",
        12000
    )


    acc3 = AccountFactory.create(
        "savings",
        "Dawit",
        "1002",
        8000
    )



    registry.add(acc1)
    registry.add(acc2)
    registry.add(acc3)



    acc1.deposit(1000)
    acc1.withdraw(500)

    acc2.deposit(2000)

    acc3.withdraw(1000)



    print("\n===== TOP BALANCES =====")


    for account in registry.top_by_balance(2):

        print(
            account.owner,
            account.balance
        )



    print("\n===== BINARY SEARCH =====")


    result = registry.find_by_number(
        "1002"
    )


    if result:

        print(
            result.owner,
            result.balance
        )



    print("\n===== TRANSACTION TOTAL =====")


    print(
        registry.total_transactions("1003")
    )