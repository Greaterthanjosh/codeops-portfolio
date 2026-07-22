customers = [
    ("Almaz", 1500),
    ("Dawit", 700),
    ("Tigist", 200),
    ("Hanna", 1200),
    ("Samuel", 450)
]


def tier(balance):
    if balance >= 1000:
        return "Premium"
    elif balance >= 500:
        return "Standard"
    else:
        return "Basic"


premium = 0
standard = 0
basic = 0


for name, balance in customers:

    customer_tier = tier(balance)

    print(f"{name}: {customer_tier} ({balance} ETB)")

    if customer_tier == "Premium":
        premium += 1
    elif customer_tier == "Standard":
        standard += 1
    else:
        basic += 1


print("\nSummary")
print("Premium:", premium)
print("Standard:", standard)
print("Basic:", basic)