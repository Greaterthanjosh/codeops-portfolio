# day07/main.py

import time
from collections import deque


# 1. Big-O Examples


# List index access
# Big-O: O(1)
# Why: Python lists store elements in memory locations that can
# be accessed directly by index.

numbers = [10, 20, 30, 40]

print(numbers[2])


# Single loop
# Big-O: O(n)
# Why: The loop runs once for every item in the list.

for number in numbers:
    print(number)


# Nested loop
# Big-O: O(n²)
# Why: Each item is compared with every other item.

for i in numbers:
    for j in numbers:
        print(i, j)


# Dictionary lookup
# Big-O: O(1)
# Why: Dictionaries use hashing to find values directly.

accounts = {
    "1001": "Eyasu",
    "1002": "Almaz"
}

print(accounts["1001"])


# Binary search
# Big-O: O(log n)
# Why: Each step cuts the search area in half.



# 2. List vs Dictionary Lookup Timing


account_numbers = []

account_dict = {}


for i in range(100000):

    account = f"ACC{i}"

    account_numbers.append(account)

    account_dict[account] = True



target = "ACC99999"


start = time.time()

target in account_numbers

list_time = time.time() - start



start = time.time()

target in account_dict

dict_time = time.time() - start



print("\nLookup Performance")

print(
    "List lookup:",
    list_time
)

print(
    "Dictionary lookup:",
    dict_time
)



# 3. Stack Implementation


class Stack:

    def __init__(self):

        self.items = []


    def push(self, item):

        self.items.append(item)


    def pop(self):

        return self.items.pop()


    def peek(self):

        return self.items[-1]



print("\nStack Example")


names = [
    "Eyasu",
    "Almaz",
    "Dawit",
    "Sara"
]


stack = Stack()


for name in names:
    stack.push(name)



reversed_names = []


while stack.items:

    reversed_names.append(
        stack.pop()
    )


print(reversed_names)



# 4. Queue Using deque


print("\nBank Queue Example")


bank_queue = deque()


customers = [
    "Customer 1",
    "Customer 2",
    "Customer 3",
    "Customer 4",
    "Customer 5"
]


for customer in customers:

    bank_queue.append(customer)



while bank_queue:

    served = bank_queue.popleft()

    print(
        "Serving:",
        served
    )



# 5. Singly Linked List


class Node:

    def __init__(self, data):

        self.data = data
        self.next = None



class LinkedList:

    def __init__(self):

        self.head = None



    def push_front(self, data):

        new_node = Node(data)

        new_node.next = self.head

        self.head = new_node



    def print_all(self):

        current = self.head

        while current:

            print(current.data)

            current = current.next



print("\nLinked List Example")


linked_list = LinkedList()


linked_list.push_front("Account 1001")
linked_list.push_front("Account 1002")
linked_list.push_front("Account 1003")


linked_list.print_all()