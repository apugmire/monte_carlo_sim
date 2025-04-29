# Project Name: `monte_carlo_sim`

**Author**: `Alysa Pugmire`

**Version**: `v1.0.0`

**License**: `MIT`

**Python Version**: `3.11.4`

---

## Description

This module implements a simple Monte Carlo Simulator using three related classes - a Die class, a Game class, and an Analyzer class. In this simulator, a “die” can be any discrete random variable associated with a stochastic process, such as using a deck of cards, flipping a coin, rolling an actual die, or speaking a language. This modules provides methods for instantiating instances of Die, Game, and Analyzer objects as well as provides methods for interacting with those objects and analysing the results of 'rolls'.

## Quick Demo

Install:
```python
pip install monte_carlo
```

Import:
```python
from monte_carlo import Die, Game, Analyzer
```

```python

import numpy as np

#create two Die objects, each with six faces
fair = Die(np.array([1,2,3,4,5,6]))
unfair = Die(np.array([1,2,3,4,5,6]))

#change the weights of the 'unfair' die so it favors odd numbers
unfair.change_weight(1,10)
unfair.change_weight(3,10)
unfair.change_weight(5,5)

#create a Game object that uses one fair die and two unfair die
demo = Game([fair,unfair,unfair])

#roll each die five times
demo.play_game(5)

#see the result of those five rolls in wide format
demo.show_outcome()

#create an Analyzer object to analyze the results
analysis = Analyzer(demo)

#check how many times all five dice were the same face
nalysis.jackpot() #output is 0

#see a count of all the different combinations of rolls
analysis.combo_count()

#see the unique permutations and their counts
analysis.perm_count()
```
Results:

show_outcome:

| dice_num |     0      |     1      |     2      |
|-------------------------------------------------|
| roll_num |            |            |            |
|----------|------------|------------|------------|
|    0     |     1      |     3      |     3      |
|    1     |     5      |     1      |     1      |
|    2     |     2      |     2      |     3      |
|    3     |     5      |     6      |     3      |
|    4     |     6      |     5      |     6      |


combo_count:

|   |   |   | Count |
| 0 | 1 | 2 |       |
|---|---|---|-------|
| 1 | 1 | 5 | 1     |
| 3 | 3 | 1 | 1     |
| 2 | 2 | 3 | 1     |
| 3 | 5 | 6 | 1     |
| 5 | 6 | 6 | 1     |

perm_count:

|   |   |   | Count |
| 0 | 1 | 2 |       |
|---|---|---|-------|
| 1 | 3 | 3 | 1     |
| 2 | 2 | 3 | 1     |
| 5 | 1 | 1 | 1     |
|   | 6 | 3 | 1     |
| 6 | 5 | 6 | 1     |


## API Reference

### class Die(faces: np.array)

This class provides methods for creating a rolling a dice. For this class, a die is any discrete random variable associated with a stochastic process. 
    
Attributes:
    
faces: the sides the die has. Each side must contain a unique string or number (type: numpy array).
weights: the probability each side will land "up" when rolled (type: list of int or float).

#### .change_weight(weight: int)

Takes an integer or float parameter and changes the weight of one face if that face is on the die and the weight is a valid value. Will attempt to cast the provided parameter to a float if possible. Changes the state of the Die object.

#### .roll_die(roll: int)

Takes an integer parameter to specify how many times the dice should be rolled. Default is 1 roll. Does not return anything.

#### .current_state()

Takes no arguments and returns a copy of the die at this point in time as a pd.DataFrame. Will show the faces and any changes to the weights if called after .change_weight()

### class Game(peices: list)

This class provides methods for playing a game with a die or dice and viewing the results. These methods require a die or dice from the Die class. The die must also be similar, i.e. they must have the same number of sides and associated faces, but each die object may have its own weights.

Game objects only keep the results of their most recent play.

Attributes:
    
pieces: a list of already instantiated similar dice to be used in the game (type: list)

#### .play_game(rolls: int)

Takes an integer parameter to specify how many times the dice should be rolled. Does not return anything but changes the object's state.

#### .show_outcome(form: str)

Takes a string parameter (either "wide" or "narrow") and returns a copy of roll(s) to the user in either wide or narrow form.
     
The narrow form will have a MultiIndex, comprising the roll number and the die number and a single column with the outcomes.

### class Analyzer(game: Game)

This class provides methods for analyzing the results of a single game. These methods require a game from the Game class. This class takes the results of a single game and computes various descriptive statistical properties about it.

Attributes:
    
game: an instantiated game object (type: Game)

#### .jackpot()

Takes no parameters. Computes how many times the game resulted in a jackpot. A jackpot is a result in which all faces are the same. Returns an integer for the number of jackpots.

#### .face_count()

Takes no parameters. Computes how many times each face is rolled in each roll. Returns a pd.DataFrame where the index is the roll number, the columns are the face values, and cells are the count values.

#### .combo_count()

Takes no parameters. Computes the distinct combinations of faces rolled, along with their counts. The combinations are order-independent and repetition is allowed. Returns a pd.DataFrame with a MultiIndex of distinct combinations and a column for the associated counts.

#### .perm_count()

Takes no parameters. Computes the distinct permutations of faces rolled, along with their counts. The permutations are order-dependent and repetition is allowed. Returns a pd.DataFrame with a MultiIndex of distinct permutations and a column for the associated counts
