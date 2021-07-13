from classes.ninja import Ninja, VampireNinja
from classes.pirate import Pirate

michelangelo = VampireNinja("Michelangelo")

jack_sparrow = Pirate("Jack Sparrow")

michelangelo.berserker_mode()
michelangelo.attack(jack_sparrow)
jack_sparrow.show_stats()
michelangelo.show_stats()

turn_indicator = 0

def action_choice(turn_indicator):
    if michelangelo.health <= 0:
        print("Jack Sparrow wins!")
    elif jack_sparrow.health <= 0:
        print("Michelangelo wins!")
    elif turn_indicator == 0: 
        print('What should the ninja do?')
        x = input('1: attack, 2: heal, 3: berserker_mode')
        turn_indicator = 1
        if x == 1:
            michelangelo.attack(jack_sparrow)
            jack_sparrow.show_stats()
        elif x == 2:
            michelangelo.heal()
            michelangelo.show_stats()
        elif x == 3:
            michelangelo.berserker_mode(jack_sparrow)
            michelangelo.show_stats()
        else:
            print('Enter a value from 1 to 3')
    
    pirate_action(turn_indicator)

def pirate_action(turn_indicator):
    if michelangelo.health <= 0:
        print("Jack Sparrow wins!")
    elif jack_sparrow.health <= 0:
        print("Michelangelo wins!")
    elif turn_indicator == 1: 
        print('What should the pirate do?/n')
        x = input('1: attack, 2: heal, 3: berserker_mode')
        turn_indicator = 0
        if x == 1:
            jack_sparrow.attack(michelangelo)
            michelangelo.show_stats()
            action_choice(turn_indicator)
        elif x == 2:
            jack_sparrow.heal()
            jack_sparrow.show_stats()
            action_choice(turn_indicator)
        elif x == 3:
            jack_sparrow.attack(michelangelo)
            jack_sparrow.show_stats()
            action_choice(turn_indicator)
        else:
            print('Enter a value from 1 to 3')
            action_choice(turn_indicator)

    pirate_action(turn_indicator)


action_choice(turn_indicator)