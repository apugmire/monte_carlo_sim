import pandas as pd
import numpy as np

class Die():
    '''
    This class provides methods for creating a rolling a dice. For this class, a die is any discrete random variable associated with a stochastic process.
    
    Attributes:
    
    faces: the sides the die has. Each side must contain a unique string or number (type: numpy array).
    weights: the probability each side will land "up" when rolled (type: list of int or float).
    '''
    
    def __init__(self, faces):
        "initialize the die instance. Weight defaults to 1 for each face but can be changed after the object is created"
        self.faces = faces
        
        #check that faces is an np array
        if type(self.faces) != np.ndarray:
            raise TypeError("Faces must be NumPy array")
        
        #check if faces are all unique"
        if len(self.faces) != len(np.unique(self.faces)):
            raise ValueError("All faces must be unique")
        self.weights = [1.0 for i in self.faces]
        self.die = pd.DataFrame({'weights' : self.weights}, index = self.faces)
        self.die.index.name = "Faces"
        
    def change_weight(self,face,weight):
        "changes the weight of one face if that face is on the die and the weight is a valid value"
        
        #check if provided value is a face
        if face not in list(self.die.index):
            raise IndexError({face}, "is not a face on this die.")
        
        #check is weight is int, float, or can be casted to int
        if type(weight) != int | float:
            try:
                weight = float(weight)
            except TypeError as e:
                print(e)
        
        #change weight
        self.die.loc[(face,'weights')] = weight
    
    def roll_die(self, rolls=1):
        "roll the die a specificed amount of times. Default is 1 roll"
        
        #calculate probablity of rolling each face
        prob = [i/sum(self.die.weights) for i in self.die.weights]
        
        #random sample of faces based on probability associated with rolling each
        results = [np.random.choice(self.die.index, replace = True, p=prob) for i in range(rolls)]
        
        #return list of results. Not stored locally
        return results
            
    def current_state(self):
        "Takes no arguments and returns a copy of the private die data frame"
        
        copy = self.die.copy()
        
        return copy