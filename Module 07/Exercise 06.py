import math


def unit_price(diameter_cm, price_eur):
    """
    Calculates the price per square meter of a round pizza.
    diameter_cm: diameter of the pizza in centimeters
    price_eur: price of the pizza in euros
    Returns: price per square meter (EUR/m^2)
    """
    radius_cm = diameter_cm / 2
    area_cm2 = math.pi * radius_cm ** 2
    area_m2 = area_cm2 / 10000  #  m^2 = 10 000 cm^2
    return price_eur / area_m2


# main program
print("Pizza 1:")
diameter1 = float(input("  Enter diameter (cm): "))
price1 = float(input("  Enter price (EUR): "))

print("Pizza 2:")
diameter2 = float(input("  Enter diameter (cm): "))
price2 = float(input("  Enter price (EUR): "))

price_per_m2_1 = unit_price(diameter1, price1)
price_per_m2_2 = unit_price(diameter2, price2)

print(f"\nPizza 1: {price_per_m2_1:.2f} EUR/m^2")
print(f"Pizza 2: {price_per_m2_2:.2f} EUR/m^2")

if price_per_m2_1 < price_per_m2_2:
    print("Pizza 1 is the better value for money.")
elif price_per_m2_2 < price_per_m2_1:
    print("Pizza 2 is the better value for money.")
else:
    print("Both pizzas have the same value for money.")