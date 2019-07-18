import time
# import the time module
import random
# import the random module for random dice roll

from wizard_actors import Wizard, Creature, SmallAnimal, Dragon
# impart wizard_actors with each item that used in the game program

def main():
    print_header()
    game_loop()



def print_header(): # print the header

    print('----------------------------------')
    print('     Wizard Battle App     ')
    print('----------------------------------')


def game_loop(): # create the game function (main game)

# list all creatures
    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 75, True),
        Wizard('Evil Wizard', 100)
    ]

    #print(creatures)

    hero = Wizard('Gandolf', 75)

    while True:

        active_creature = random.choice(creatures) # randomly chooses the opponent from the creatures list
        print('A {} of level {} has appear from a dark and foggy forest...'
              .format(active_creature.name, active_creature.level))
        print()

        cmd = input('Do you [a]ttack, [r]unaway, [l]ook around, or [q]uit : ') # ask the user what he/she want to do
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard runs and hides taking time to recover...")
                time.sleep(5)
                print("The wizard returns revitalized!")
        elif cmd == 'r':
            print('The wizard has become unsure of his power and flees!')
        elif cmd == 'l':
            print('The wizard {} takes in the surroundings and sees:'
                  .format(hero.name))
            for c in creatures:
                print(' * A {} of level {}'.format(c.name, c.level))
        elif cmd =='q':
            print('Okay, exiting... See You Next Time!')
            raise SystemExit  # force quits the program

        if not creatures:
            print("Congratulation！！ You've defeated all the creature. Excellent job!!!")
            break

        print()


if __name__ == '__main__':
    main()
