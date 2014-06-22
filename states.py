import random
from score_sheet import *
from score_fields import *
from sets import Set
    
class Dice(object):
    
    def __init__(self):    
        self.dices = {'a': 1, 'r': 2, 's': 3, 't': 4, 'd': 5}
        self.key_order = ['a', 'r', 's', 't', 'd']
        
    # Rolls all the dice
    def roll_all(self):
        for dice_name in self.dices.iterkeys():
            self.dices[dice_name] = random.randint(1,6)

    # Rolls ones of the dice: A, B, C, D or E.       
    def roll(self, dice_to_roll):
        self.dices[dice_to_roll] = random.randint(1,6)
        
    # Prints dice roll result
    def display_dice(self):

        print '\n' + '-' * 80
        print "\tDice\t\tA\tR\tS\tT\tD"
        display_string = "\tValue\t"
        # Had to create a for-loop in this way because dictionaries aren't
        # ordered.
        for dice_name in self.key_order:
            display_string += '\t' + str(self.dices[dice_name])
        print display_string
        print '-' * 80 + '\n'
    
    # Takes a list of dice values and assigns it to self.dices in the correct order
    def assign(self, list_of_dice):
        self.dices = dict(zip(self.key_order, list_of_dice))
        
    def keep(self, dice_val_to_keep):
        print "\nKeeping %d and re-rolling other dice.\n" % dice_val_to_keep
        for key, dice in self.dices.iteritems():
            if not dice == dice_val_to_keep:
                game_dice.roll(key)

# This is the state where the user inputs something and the class parses the
# result. It also must keep a count of how many rolls have been played.

class User(object):
    
    score_fields = {
        'ones': SingleFace(1),
        'twos': SingleFace(2),
        'threes': SingleFace(3),
        'fours': SingleFace(4),
        'fives': SingleFace(5),
        'sixes': SingleFace(6),
        'three of a kind': ThreeOfaKind(),
        'four of a kind': FourOfaKind(),
        'full house': FullHouse(),
        'small straight': SmallStraight(),
        'large straight': LargeStraight(),
        'chance': Chance(),
        'yahtzee': Yahtzee()
        }

    def __init__(self):
        self.instruction = None
        self.rolls_remaining = 2
        game_dice.roll_all()
    
    # prompt(score_sheet) takes the user input and parses it
    
    def prompt(self, score_sheet):
       
        game_dice.display_dice()
        print ("Select a score field or choose dice to re-roll." +
            " (%d)") % self.rolls_remaining
        action = raw_input("> ")
        
        # Convert any upper case letters to lower case
        action = action.lower()
        
        # Convert action and dice names to Set Objects
        # This will be used in an elif condition
        dice_user_wants = Set(action)
        available_dice = Set(''.join(game_dice.dices.keys()))        
        
        # First, check if it is a score assignment
        
        if action in self.score_fields.keys():
            
            # Check to see if the score field is available to be played.
            # Also takes into account yahtzee bonus
            
            if not score_sheet.score[action][1] or \
                score_sheet.yahtzee_playable(game_dice.dices.values()):
                
                # Create a class for the score field
                scr_field = self.score_fields.get(action)
                
                # Convert dice values into a list
                dice_values = game_dice.dices.values()
                
                # Calculate the score
                score = scr_field.calculate(dice_values)
                
                # Assign the score on the score sheet
                score_sheet.score[action][0] = score
                
                # Mark the score field as played
                score_sheet.score[action][1] = True
                
                # Print score
                score_sheet.print_score()
                
                # Reset rolls remaining
                self.rolls_remaining = 2
                
                # Roll all dice for next turn
                game_dice.roll_all()
                
                if not score_sheet.all_played():
                    print "\nNew turn. Here are your dice:"
                
                
            else:
                print "\nYou have already played %s." % action
        
        # help info
        elif action == 'help':
            print ("\nTo allocate a set of dice to a score, type in the name of score field.\n\n" +\
                   "To re-roll, type in the labels of the dice to re-roll or type in a number to keep.\n" +\
                   "For example, if you enter 2, all dices that are not 2 will be re-rolled.\n\n" +\
                   "Commands:\n" +\
                   "\tmode  - will determine the mode of the dice-set and roll all non-modal dice.\n" +\
                   "\tsort  - sorts the dice in ascending order.\n" +\
                   "\tscore - displays the score sheet.\n")
        
        # sort command allows the dice to be sorted in ascending order.    
        elif action == 'sort':
            game_dice.assign(sorted(game_dice.dices.values()))
            
        elif action == 'score':
            score_sheet.print_score()
        
        
        # Rolls remaining. All commands associated with re-rolling should go
        # below this elif
        
        elif self.rolls_remaining == 0:
            print "\nYou have no more rolls remaining. Please select a score field."

        # Re-rolling dice by letters        
        elif dice_user_wants.issubset(available_dice):
            
            # convert set to a list
            dice_to_roll = list(dice_user_wants)
            
            for dice in dice_to_roll:
                game_dice.roll(dice)        
            
            self.rolls_remaining -= 1
            
        
        # mode command just keeps the modal dice value and re-rolls other dice
        elif action == 'mode':
            # set up a ScoreField object to utilise the mode function
            scr_field = ScoreField()
            list_of_modes = scr_field.modes(game_dice.dices.values())
            
            
            # Unimodal case
            if list_of_modes[0][1] >= 2 and list_of_modes[1][1] <= 1:
                modal_value = list_of_modes[0][0]
                game_dice.keep(modal_value)
                self.rolls_remaining -= 1
                        
            # Bimodal case
            elif list_of_modes[0][1] == 2 and list_of_modes[1][1] == 2:
                mode_1 = list_of_modes[0][0]
                mode_2 = list_of_modes[1][0]
                print "Would you like to keep %d or %d?" % (mode_1, mode_2)
                user_mode = raw_input("> ")
                
                if user_mode == str(mode_1):
                    game_dice.keep(mode_1)
                    self.rolls_remaining -= 1
                    
                elif user_mode == str(mode_2):
                    game_dice.keep(mode_2)
                    self.rolls_remaining -= 1
                
                else:
                    print "You must either select %d or %d?" % (mode_1, mode_2)
                    
            # No mode case
            else:
                print "No mode exists."
                
        # Command to roll all dice
        elif action == 'all':
            game_dice.roll_all()
            
        # Keep dice of a certain value
        elif action in list("123456"):
            game_dice.keep(int(action))
            self.rolls_remaining -= 1        
        
        # cheat for testing yahtzee bonus
        elif action == 'yz':
            game_dice.assign([3, 3, 3, 3, 3])
        
        else:
            print "\nUnknown command."

# Global variables
game_dice = Dice()