# Exercise 1
temperature = float(input("Enter temperature in °C: "))

if temperature < 15:
    print("cold")
elif temperature <= 28:
    print("warm")
else:
    print("hot")


# Exercise 2
for receipt in range(1, 11):
    print(f"Receipt #{receipt}")


# Exercise 3
for number in range(1, 21):
    if number % 2 == 0:
        print(number)


# Exercise 4
def apply_discount(price, percent=10):
    discount = price * percent / 100
    return price - discount


# Exercise 5
count = 5

while count > 0:
    print(count)
    count -= 1

print("Liftoff!")