import math
# Function to calculate unit price of pizza per square meter
def unit_price(diameter, price):
    radius = diameter / 2
    area = math.pi * radius ** 2 / 10000  # Area in square meters
    return price / area


# Main program
def main():
    diameter1 = float(input("Enter the diameter of the first pizza (cm): "))
    price1 = float(input("Enter the price of the first pizza (euros): "))

    diameter2 = float(input("Enter the diameter of the second pizza (cm): "))
    price2 = float(input("Enter the price of the second pizza (euros): "))

    price_per_sqm1 = unit_price(diameter1, price1)
    price_per_sqm2 = unit_price(diameter2, price2)

    if price_per_sqm1 < price_per_sqm2:
        print("The first pizza offers better value for money.")
    else:
        print("The second pizza offers better value for money.")


# Call main function
if __name__ == "__main__":
    main()
