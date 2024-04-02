import sys
def main():
    intro()
    hero_name = set_nickname()
    abilitiess(hero_name)


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
                    sys.exit()
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
            print(f"Hello {hero_name}!")
            return hero_name
        else:
            print("Wrong choice")
        return None


def abilitiess(hero_name):
    abilities = {
        "Attack damage": {
            "points": 1,
            "description": "Sila je potrebna k útoku, do ktorého okrem sily vstupuje aj obratnosť a skill."
        },
        "Defense": {
            "points": 1,
            "description": "Celkový obrana sa ráta z bodov obrany + obratnosti."
        },
        "Ability Power": {
            "points": 1,
            "description": "Obratnosť je dôležitá aj pre obranu aj pre útok."
        },
        "Skill": {
            "points": 1,
            "description": "SKill je dôležitý pri normálnom útoku ako aj kritickom útoku"
        },
        "Health": {
            "points": 50,
            "description": "Život je dôležitý pri bitke. Život sa dá doplniť po každom súboji."
        },
        "Luck": {
            "points": 1,
            "description": "Šťastie je dôležité pre kritický útok"
        }
    }
    print(f"{hero_name}, These are your abilities:\n")
    for ability, details in abilities.items():
        print(f"{ability}: {details['points']} points")
    return abilities


main()
