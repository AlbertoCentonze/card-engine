from itertools import product
from items import Item, Property

__french_raw = list(product(range(1, 14), ["heart", "diamond", "spade", "club"]))

class Card(Item):
	rank = Property("rank", lambda x : isinstance(x, int) and x > 0 and x <= 13)
	suit = Property("suit", ["spade", "heart", "club", "diamond"])

french = []
for rank, suit in __french_raw:
	french.append(Card(rank=rank, suit=suit))

print(len(french))