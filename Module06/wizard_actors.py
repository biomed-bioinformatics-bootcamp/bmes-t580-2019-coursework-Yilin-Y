import random
# imports the random module for random dice roll



class Creature: # create the Creature class
    def __init__(self, name, the_level): # takes in self, name , and its level of the creature
        #leve
        self.name = name # obtain the name of the object
        self.level = the_level # obtain the level of the object

    def __repr__(self):
        return "Creature {} of level {}". format(
            self.name, self.level
        )

    def get_defensive_roll(self):
        return random.randint(1,12)* self.level



class Wizard(Creature): # import the wizard in the Creature class
    # def __init__(self,name,level):
        # self.name = name
        # self.level = level

    def attack(self,creature):
        print('The wizard {} attacks {}'.format(
            self.name,creature.level
        ))

        my_roll = self.get_defensive_roll()
        # creature_roll = random.randint(1,12)* creature.level
        creature_roll = creature.get_defensive_roll()

        print('You roll {}...'.format(my_roll))
        print('{} rolls {}...'.format(creature.name,creature_roll))

        if my_roll >= creature_roll:
            print('The wizard has handily triumphed over {}'.format(creature.name))
            return True
        else:
            print('The wizard has been DEFEATED !')
            return False

class SmallAnimal(Creature): # import the small animal in the Creature class
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2


class Dragon(Creature): # import the Dragon in the Creature class
    def __init__(self, name, level, scaliness, breaths_fire): # takes in self, name, scaliness and its level of the creature
        super().__init__(name,level)
        self.breaths_fire = breaths_fire
        self.scaliness = scaliness

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        # fire_modifier = VALUE_IF_TURE if SOME_TEST else VALUE_IF_FALSE
        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifire = self.scaliness / 10
        return base_roll * fire_modifier * scale_modifire
