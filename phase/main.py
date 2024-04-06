import intro
import name
import abilities
import check
import phase.check


def main():
    intro.intro()
    hero_name = name.set_nickname()
    abilities.abilitiess(hero_name)
    abilities.assign_points(abilities.abilitiess(hero_name))
    phase.check.phase_check()


main()
