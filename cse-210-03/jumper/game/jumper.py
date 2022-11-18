class Jumper:

    def __init__(self):
        """Constructs a new Jumper.
        
        Args:
            self (Jumper): an instance of Jumper.
        """
        self._is_alive = True
        self._parachute = [
            ['  ____'],
            [' /____\\'],
            [' \    /'],
            ['  \  /'],
            ['   O  '],
            ['  /|\\'],
            ['  / \\'],
            ['       '],
            ['^^^^^^^']
            ]
        self._alive_jumper = [
            [' \ O /  '],
            ['   | '],
            ['  / \\'],
            ['^^^^^^^']
            ]

    def display_parachute(self):
       """Display jumper in parachute
       """
       for row in self._parachute:
           print(' '.join([str(elem) for elem in row]))

    def display_alive_jumper(self): 
       """Display for when a jumper is alive
       """
       for row in self._alive_jumper:
           print(' '.join([str(elem) for elem in row]))

    def remove_parachute(self, remove):
        """Remove a line of the parachute guy
        """
        if len(self._parachute) == 6:
            self._parachute.pop(0),
            self._parachute[0] = '   X  ',
            self._is_alive = False
        elif remove:
            self._parachute.pop(0) 

    def get_status(self):
        return self._is_alive