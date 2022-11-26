import random 

class Word:

    def __init__(self):
        """Constructs a new Word.
        
        Args:
            self (Word): an instance of Word.
        """ 
        self._words = ['tandem','castle','sculpt']
        self._selected_word = ''
        self._guess = ['_','_','_','_','_','_']
        self._is_solved = False
        
    
    def word_selected(self):
        """Randomly choose a word from the word list
        """
        word = random.choice(self._words)
        self._selected_word = list(word)

    def get_word_guess(self):
        """Get the hint
        """
        return self._guess
            
    def evaluate_guess(self, guess):
        """Evaluate each guess letter
        """
        word = self._selected_word
        if guess in word:
            self._guess[word.index(guess)] = guess
            return True
        else:
            return False

    def get_status(self):
        if '_' not in self._guess:
            self._is_solved = True

        return self._is_solved        
            
