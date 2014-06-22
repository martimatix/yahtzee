import random
from collections import Counter
from sets import Set

# ScoreField class is the template class for all score fields.

class ScoreField(object):
    
    # Calculates the score for a given field
    def calculate(self, dice_values):
        print "Score field calculation unavaliable."
        
    # Mode of the dice. Mode in the statistical sense (mean, mode, median).    
    def modes(self, dice_values):
        
        # Utilise the Counter class
        data = Counter(dice_values)
        
        # Find the mode and modal frequency of the dice
        list_of_modal_tuples = data.most_common(2)
        
        #  returns a list of tuples where tuple[0] is the mode and tuple[1] is the modal frequency
        return list_of_modal_tuples
 
 # SingleFace() is for ones, twos, threes, fours, fives & sixes.
 # It takes in an argument at initialisation do determine which face to
 # evaluate.
 
class SingleFace(ScoreField):
    def __init__(self, face):
        self.num = face
        
    def calculate(self, dice_values):
        score = 0
        for dice_face in dice_values:
            if dice_face == self.num:
                score += self.num
        return score
    
class ThreeOfaKind(ScoreField):
    
    def calculate(self, dice_values):
        if self.modes(dice_values)[0][1] >= 3:
            return sum(dice_values)
        else:
            return 0

class FourOfaKind(ScoreField):
    
    def calculate(self, dice_values):
        if self.modes(dice_values)[0][1] >= 4:
            return sum(dice_values)
        else:
            return 0
    
class FullHouse(ScoreField):
    
    def calculate(self, dice_values):
        # check to see if there is a triple and a double
        if self.modes(dice_values)[0][1] == 3 and \
            self.modes(dice_values)[1][1] == 2:
            return 25
        # a yahtzee can also be a full house
        elif self.modes(dice_values)[0][1] == 5:
            return 25
        else:
            return 0
        
class SmallStraight(ScoreField):
    
# As there are only 3 ways that a small straight can be achieved, the checks
# are performed explicitly.
    
    def calculate(self, dice_values):
        
        dice = Set(dice_values)
        
        if Set([1, 2, 3, 4]).issubset(dice):
            return 30
        if Set([2, 3, 4, 5]).issubset(dice):
            return 30
        if Set([3, 4, 5, 6]).issubset(dice):
            return 30
        else:
            return 0
        
class LargeStraight(ScoreField):
    
# As there are only 2 ways that a large straight can be achieved, the checks
# are performed explicitly.
    
    def calculate(self, dice_values):
        
        dice = Set(dice_values)
        
        if Set([1, 2, 3, 4, 5]).issubset(dice):
            return 40
        if Set([2, 3, 4, 5, 6]).issubset(dice):
            return 40
        else:
            return 0
        
class Chance(ScoreField):

    def calculate(self, dice_values):
        return sum(dice_values)
    

# Yahtzee class also includes bonus calculations
    
class Yahtzee(ScoreField):
    
    def __init__(self):
        print "yahtzee score field class intialised"
        self.num_of_bonus_yahtzees = 0
        # yahtzee score in this class is purely for calculating yahtzee bonus
        # the displayed score is stored in the ScoreSheets classs
    
    def calculate(self, dice_values):
        
        if all(dice == dice_values[0] for dice in dice_values):
            # takes into account yahtzee bonus - 100 points for bonus yahtzees
            yahtzee_score = 50 + 100 * (self.num_of_bonus_yahtzees)
            self.num_of_bonus_yahtzees += 1
            return yahtzee_score
        else:
            return 0