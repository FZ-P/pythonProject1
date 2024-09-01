# inches_to_cm.py
def inches_to_cm():
    while True:
        inches = float(input("Enter inches (negative to quit): "))
        if inches < 0:
            break
        centimeters = inches * 2.54
        print(f"{inches} inches is {centimeters:.2f} centimeters.")

inches_to_cm()
