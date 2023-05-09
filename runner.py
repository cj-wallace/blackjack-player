import random
from deck import Deck
from hand import Hand

class Input(enumerate):
    NULL = 0
    HIT = 1
    STAND = 2
    DOUBLE = 3
    SPLIT = 4
    SURRENDER = 5

class Runner():

    def __init__(self):
        self.deck = None
        self.hand = None
        self.dealer_hand = None
        self.win = False
        self.result_type = None

    def run_hand(self, print_output=False):
        self.deck = Deck()

        self.output("1v1 Blackjack", print_output)
        self.hand = Hand(self.deck.draw(2), False)
        self.dealer_hand = Hand(self.deck.draw(2), True)

        #Check for blackjack
        if self.hand.score(True) == 21:
            self.output("Blackjack!", print_output)
            self.output("Hand :"+ self.hand.print_hand(True,True), print_output)
            self.output("Dealer: "+ self.dealer_hand.print_hand(True,True), print_output)
            self.hand.evaluate(self.dealer_hand)
            return

        self.output("Hand :"+ self.hand.print_hand(True,True), print_output)
        self.output("Dealer: "+ self.dealer_hand.print_hand(True,True), print_output)

        input_mode = True
        self.output("Getting Input", print_output)
        while input_mode:
            new_input = self.get_input()

            if new_input == Input.STAND:
                input_mode = False
            elif new_input == Input.HIT:
                self.hand.hit(self.deck.draw(1))
                self.output("Hand :"+ self.hand.print_hand(False,True), print_output)
                if self.hand.score(False) > 21:
                    input_mode = False
        self.output("Outcome", print_output)
        self.output("Hand :"+ self.hand.print_hand(False,True), print_output)
        self.output("Dealer: "+ self.dealer_hand.print_hand(False,True), print_output)
        self.hand.evaluate(self.dealer_hand)

    def get_input(self):
        r = random.randint(0, 99)
        if r < 50:
            return Input.HIT
        else:
            return Input.STAND

    def output(self, text, print_output):
        if print_output==True:
            print(text)
