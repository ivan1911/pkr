from .board import CardCollection
from .hand_eval import Two


class Hand(list):
    """ """
    def __init__(self, cards):
        list.__init__(self, reversed(sorted(cards, key=lambda a: a.rank)))

    @property
    def score(self):
        return Two.evaluate_rank(self)

    def __hash__(self):
        return (
            self[0].rank * 10000 +
            self[0].suit * 1000 +
            self[1].rank * 10 +
            self[1].suit
        )

    @property
    def is_pair(self):
        return self[0].rank == self[1].rank

    @property
    def gap(self):
        return self[0].rank - self[1].rank - 1

    def __repr__(self):
        return 'Hand(%s)' % ', '.join(repr(card) for card in self)

    def __str__(self):
        return ' '.join([str(card) for card in self])

    def __eq__(self, other):
        return self.score == other.score

    def __gt__(self, other):
        return self.score < other.score

    def __lt__(self, other):
        return self.score > other.score


class StartingHand(CardCollection):
    def __init__(self, cards):
        self.cards = cards
        self.cards.sort()
        self.cards.reverse()

    def absolute_strength():
        raise NotImplementedError

    def relative_strength():
        raise NotImplementedError


class HoldEmStartingHand(StartingHand):
    def absolute_strength():
        raise NotImplementedError

    def relative_strength():
        raise NotImplementedError
