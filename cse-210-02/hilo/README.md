## Week 2 - HiLo

Hilo is a game in which the player guesses if the next card drawn by the dealer will be higher or lower than the previous one. Points are won or lost based on whether or not the player guessed correctly.

### Rules

Hilo is played according to the following rules.

- The player starts the game with 300 points.
- Individual cards are represented as a number from 1 to 13.
- The current card is displayed.
- The player guesses if the next one will be higher or lower.
- The the next card is displayed.
- The player earns 100 points if they guessed correctly.
- The player loses 75 points if they guessed incorrectly.
- If a player reaches 0 points the game is over.
- If a player has more than 0 points they decide if they want to keep playing.
- If a player decides not to play again the game is over.

### Requirements

The program must also meet the following requirements.

- The program must include a README file.
- The program must include class and method comments.
- The program must have at least two classes.
- The program must remain true to game play described in the overview.

### Project Structure

**Object**: Director

**Responsibility**: Control sequence of play

**Behaviors**:

- start game
- show card
- get input
- show next card
- make evaluation
- show score
- play again? (end game)

**State**:

- card
- next card
- guess
- score
- total score

**Object**: Card

**Responsibility**: Create a random card with a value from 1-13

**Behaviors**:

- get value

**State**:

- value (1-13)

---

#### Class - Director

#### Variables:
- card: Card
- next_card: Card
- score: integer
- guess: string
- is_playing: boolean
- total_score: integer

#### Methods:
- start_game(): None
- show_card(): None
- get_input(): None
- show_next_card(): None
- make_evaluation(): None
- show_score(): None
- play_again(): None

#### Class - Card

#### Variables:
- value: integer

#### Methods:
- get_value(): None

The relationship between objects: The director has cards.

---

**Norre Daroy**

*norrej.daroy@gmail.com*
