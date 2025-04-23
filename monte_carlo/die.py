import pandas as pd
import numpy as np

class Die():
    '''
    This class provides methods for creating a rolling a dice. For this class, a die is any discrete random variable 
    associated with a stochastic process.
    
    Attributes:
    
    faces: the sides the die has. Each side must contain a unique string or number (type: numpy array).
    weights: the probability each side will land "up" when rolled (type: list of int or float).
    '''
    
    def __init__(self, faces):
        '''initialize the die instance. Weight defaults to 1 for each face but can be changed after the object is created'''
        self.faces = faces
        
        #check that faces is an np array
        if type(self.faces) != np.ndarray:
            raise TypeError("Faces must be NumPy array")
        
        #check if faces are all unique"
        if len(self.faces) != len(np.unique(self.faces)):
            raise ValueError("All faces must be unique")
        self.weights = [1.0 for i in self.faces]
        self._die = pd.DataFrame({'weights' : self.weights}, index = self.faces)
        self._die.index.name = "Faces"
        
    def change_weight(self,face,weight):
        '''changes the weight of one face if that face is on the die and the weight is a valid value'''
        
        #check if provided value is a face
        if face not in list(self._die.index):
            raise IndexError(face, "is not a face on this die.")
        
        #check is weight is int, float, or can be casted to int
        if type(weight) != int | float:
            try:
                weight = float(weight)
            except TypeError as e:
                print(e)
        
        #change weight
        self._die.loc[(face,'weights')] = weight
    
    def roll_die(self, rolls=1):
        '''roll the die a specificed amount of times. Default is 1 roll'''
        
        #calculate probablity of rolling each face
        prob = [i/sum(self._die.weights) for i in self._die.weights]
        
        # get random sample of faces based on probability associated with rolling each then return the list
        return [np.random.choice(self._die.index, replace = True, p=prob) for i in range(rolls)]
            
    def current_state(self):
        '''Takes no arguments and returns a copy of the private die data frame'''
        
        copy = self._die.copy()
        
        return copy

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
        
        # roll each dice in the list and store the results in a dictionary 
        # where the key is the position in the list and the value is the list of results
        outcome = {self.pieces.index(piece): piece.roll_die(rolls) for piece in self.pieces}
        
        # convert dictionary into a dataframe where the column names are the list index 
        # and the row names are the roll number
        self._play_results  = pd.DataFrame(outcome, index=[i+1 for i in range(0,rolls)])
        self._play_results.index.name = "roll_num"
        
    def show_outcome(self, form="wide"):
        '''
        takes a string parameter (either "wide" or "narrow") and returns a copy of the private play data frame to the user 
        in either wide or narrow form.
        
        The narrow form will have a MultiIndex, comprising the roll number and the die number and a single column with the 
        outcomes
        '''
        
        # convert parameter entry to all lowercase
        self.form = form.lower()
        
        # if user indicates wide form, return a copy of the data frame as is
        if self.form == "wide":
            return self._play_results
        
        # if user indicates wide form, format data frame and return a copy
        elif self.form == "narrow":
            narrow = self._play_results.copy()
            narrow
            ## convert play_game dataframe to narrow format and return that
        
        # if the uswer enters anything else, raise a error
        else:
            raise ValueError("Please specify either narrow or wide.")