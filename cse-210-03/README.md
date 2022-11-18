## Week 3 - Jumper

Jumper is a game in which the player seeks to solve a puzzle by guessing the letters of a secret word one at a time. 

### Rules

Jumper is played according to the following rules.

- The puzzle is a secret word randomly chosen from a list.
- The player guesses a letter in the puzzle.
- If the guess is correct, the letter is revealed.
- If the guess is incorrect, a line is cut on the player's parachute.
- If the puzzle is solved the game is over.
- If the player has no more parachute the game is over.


### Requirements

 The program must also meet the following requirements.

- The program must include a README file.
- The program must include class and method comments.
- The program must have at least four classes.
- The program must remain true to game play described in the overview.


**Object**: Director

**Responsibility**: Control sequence of game

**Behaviors**:

- start game
- get inputs
- do updates
- do outputs

**State**:

- is playing
- is correct
- word
- jumper
- terminal service

**Object**: Jumper

**Responsibility**: 
-	Stores the parachute
-	Displays the parachute
-	Cuts line of the parachute for every incorrect guess


**Behaviors**:
- display parachute
- cuts line of parachute
- status of jumper


**State**:
- is alive
- parachute

**Object**: Word

**Responsibility**: 
-	Stores list of words to be used
-	Selects word to guess from list
-	Keep track of the status of word guess
-	Displays hints

**Behaviors**:
- select a word randomly
- show hints for word guesses
- evaluate the guesses
- status of word if solved

**State**:
- is alive
- parachute

**Object**: Terminal Service

**Responsibility**: 
-	Handles terminal operations

**Behaviors**:
- read text
- read number
- write text


**State**:
n/a

---

#### Class - Director

#### Variables:
- _is_playing: Boolean
- _is_correct: Boolean


#### Methods:
- start_game(): None
- _get_inputs(): None
- _do_updates(): None
- _do_outputs(): None

#### Class - Jumper

#### Variables:
- _is_alive: Boolean
- _parachute: List String

#### Methods:
- display_parachute(): None
- remove_parachute(): None
- get_status(): Boolean

#### Class - Word

#### Variables:
- _words: List String
- _selected_word: String
- _guess: List String
- _is_solved: Boolean


#### Methods:
- word_selected(): None
- word_selected_guess():None
- evaluate_guess(): Boolean
- get_status(): Boolean


The relationship between objects: 
Director gets a word from Word
Director gets status from jumper and display parachute
Director uses terminal services

---

**Norre Daroy**

*norrej.daroy@gmail.com*
