# cabin_class_description.py
def cabin_class_description():
    cabin_class = input("Enter the cabin class: ").upper()
    if cabin_class == "LUX":
        print("LUX: upper-deck cabin with a balcony.")
    elif cabin_class == "A":
        print("A: above the car deck, equipped with a window.")
    elif cabin_class == "B":
        print("B: windowless cabin above the car deck.")
    elif cabin_class == "C":
        print("C: windowless cabin below the car deck.")
    else:
        print("Invalid cabin class")

cabin_class_description()
