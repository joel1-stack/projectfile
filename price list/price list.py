products = []

for i in range(5):
    name = input(f"Enter name of product {i+1}: ")
    price = input(f"Enter price of {name} (Ksh): ")
    products.append((name, price))

print("\n" + "-" * 45)
print(f"{'Product Name':<20} | {'Price':>10}")
print("-" * 45)

for product, price in products:
    print(f"{product:<20} | Ksh. {price}")
    print("-" * 45)


