from itertools import product
from items import Item, Property

_french_raw = product(range(1, 14), ["heart", "diamond", "spade", "club"])


class Card(Item):
    rank = Property("rank", lambda x: isinstance(x, int) and 0 < x <= 13)
    suit = Property("suit", ["spade", "heart", "club", "diamond"])


french = []
for rank, suit in _french_raw:
    french.append(Card(rank=rank, suit=suit))
