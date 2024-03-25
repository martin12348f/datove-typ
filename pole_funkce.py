cars = ["Ford", "Volvo", "BMW", "audi"]

for x in range(len(cars)):
    print(f"Auto s cislem {x - 1}: {cars[x]}")

prvek_plus = input("zadej auto, ktere chcete odebrat")

print(" ")
cars.append(prvek_plus)

for x in range(len(cars)):
    print(f"Auto s cislem {x - 1}: {cars[x]}")
