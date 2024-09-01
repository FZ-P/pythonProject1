# mass_conversion.py
def mass_conversion():
    talents = float(input("Enter talents: "))
    pounds = float(input("Enter pounds: "))
    lots = float(input("Enter lots: "))

    total_pounds = talents * 20 + pounds
    total_lots = total_pounds * 32 + lots
    grams = total_lots * 13.3

    kilograms = int(grams // 1000)
    grams = grams % 1000

    print(f"The weight in modern units: {kilograms} kilograms and {grams:.2f} grams.")

mass_conversion()
