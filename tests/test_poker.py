import unittest
from card_engine.decks import french, Card


class PokerCardsTestCase(unittest.TestCase):
    def test_exception_on_args(self):
        with self.assertRaises(Exception):
            Card(5, rank=7, suit="diamond")

    def test_wrong_kwargs(self):
        # wrong number
        with self.assertRaises(Exception):
            Card(rank=7)
        # wrong names
        with self.assertRaises(Exception):
            Card(rank=7, geppetto="diamond")

    def test_wrong_conditions(self):
        for i in range(-10, 1):
            with self.subTest(i=i):
                with self.assertRaises(Exception):
                    Card(rank=i, suit="diamond")
        for i in range(14, 100):
            with self.subTest(i=i):
                with self.assertRaises(Exception):
                    Card(rank=i, suit="diamond")

    def test_wrong_types(self):
        wrong_types = [
            {"rank": 5.0, "suit": "diamond"},
            {"rank": 5, "suit": 5},
            {"rank": "bella", "suit": "diamond"}
        ]
        for w in wrong_types:
            with self.subTest(i=w):
                with self.assertRaises(Exception):
                    self.assertRaises(AttributeError, Card(**w))

    def test_list_membership(self):
        with self.assertRaises(Exception):
            Card(rank=1, suit="pinocchio")

    def test_immutability(self):
        card = Card(rank=1, suit="club")
        with self.assertRaises(Exception):
            card.rank = 5
        with self.assertRaises(Exception):
            card.suit = 7


if __name__ == '__main__':
    unittest.main()
