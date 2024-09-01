# hemoglobin_check.py
def hemoglobin_check():
    gender = input("Enter biological gender (male/female): ").lower()
    hemoglobin = float(input("Enter hemoglobin value (g/l): "))

    if gender == 'female':
        if 117 <= hemoglobin <= 155:
            print("Normal hemoglobin level.")
        elif hemoglobin < 117:
            print("Hemoglobin level is low.")
        else:
            print("Hemoglobin level is high.")
    elif gender == 'male':
        if 134 <= hemoglobin <= 167:
            print("Normal hemoglobin level.")
        elif hemoglobin < 134:
            print("Hemoglobin level is low.")
        else:
            print("Hemoglobin level is high.")
    else:
        print("Invalid gender.")

hemoglobin_check()
