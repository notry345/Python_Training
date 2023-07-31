FACES=list(range(2,11))+['Jack','Queen','King','Ace']
SUITS=['Clubs','Diamonds','Hearts','Spades']

class Card(object):
    """A Blackjack card."""
    """Already defined __inti__ and value methods"""
    def __init__(self,face,suit):
        assert face in FACES and suit in SUITS
        self.face = face
        self.suit = suit
    def value(self):
        if type(self.face) == int:
            return self.face
        elif self.face == "Ace":
            return 11
        else:
            return 10
    def __str__(self):
        article = "a "
        if self.face in [8, "Ace"]:
            article = "an "
        return (article + str(self.face) + " of " + self.suit)

    def __eq__(self,rhs):
        return (self.face == rhs.face and
                self.suit == rhs.suit)
    def __ne__(self,rhs):
        return not self == rhs


import random
class Deck(object):
    """A deck of cards."""
    def __init__(self):
        "Create a deck of 52 cards and shuffle them."
        self.cards = []
        for suit in SUITS:
            for face in FACES:
                self.cards.append(Card(face,suit))
        random.shuffle(self.cards)
    def draw(self):
        """Draw the top card from the deck."""
        return self.cards.pop()


def hand_value(hand):
    total = 0
    for card in hand:
        total += card.value()
    return total

num_players = 1
num_cards = 1
deck = Deck()
hands = []
for j in range(num_players):
    hands.append([])
for i in range(num_cards):
    for j in range(num_players):
        card = deck.draw()
        hands[j].append(card)
        print("Player",j+1,"draws",card)
for j in range(num_players):
    print("Player %d's hand (value %d):"%
          (j+1,hand_value(hands[j])))
    for card in hands[j]:
        print(" ",card)


class Table(object):

    def ask(slef,prompt):
        self.question.setMessage(prommpt)
        while True:
            e = self.canvas.wait()
            d = e.getDescription()
            if d == "canvas close":
                sys.exit(1)
            if d == "keyboard":
                key = e.getKey()
                if key == 'y':
                    return True
                if key == 'n':
                    return False



















 










