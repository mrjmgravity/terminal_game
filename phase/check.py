import phase_constants


def end_game():
    print("Do u really want to quit the game?")
    while True:
        print("0 - Back to the game!")
        print("1 - Exit")
        user_input = int(input("What do u want? "))
        if user_input not in [0, 1]:
            continue

        if user_input == 0:
            return False
        elif user_input == 1:
            return True


def phase_check(next_phase):
    while True:
        print("0 - Continue to", next_phase)
        print("1 - Edit hero")
        print("2 - Save the game")
        print("3 - Exit")
        user_input = int(input("What is your choice? "))
        if user_input not in ["0", "1", "2", "3"]:
            print("Make sure you pick one of your choices")
            continue
        if user_input == 0:
            return next_phase
        elif user_input == 1:
            # TODO dorobit edit hrdinu
            continue
        elif user_input == 2:
            # TODO dorobit save game
            continue
        elif user_input == 3:
            if end_game():
                return phase_constants.END
