def main():
    intro()
    set_nickname()


def intro():
    print("Welcome in game Arcadius, you will battle with monsters. Are you ready?")
    print("0 - No ")
    print("1 - Im ready!\n")
    while True:
        try:
            user_input = int(input("What do you want to choose? "))
            if user_input == 0:
                print("Do u really want quit the game?\n")
                print("0 - Quit the game")
                print("1 - Lets continue!\n")
                quit_input = int(input("What do you want to choose? "))
                if quit_input == 0:
                    print("Goodbye")
                    break  # Ukončení programu
            elif user_input == 1:
                print("Welcome to the game!")
                break
            else:
                print("Wrong choose")
        except ValueError:
            print("Invalid answer")


def set_nickname():
    while True:
        hero_name = input("Choose nickname for your hero: ")
        print("Accept the nickname or edit:")
        print("0 - Edit nickname\n1 - Accept nickname\n")
        choice = input()
        if choice == "0":
            continue
        elif choice == "1":
            print(f"Hero name is {hero_name}")
            break
        else:
            print("Wrong choice")


main()
