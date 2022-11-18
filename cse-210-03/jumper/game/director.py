from game.terminal_service import TerminalService
from game.word import Word
from game.jumper import Jumper


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._word = Word()
        self._jumper = Jumper()
        self._is_playing = True
        self._is_correct = True
    
        self._terminal_service = TerminalService()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self._word.word_selected()
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Asks player to guess a letter"""
        self._word.word_selected_guess()
        print("\n")
        self._jumper.display_parachute()
        player_guess = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
        self._is_correct = self._word.evaluate_guess(player_guess)

    def _do_updates(self):
        """Keeps watch if the jumper is still alive"""
        if not self._is_correct:
            self._jumper.remove_parachute(True)

        
    def _do_outputs(self):
        """Provides hints for the player to guess word"""
        if self._word.get_status() == True:
            self._is_playing = False
            print("\nYou guessed it right and saved the jumper!!\n")
            self._jumper.display_alive_jumper()
        elif self._jumper.get_status() == False:
            self._is_playing = False
            self._word.word_selected_guess()
            print("\n")
            self._jumper.display_parachute()
            print("You lost!! ") 