# Exercise 1

print("Exercise 1")


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def describe(self):
        print(f"'{self.title}' by {self.author} - {self.pages} pages")


book1 = Book("Atomic Habits", "James Clear", 320)
book2 = Book("Deep Work", "Cal Newport", 304)

book1.describe()
book2.describe()


# Exercise 2

print("\nExercise 2")


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def restock(self, n):
        self.quantity += n

    def sell(self, n):
        self.quantity -= n


product = Product("Paracetamol", 25, 100)

print("Before:", product.quantity)

product.sell(15)
print("After selling:", product.quantity)

product.restock(30)
print("After restocking:", product.quantity)


# Exercise 3

print("\nExercise 3")


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.__quantity = quantity

    @property
    def quantity(self):
        return self.__quantity

    def restock(self, n):
        self.__quantity += n

    def sell(self, n):
        self.__quantity -= n


product = Product("Ibuprofen", 40, 50)

print("Quantity:", product.quantity)

product.sell(10)

print("After selling:", product.quantity)


# Exercise 4

print("\nExercise 4")


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.__quantity = quantity

    @property
    def quantity(self):
        return self.__quantity

    def restock(self, n):
        self.__quantity += n

    def sell(self, n):
        if n > self.__quantity:
            print("Not enough stock available.")
        else:
            self.__quantity -= n


product = Product("Vitamin C", 120, 20)

product.sell(5)
print(product.quantity)

product.sell(30)
print(product.quantity)


# Exercise 5

print("\nExercise 5")


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.__quantity = quantity

    @property
    def quantity(self):
        return self.__quantity

    def restock(self, n):
        self.__quantity += n

    def sell(self, n):
        if n <= self.__quantity:
            self.__quantity -= n
        else:
            print(f"Cannot sell {n} units of {self.name}. Not enough stock.")


product1 = Product("Paracetamol", 25, 100)
product2 = Product("Ibuprofen", 40, 50)
product3 = Product("ORS", 15, 200)

product1.sell(20)

print(f"{product1.name}: {product1.quantity}")
print(f"{product2.name}: {product2.quantity}")
print(f"{product3.name}: {product3.quantity}")