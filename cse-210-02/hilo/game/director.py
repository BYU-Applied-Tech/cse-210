from game.card import Card

class Director:

    def __init__(self):
        self.is_playing = True
        self.score = 0
        self.total_score = 300
        self.player_input = ""
        self.card = Card()

    def start_game(self):
        card = self.card

        while self.is_playing:
            card.show_card()
            self.get_inputs()
            card.show_next_card()
            self.do_updates()
            self.do_outputs()
            self.play_again()

    def get_inputs(self):
        self.player_input = input("Higher or lower? [h/l]: ")

    def do_updates(self):
        if not self.is_playing:
            return 
        
        card = self.card
        if card.card_value > card.next_card_value:
            if self.player_input == "l":
                self.score = self.total_score + 100
            elif self.player_input =='h':
                self.score = self.total_score - 75
        elif card.card_value < card.next_card_value:
            if self.player_input == "h":
                self.score = self.total_score + 100
            elif self.player_input == "l":
                self.score = self.total_score - 75

        self.total_score = self.score

    def do_outputs(self):
        if self.score == 0:
            self.is_playing = False
            print(f"You lost!")
        else: 
            print(f"Your score is: {self.score}")

    def play_again(self):
        user_play = input("Play again? [y/n]: ")
        print(f"\n")
        
        self.is_playing = (user_play == "y")
       

    def invalid_input(self):
        self.is_playing = False
        print("Game stopped!. You have entered wrong input.")