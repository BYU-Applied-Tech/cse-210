from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

class Artifact(Actor):

    def __init__(self):
        self._message = ""
        super().__init__()

    def set_message(self, message):
        self._message = message

    def get_message(self):
        return self._message


        