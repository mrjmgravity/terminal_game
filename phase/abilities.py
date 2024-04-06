def abilitiess(hero_name):
    abilities = {
        "Attack damage": {
            "points": 1,
        },
        "Defense": {
            "points": 1,
        },
        "Obratnost": {
            "points": 1,
        },
        "Skill": {
            "points": 1,
        },
        "Health": {
            "points": 50,
        },
        "Luck": {
            "points": 1,
        }
    }
    print(f"{hero_name}, These are your abilities:\n")
    for ability, details in abilities.items():
        print(f"{ability}: {details['points']} points")
    return abilities


def assign_points(abilities):
    dict_string = ""

    points_to_assign = 7
    while points_to_assign > 0:
        print(f"You have {points_to_assign} points left to assign.")
        print("What do you want to upgrade?")
        for index, (ability, details) in enumerate(abilities.items(), start=1):
            print(f"{index}. {ability}:")

        try:
            choice = int(input("Enter the number of the ability you want to upgrade: "))
            if 1 <= choice <= len(abilities):
                ability_name = list(abilities.keys())[choice - 1]
                abilities[ability_name]['points'] += 1
                if ability_name == "Health":
                    abilities[ability_name]['points'] += 5 - 1
                points_to_assign -= 1
                print(f"You've assigned a point to {ability_name}.\n")
            else:
                print("Invalid choice. Please choose a number corresponding to the ability.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")
    for ability, details in abilities.items():  # Toto prechadza dictionary a vpise aktualny pocet bodov
        dict_string += f"{ability}: {details['points']}\n"
    print(dict_string)
    print("You've assigned all your points.")
