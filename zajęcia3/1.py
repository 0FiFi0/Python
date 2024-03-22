products = set((input("Podaj produkty: ").lower()).split(","))
print(products)

product_prices = dict()

for element in products:
    price = float(input(f"Podaj cenę dla {element}: "))
    product_prices[element] = price

print(product_prices)
