# zander_size_check.py
def zander_size_check():
    length = float(input("Enter the length of the zander in centimeters: "))
    if length < 42:
        print(f"Release the fish. It is {42 - length:.2f} centimeters below the size limit.")
    else:
        print("The zander meets the size limit.")

zander_size_check()
