import random

class Dice(object):
    
    def __init__(self):    
        self.dices = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}

    # roll(dice to roll)        
    def roll(self, dice_to_roll):
        self.dices[dice_to_roll] = random.randint(1,6)
        
        for dice in ['A', 'B', 'C', 'D', 'E']:
            print "Dice " + dice + ": " + str(self.dices[dice])
        print "-----------"

game_dice = Dice()
        
for i in range(0, 10):
    random_dice = random.choice(['A', 'B', 'C', 'D', 'E'])
    game_dice.roll(random_dice)
    
def dict_experiment(my_dict):
    print my_dict.values()
    
dict_experiment(game_dice.dices)