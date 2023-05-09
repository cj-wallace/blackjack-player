import random
from hand import Hand
from runner import Input

class Strategy():
    def __init__(self):
        strat_name = None
        pass

    def get_input(self, hand, dealer_hand):
        r = random.randint(0, 99)
        if r < 50:
            return Input.HIT
        else:
            return Input.STAND
