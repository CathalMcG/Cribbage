import random

RANKS=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
SUITS="DCHS"


class Card(object):
    def __init__(self, rank, suit):
        self._suit = suit
        self._rank = rank

    def __repr__(self):
        return "Card()"

    def __str__(self):
        return f"<Card {self.to_string()} >"

    def get_rank(self):
        return self._rank

    def get_suit(self):
        return self._suit

    def to_string(self):
        return f"{self._rank}{self._suit}"


class CardList(object):
    # a list of Cards
    # the head of the list is the top of the deck
    def __init__(self):
        self._cards = self._create_deck()

    def __repr__(self):
        return "CardList()"

    def __str__(self):
        list_str = self.to_string()
        return f"<CardList {list_str}>"

    def to_string(self):
        return ", ".join(list(map(lambda c: c.to_string(), self._cards)))

    def size(self):
        return len(self._cards)


class Deck(CardList):

    def __init__(self):
        self._cards = self._create_deck()

    def __repr__(self):
        return "Deck()"

    def __str__(self):
        deck_str = self.to_string()
        return f"<Deck {deck_str}>"

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self, number_to_draw=1):
        drawn = self._cards[0:number_to_draw]
        self._cards = self._cards[number_to_draw:]
        return Hand(drawn)

    def _create_deck(self):
        return [Card(r,s) for s in SUITS for r in RANKS ]


class Hand(CardList):

    def __init__(self, cards):
        self._cards = cards

    def add_card(self, card):
        self._cards.append(card)

    def __repr__(self):
        return "Hand()"

    def __str__(self):
        hand_str = self.to_string()
        return f"<Hand {hand_str}>"
