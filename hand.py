from card import Card

class Hand:
    def __init__(self, cards, dealer=False):
        self.cards = cards
        self.dealer = dealer

    def score(self, initial=False):
        score = 0

        if initial:
            c1 = Card.get_score(self.cards[0])
            c2 = Card.get_score(self.cards[1])
            if self.dealer:
                score += c1
            else:
                score += c1 + c2
        else:
            for i in range(len(self.cards)):
                card_score = Card.get_score(self.cards[i])

                if card_score == 11 and score + card_score > 21:
                    card_score = 1

                score += card_score

                if score > 21:
                    score = 0
                    break

        return score

    def print_hand(self, initial=False):
        """
        Print cards list using Cards.print.
        """
        output = ""
        if initial:
            c1 = str(Card.print_card(self.cards[0]))
            c2 = str(Card.print_card(self.cards[1]))
            if self.dealer:
                output += c1
            else:
                output += c1 + ", " + c2
        else:
            for i in range(len(self.cards)):
                c = self.cards[i]
                if i != len(self.cards) - 1:
                    output += str(Card.print_card(c)) + ","
                else:
                    output += str(Card.print_card(c)) + " "
        return output

    def hit(self, card):
        self.cards.append(card)

