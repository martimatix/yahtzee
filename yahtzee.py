from states import *
from sys import exit
    
class Engine(object):
    
    def __init__(self, User):
        self.player = User
    
    def play(self):
        
        # Welcome block
        screen_width = 80
        welcome_text = "Welcome to Yahtzee!"
        spacing = (screen_width - len(welcome_text))/2
        print '-' * screen_width
        print ' ' * spacing + welcome_text
        print '-' * screen_width
        
        # Main loop of the game
        print "Here is your first roll. Type help for assistance."
        while not a_score_sheet.all_played():
            a_user.prompt(a_score_sheet)
            
        print "\nYour final score is %d. Goodbye!\n" %a_score_sheet.total()
        exit()
       
if __name__=='__main__':
    game_dice = Dice()
    a_score_sheet = ScoreSheet()
    game_dice = Dice()
    a_user = User()
    a_game = Engine(a_user)
    a_game.play()