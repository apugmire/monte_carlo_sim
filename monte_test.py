import unittest
import pandas as pd
import numpy as np

from monte_carlo import Die, Game, Analyzer

class DieTestSuite(unittest.TestCase):
    
    def test_01_create_die(self):
        
        reg = np.array([1,2,3,4,5,6]) 
        
        die1 = Die(reg) #create die with 6 faces
                       
        self.assertTrue(type(die1)==Die and len(die1.faces)==6) # confirm type is die and there are 6 faces
        
    def test_02_change_weight_bad(self):
        
        alph = np.array(["A","B","C","D"]) 
        
        die2 = Die(alph) #create die with 4 faces
        
        
        with self.assertRaises(IndexError): #should raise exception since E is not a face
            die2.change_weight("E",10) #change weight of E to 10
        
    def test_03_change_weight_good(self):
    
        alph = np.array(["A","B","C","D"]) 
        
        die3 = Die(alph) #create die with 4 faces
        
        die3.change_weight("B",6) #change weight of B to 6
        
        actual = die3._die.loc[("B", "weights")]
        
        expected = 6
        
        self.assertEqual(actual,expected) #test if the weight of B is now 6
    
    def test_04_roll_die(self):
        
        even = np.array([2,4,6,8,10,12,14,16,18,20])
        
        die4 = Die(even)
        
        actual = die4.roll_die(5) #roll the die 5 times
    
        self.assertTrue(len(actual) == 5 and sum(actual) >= 10) #confirm die was rolled 5 times and resulting values are
                                                                #possible (lowest value that could possibly be rolled is 
                                                                #5 2's so 10
        
    def test_05_current_state(self):
        
        odd = np.array([1,3,5])
        
        die5 = Die(odd)
        
        die5.change_weight(1,5) #change weight of once face
        
        state = die5.current_state()
        
        self.assertIsInstance(state, pd.DataFrame) #check the copy is a data frame
        
        self.assertEqual(list(state.index), odd.tolist()) #check the faces are actually the faces
        
        expectedwt = [5.0,1.0,1.0]
        actualwt = state['weights'].tolist()
        
        self.assertEqual(actualwt, expectedwt)
    
class GameTestSuite(unittest.TestCase):

    def test_06_create_game(self):
        
        die6 = Die(np.array(["A","B","C"]))
        
        die7 = Die(np.array(["A","B","C"]))
                         
        game1 = Game([die6,die7]) #create game with two dice
                         
        self.assertTrue(type(game1)==Game and len(game1.pieces) ==2) #confirm game1 is a Game with 2 dice
    
    def test_07_play_game(self):
        
        die8 = Die(np.array(["A","B","C"]))
        
        die9 = Die(np.array(["A","B","C"]))
                         
        game2 = Game([die8,die9]) #create game with two dice
        
        game2.play_game(4) # roll each die 4 times
        
        actual = len(game2.show_outcome()) #play_game only updates the object's state, using show_outcome to confirm state
                                           #was updated correcty
        
        expected = 4
        
        self.assertEqual(actual,expected) #confirm each die was rolled 4 times
    
    def test_08_show_outcome_wide(self):
        
        die10 = Die(np.array(["A","B","C"]))
        
        die11 = Die(np.array(["A","B","C"]))
                         
        game3 = Game([die10,die11]) #create game with two dice
        
        game3.play_game(7)
        
        outcome = game3.show_outcome()
        
        self.assertIsInstance(outcome, pd.DataFrame) #check the outcome is a data frame
    
    def test_09_show_outcome_narrow(self):
        
        die12 = Die(np.array(["A","B","C"]))
        
        die13 = Die(np.array(["A","B","C"]))
                         
        game4 = Game([die12,die13]) #create game with two dice
        
        game4.play_game(7) #roll 7 times
        
        outcome = game4.show_outcome('narrow') #how results in narrow form
        
        self.assertIsInstance(outcome, pd.DataFrame) #check the outcome is a data frame
        
        self.assertEqual(outcome.shape, (14,1)) #check there are 14 rows and one column
        
        self.assertEqual(outcome.index.names, ['roll_num', 'die_num']) # check presence of multiindex and index names
    
class AnalyzerTestSuite(unittest.TestCase):
    
    def test_10_create_analyzer_bad(self):
        
        die14 = Die(np.array(["T", "F"]))
        
        die15 = Die(np.array(["T", "F"]))
                         
        game5 = Game([die14,die15]) #create game with two dice
                         
        with self.assertRaises(ValueError):
            a1 = Analyzer(die14) #attempt to initialize with no class
        
    def test_11_create_analyzer_good(self):
        
        die16 = Die(np.array(["T", "F"]))
        
        die17 = Die(np.array(["T", "F"]))
                         
        game6 = Game([die16,die17]) #create game with two dice
                         
        a2 = Analyzer(game6)   
        
        self.assertTrue(type(a2)==Analyzer and len(a2.game.pieces)==2) #confirm a2 is an Analyzer of a Game with 2 pieces
    
    def test_12_jackpot(self):
        
        die18 = Die(np.array(["T"]))
        
        game7 = Game([die18, die18]) #create a Game with two dice
        
        game7.play_game(4) # roll 4 times
        
        a3 = Analyzer(game7) #analyze
        
        actual = a3.jackpot() #since all faces are the same, we should get jackpot every time
        expected = 4
        
        self.assertEqual(actual,expected) #check that we actually did get jackpot each time
    
    def test_13_face_count(self):
                         
        die20 = Die(np.array(["H", "T"]))
        
        die21 = Die(np.array(["H", "T"]))
        
        game8 = Game([die20, die21]) #create a Game with two dice
        
        game8.play_game(10) #play game with 10 rolls
        
        a4 = Analyzer(game8) # analyze
                         
        actual = a4.face_count().shape # should have 10 rows and 2 columns since
                         
        expected = (10,2)
                         
        self.assertIsInstance(a4.face_count(), pd.DataFrame)  # check result is a data frame
        self.assertEqual(actual,expected)                    #check the shape is correct. Should have a row for each roll
                                                             #and a column for each face
    def test_14_combo_count(self):
    
        die22 = Die(np.array(["H", "T"]))
        
        die23 = Die(np.array(["H", "T"]))
        
        game9 = Game([die22, die23]) #create a Game with two dice
        
        game9.play_game(6) #play game with 6 rolls
        
        a5 = Analyzer(game9) #analyze
        
        self.assertIsInstance(a5.combo_count(), pd.DataFrame) #confirm result is a pandas data frame
        self.assertIsInstance(a5.combo_count().index, pd.MultiIndex) #confirm presence of multiindex
        
    def test_15_pem_count(self):
        
        die24 = Die(np.array(["Ace", "King", "Queen", "Jack"]))
        
        die25 = Die(np.array(["Ace", "King", "Queen", "Jack"]))
        
        game10 = Game([die24, die25]) #create a Game with two dice
        
        game10.play_game(100) # play game with 100 rolls
        
        a6 = Analyzer(game10) # analyze
            
        self.assertIsInstance(a6.perm_count(), pd.DataFrame) #confirm result is a pandas data frame
        self.assertIsInstance(a6.perm_count().index, pd.MultiIndex) #confirm presence of multiindex

if __name__ == '__main__':
    
    unittest.main(verbosity=3)