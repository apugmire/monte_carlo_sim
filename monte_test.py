import unittest
import pandas as pd
import numpy as np

from monte import *

class DieTestSuite(unittest.TestCase):
    
    def test_1_create_die(self):
        
        reg = np.array([1,2,3,4,5,6]) 
        
        die1 = Die(reg) #create die with 6 faces
                       
        self.assertTrue(type(die1)==Die and len(die1.faces)==6) # confirm type is die and there are 6 faces
        
    def test_2_change_weight_bad(self):
        
        alph = np.array(["A","B","C","D"]) 
        
        die2 = Die(alph) #create die with 4 faces
        
        
        with self.assertRaises(IndexError): #should raise exception since E is not a face
            die2.change_weight("E",10) #change weight of E to 10
        
    def test_3_change_weight_good(self):
    
        alph = np.array(["A","B","C","D"]) 
        
        die3 = Die(alph) #create die with 4 faces
        
        die3.change_weight("B",6) #change weight of B to 6
        
        actual = die3._die.loc[("B", "weights")] == 6
        
        expected = 6
        
        self.assertEqual(actual,expected) #test if the weight of B is now 6
    
    def test_4_roll_die(self):
        
        even = np.array([2,4,6,8,10,12,14,16,18,20])
        
        die4 = Die(even)
        
        actual = die4.roll_die(5) #roll the die 5 times
    
        self.assertTrue(len(actual) == 5 and sum(actual) >= 10) #confirm die was rolled 5 times and resulting values are
                                                                #possible (lowest value that could possibly be rolled is 
                                                                #5 2's so 10
        
    def test_5_current_state(self):
        
        odd = np.array([1,3,5])
        
        die5 = Die(odd)
        
        die5.change_weight(1,5) #change weight of once face
        
        state = die5.current_state()
        
        self.assertIsInstance(state, pd.DataFrame) #check the copy is a data frame
        
        self.assertEqual(list(state.index, odd) #check the faces are actually the faces
        
        expectedwt = [5.0,1.0,1.0]
        actualwt = state['weights'].tolist()
        
        self.assertEqual(actualwt, expectedwt)
    
class GameTestSuite(unittest.TestCase):

    def test_6_create_game(self):
        
        die6 = ["A","B","C"]
        
        die7 = ["A","B","C"]
                         
        game1 = Game([die6,die7]) #create game with two dice
                         
        self.assertTrue(type(game1)==Game and len(game.pieces) ==2) #confirm game1 is a Game with 2 dice
    
    def test_7_play_game(self):
        
        die8 = ["A","B","C"]
        
        die9 = ["A","B","C"]
                         
        game2 = Game([die8,die9]) #create game with two dice
        
        x = game2.play_game(4) # roll each die 4 times
        
        actual = len(x._play_results) 
        
        expected = 4
        
        self.assertEqual(actual,expected) #confirm each die was rolled 4 times
    
    def test_8_show_outcome_wide(self):
        
        die10 = ["A","B","C"]
        
        die11 = ["A","B","C"]
                         
        game3 = Game([die10,die11]) #create game with two dice
        
        game3.play_game(7)
        
        outcome = game3.show_outcome()
        
        self.assertIsInstance(outcome, pd.DataFrame) #check the outcome is a data frame
    
    def test_9_show_outcome_narrow(self):
        
        die12 = ["A","B","C"]
        
        die13 = ["A","B","C"]
                         
        game4 = Game([die12,die13]) #create game with two dice
        
        game4.play_game(7) #roll each die 7 times
        
        outcome = game4.show_outcome('narrow')
        
        self.assertIsInstance(outcome, pd.DataFrame) #check the outcome is a data frame
        
        self.assertEqual(outcome.shape, (7,1)) #check there are 7 rows and one column
        
        self.assertEqual(outcome.index.names, ['roll_num', 'die_num']) # check presence of multiindex and index names
    
class AnalyzerTestSuite(unittest.TestCase):
    
    def test_10_create_analyzer_bad(self):
        
        die14 = ["T", "F"]
        
        die15 = ["T", "F"]
                         
        game4 = Game([die14,die15]) #create game with two dice
                         
        with self.assertRaises(ValueError):
            a1 = Analyzer(die14) #attempt to initialize with no class
        
     def test_11_create_analyzer(self):
        
        die16 = ["T", "F"]
        
        die17 = ["T", "F"]
                         
        game5 = Game([die16,die17]) #create game with two dice
                         
        a2 = Analyzer(game4)   
        
        self.assertEqual(type(a2)==Analyzer and len(a2.game.pieces==2)) #confirm a2 is an Analyzer of a Game with 2 pieces
    
    def test_12_jackpot(self):
        
        die18 = ["T", "T"]
        
        die19 = ["T", "T"]
        
        game6 = Game([die18, die19]) #create a Game with two dice
        
        a3 = Analyzer(game6.play_game(4)) #create an Analyzer based on the Game with 4 rolls
        
        actual = a3.jackpot() #since all faces are the same, we should get jackpot every time
        expected = 4
        
        self.assertEqual(actual,expected)
    
    #def test__face_count(self):
        
    #def test__combo_count(self):
    
    #def test__pem_count(self):