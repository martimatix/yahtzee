"""Score sheet class. I opted to use a dictionary as the data structure to hold
the scores. I should've used an ordered dictionary as that would've allowed for
for-loops for returning scores. However, in some ways the explicit nature of
the code may improve readability."""

class ScoreSheet(object):
    def __init__(self):
        # Each score field is a list of the score value and a flag for whether 
        # or its been played.
        
        self.score = {'ones': [0, False],
                      'twos': [0, False],
                      'threes': [0, False],
                      'fours': [0, False],
                      'fives': [0, False],
                      'sixes': [0, False],
                      'three of a kind': [0, False],
                      'four of a kind': [0, False],
                      'full house': [0, False],
                      'small straight': [0, False],
                      'large straight': [0, False],
                      'chance': [0, False],
                      'yahtzee': [0, False]
                      }
        
        # Due to the yahtzee bonus, this variable needs to be introduced
        self.yz_playable = True
    
    # Returns the upper score total
    
    def upper_score(self):
        x = self.score['ones'][0] + self.score['twos'][0] +\
            self.score['threes'][0] + self.score['fours'][0] +\
            self.score['fives'][0] + self.score['sixes'][0]
        return x
    
    
    # Returns True if Upper Score Bonus applies. Otherwise False.
    
    def upper_score_bonus(self):
        if self.upper_score() >= 63:
            return True
        else:
            return False
    
    
    
    # Returns the lower score total
    
    def lower_score(self):
        
        y = self.score['three of a kind'][0] +\
            self.score['four of a kind'][0] +\
            self.score['full house'][0] + self.score['small straight'][0] +\
            self.score['large straight'][0] + self.score['chance'][0] +\
            self.score['yahtzee'][0]
        return y 
   
   
    # Returns the total score.
    
    def total(self):
        z = self.upper_score() + self.lower_score()
        if self.upper_score_bonus() is True:
            z += 35
        return z
   
   
    # Determines what string to print for print_score()
    
    def string_to_print(self, key):
        if self.score[key][1] is True:
            x = str(self.score[key][0])
        else:
            x = '-'
        return x
   
   
    # Prints the current score.
    
    def print_score(self):
        
        print '\n'
        
        title = " S C O R E  S H E E T "
        width = 80
        spacing = (width - len(title))/2
        print "=" * spacing + title + "=" * spacing
        
        print '\n'
        
        x = self.upper_score()
        y = self.lower_score()        
        print "\t\tUPPER SCORE (%d) \t\tLOWER SCORE (%d)" %(x,y)
        
        x = self.string_to_print('ones')
        y = self.string_to_print('three of a kind')
        print "\t\tOnes\t%s\t\t\tThree of a Kind\t%s" % (x,y)
        
        x = self.string_to_print('twos')
        y = self.string_to_print('four of a kind')
        print "\t\tTwos\t%s\t\t\tFour of a Kind\t%s" % (x,y)
        
        x = self.string_to_print('threes')
        y = self.string_to_print('full house')
        print "\t\tThrees\t%s\t\t\tFull House\t%s" % (x,y)
        
        x = self.string_to_print('fours')
        y = self.string_to_print('small straight')
        print "\t\tFours\t%s\t\t\tSmall Straight\t%s" % (x,y)
        
        x = self.string_to_print('fives')
        y = self.string_to_print('large straight')
        print "\t\tFives\t%s\t\t\tLarge Straight\t%s" % (x,y)
        
        x = self.string_to_print('sixes')
        y = self.string_to_print('chance')
        print "\t\tSixes\t%s\t\t\tChance\t\t%s" % (x,y)
        
        if self.upper_score_bonus():
            x = '35'
        else:   
            x = '0'
        y = self.string_to_print('yahtzee')
        print "\t\tBonus\t%s\t\t\tYahtzee\t\t%s" % (x,y)
        
        total_string = "TOTAL = " + str(self.total())
        print '\n' + total_string.center(width, ' ')

        print '\n' + '=' * width
        
    def all_played(self):
        
        # Generate a list of whether each field has been played.
        list_of_played = [field[1] for field in self.score.values()]
        return all(list_of_played)
    
    def yahtzee_playable(self, dice_values):
        
        yahtzee_score = self.score['yahtzee'][0]
        yahtzee_played = self.score['yahtzee'][1]
        
        # A duplication of code from the yahtzee class but as it was one line,
        # it seemed easier to do this than to make a call to the Yahtzee
        # ScoreField class.
        is_yahtzee = all(dice == dice_values[0] for dice in dice_values)
        
        # If yahtzee is played and the score is zero, the Yahtzee field is not
        # playable.
        
        if yahtzee_score == 0 and yahtzee_played:
            return False
        
        elif not is_yahtzee:
            return False
            
        else:   
            return True