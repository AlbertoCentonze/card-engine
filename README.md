# Card engine
A game engine for card games that allows to create custom card games.

# Motivations behind the project

I always make card games simulations to find winning strategies and hidden techniques. Creating the whole game from scratch can be quite tedious.

This library was born as an opinionated boilerplate to theoretically create every single card (or in general turn base) game with the minimum effort possible.

I also found in this project a great opportunity to learn about metaclasses, packaging in python and maintaining a whole code ecosystem.

# What can you do with this engine
Here some possible applications for this engine:
* Create your own card game from scratch and play it from your PC
* Run simulations on already existing games (make different play-styles fight between each other, analyze the impact of luck on the game, ecc.)
* Quickly create a working base for more advanced projects (creating a sandbox for AI training, ecc)

## What is working already
* Create playing cards or in general game `Items` effortlessly.
* A dependencies system implementing the Observer design pattern
## What is coming at some point
* Create the different phases of the game with state-machines
* Automatically generate the rules of the game from the code
* Easily create a user interface for the game

# Examples
## Create a class for the poker cards
You can easily model any type of playing card with the Item metaclass. If you're familiar with dataclasses the approach is really similar

```python
from card_engine.items import Item, Property


# creating a card representing any french playing card
class FrenchCard(Item):
    # validating with a function the possible attributes
    rank = Property(lambda x: 0 < x <= 13, int)
    # validating with list membership
    suit = Property(("spade", "heart", "club", "diamond"))
```