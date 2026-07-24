# Pharmacy Inventory Management

stock = {}

# Read stock from file
try:
    with open("stock.txt", "r") as file:
        for line in file:
            item, qty = line.strip().split(",")
            stock[item] = int(qty)

except FileNotFoundError:
    print("No stock file yet — starting empty")


# Function to adjust stock
def adjust(item, amount):
    stock[item] = stock.get(item, 0) + amount


# Example updates
adjust("Paracetamol", 5)
adjust("Amoxicillin", -3)
adjust("Vitamin C", 8)


# Print inventory
print("\nCurrent Inventory")
for item, qty in stock.items():
    print(f"{item}: {qty}")


# Low stock report
low_stock = [item for item, qty in stock.items() if qty < 10]

print("\nLow Stock Items")
if low_stock:
    for item in low_stock:
        print(item)
else:
    print("None")


# Save updated inventory
with open("stock.txt", "w") as file:
    for item, qty in stock.items():
        file.write(f"{item},{qty}\n")

print("\nInventory saved successfully.")