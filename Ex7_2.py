def manage_names():
    names = set()

    while True:
        name = input("Enter a name (leave empty to stop): ")
        if name == "":
            break
        if name in names:
            print("Existing name")
        else:
            print("New name")
            names.add(name)

    print("\nNames entered:")
    for name in names:
        print(name)


manage_names()
