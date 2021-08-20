from itertools import product
from items import Item, Property

_french_raw = product(range(1, 14), ["heart", "diamond", "spade", "club"])


class Card(Item):
    # rank = Property("rank", lambda x: 0 < x <= 13, int)
    rank = Property(lambda x: True, int)
    suit = Property(["spade", "heart", "club", "diamond"], str)


french = []
for rank, suit in _french_raw:
    french.append(Card(rank=rank, suit=suit))
