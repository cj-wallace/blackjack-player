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


deck = Deck()

print("1v1 Blackjack")
hand = Hand(deck.draw(2), False)
dealer_hand = Hand(deck.draw(2), True)

print("Hand1:", hand.print_hand(True), hand.score(True))
print("Dealer:", dealer_hand.print_hand(True), dealer_hand.score(True))

input_mode = True


def get_input():
    r = random.randint(0, 99)
    if r < 50:
        return Input.HIT
    else:
        return Input.STAND


print("Input")
while input_mode:
    new_input = get_input()

    if new_input == Input.STAND:
        input_mode = False
    elif new_input == Input.HIT:
        hand.hit(deck.draw(1))
        print("Hand1:", hand.print_hand(False), hand.score(False))

print("Outcome")
print("Hand1:", hand.print_hand(False), hand.score(False))
print("Dealer:", dealer_hand.print_hand(False), dealer_hand.score(False))
