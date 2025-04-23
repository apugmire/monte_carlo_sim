import pandas as pd
import numpy as np

class Game():
    
    '''
    This class provides methods for playing a game with a die or dice and viewing the results. These methods require a die
    or dice from the Die class. The die must also be similar, i.e. they must have the same number of sides and associated 
    faces, but each die object may have its own weights.

    Game objects only keep the results of their most recent play.

    Attributes:
    
    pieces: a list of already instantiated similar dice to be used in the game (type: list)
    '''
    
    def __init__(self,pieces):
        '''initialize the list of die/dice to be used in the game'''
        
        self.pieces = pieces
        
    def play_game(self, rolls):
        '''takes an integer parameter to specify how many times the dice should be rolled and saves the result of the
        roll(s) in a wide format data frame'''
        
        # roll each dice in the list and store the results in a dictionary where the key is the position in the list and the
        # value is the list of results
        outcome = {self.pieces.index(piece): piece.roll_die(rolls) for piece in self.pieces}
        
        # convert that dictionary into a dataframe where the column names are the list index 
        # and the row names are the roll number
        self._results  = pd.DataFrame(outcome, index=[i+1 for i in range(0,rolls)])
        
    
    def show_outcome(self, form="wide"):
        
        self.form = form.lower()
        
        if self.form == "wide":
            returns self._results
        #elif self.form == "narrow":
            ## convert play_game dataframe to narrow format and return that
        else:
            raise ValueError("Please specify either narrow or wide.")
        
        