import random
from time import perf_counter, time
start = perf_counter()
class Card():
    converterToVal = {"ace": 1, "j":11, "jack": 11, "q":12, "queen": 12, "k":13, "king": 13}
    def __init__(self,rank=0,suit=""):
        if type(rank) is int:
            self.rank=rank
        else:
            try:
                self.rank = self.converterToVal[rank.lower()]
            except:
                self.rank=0
                self.suit=""
                return
        if type(suit) is str:
            self.suit=suit.upper()

    def __str__(self):
        converterToCard = {1: "A", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "J", 12: "Q", 13: "K"}
        if self.rank!=0:
            return '{:>3}{}'.format(converterToCard[self.rank],self.suit)
        else:
            return '{:>4}'.format("blk")
    def is_blank(self):
        return not self.rank


class Deck():
    def __init__(self):
        self.deck=[Card( ((i//4)%13)+1, ['s','h','d','c'][i%4]) for i in range(52)]

    def __str__(self):
        kek=[]
        for i in range(len(self.deck)):
            kek.append(str(self.deck[i]))
            if i%13==12:
                kek.append('\n')
        return "".join(kek)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop(0)



class PlayingHand():
    NUMBER_CARDS=13
    def __init__(self):
        self.cards=[Card() for i in range(13)]

    def __str__(self):
        hand=[]
        for card in self.cards:
            hand.append(str(card))
        return "".join(hand)

    def add_card(self,card):
        try:
            i=0
            while self.cards[i].rank!=0:
                i+=1
            self.cards[i]=card
        except:
            return





def test_cards():
     card1 = Card()
     print(card1)
     card2 = Card(5,'s')
     print(card2)
     card3 = Card('Q','D')
     print(card3)
     card4 = Card('x', 7)
     print(card4)
def print_4_hands(hand1, hand2, hand3, hand4):
     ''' Prints the 4 hands '''
     print(hand1)
     print(hand2)
     print(hand3)
     print(hand4)
def deal_4_hands(deck, hand1, hand2, hand3, hand4):
 ''' Deals cards for 4 hands '''
 for i in range(PlayingHand.NUMBER_CARDS):
     hand1.add_card(deck.deal())
     hand2.add_card(deck.deal())
     hand3.add_card(deck.deal())
     hand4.add_card(deck.deal())
def test_hands(deck):
     hand1 = PlayingHand()
     hand2 = PlayingHand()
     hand3 = PlayingHand()
     hand4 = PlayingHand()
     print("The 4 hands:")
     print_4_hands(hand1, hand2, hand3, hand4)
     deal_4_hands(deck, hand1, hand2, hand3, hand4)
     print("The 4 hands after dealing:")
     print_4_hands(hand1, hand2, hand3, hand4)
# The main program starts here
random.seed(10)
test_cards()
deck = Deck()
deck.shuffle()
print("The deck:")
print(deck)
test_hands(deck)
print("The deck after dealing:")
print(deck)
print(perf_counter() - start)