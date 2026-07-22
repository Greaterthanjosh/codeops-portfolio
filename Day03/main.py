# Exercise 1

cities = [
    "Addis Ababa",
    "Hawassa",
    "Addis Ababa",
    "Mekelle",
    "Adama",
    "Hawassa",
    "Bahir Dar"
]

unique_cities = set(cities)

print("Exercise 1")
print("Unique Cities:", unique_cities)
print("Number of Unique Cities:", len(unique_cities))

# Exercise 2

prices = {
    "Bread": 55,
    "Milk": 90,
    "Sugar": 120,
    "Rice": 180,
    "Eggs": 220
}

print("\nExercise 2")

for item, price in prices.items():
    print(f"{item}: {price} ETB")

# Exercise 3 

prices = [100, 250, 400, 80]

prices_with_tax = [price * 1.15 for price in prices]

print("\nExercise 3")
print("Prices with 15% tax:", prices_with_tax)

# Exercise 4

cheap_prices = [price for price in prices if price < 200]

print("\nExercise 4")
print("Cheap prices:", cheap_prices)

# Exercise 5

with open("names.txt", "w") as file:
    file.write("Almaz\n")
    file.write("Dawit\n")
    file.write("Hanna\n")

print("\nExercise 5")

with open("names.txt", "r") as file:
    for name in file:
        print(name.strip())

# Exercise 6

print("\nExercise 6")

try:
    number = float(input("Enter a number: "))
    result = 1000 / number
    print("Result:", result)

except ValueError:
    print("Error: Please enter a valid number.")

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")