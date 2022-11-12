import random

class Card:

    def _init_(self):
        self.card_value = 0
        self.next_card_value = 0

    def show_card(self):
        self.card_value = random.randint(1,13)
        print("----------------------")
        print(f"The card is: {self.card_value}")

    def show_next_card(self):
        self.next_card_value = random.randint(1,13)
        print(f"Next card was: {self.next_card_value}")
