def set_nickname():
    while True:
        hero_name = input("Choose nickname for your hero: ")
        print("Accept the nickname or edit:\n")
        print("0 - Edit nickname\n1 - Accept nickname\n")
        choice = input()
        if choice == "0":
            continue
        elif choice == "1":
            print(f"Hello {hero_name}!")
            return hero_name
        else:
            print("Wrong choice")
        return None