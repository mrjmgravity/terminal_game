def main():
    intro()


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


main()
