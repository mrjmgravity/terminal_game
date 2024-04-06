import intro
import name
import abilities


def main():
    intro.intro()
    hero_name = name.set_nickname()
    abilities.abilitiess(hero_name)
    abilities.assign_points(abilities.abilitiess(hero_name))


main()
