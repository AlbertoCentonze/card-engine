# Card engine
 A game engine for card games that allows to create custom cards

# Motivations behind the project
I always make simulations of card games to find a winning strategy and understand how much luck has an impact in certain situations. I also found in this project a great opportunity to learn about metaclasses and how they work in python

# Structure of the engine
## Item metaclass
You can easily model any type of playing card with the Item metaclass. If you're familiar with dataclasses the approach is really similar
```python
from items import Item, Property

# creating a card representing any french playing card
class FrenchCard(Item):
    # validating with a function the possible attributes
    rank = Property(lambda x: isinstance(x, int) and 0 < x <= 13)
    # validating with list membership
    suit = Property(("spade", "heart", "club", "diamond"))
```
