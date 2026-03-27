# Score categories.
# Change the values as you see fit.

from collections import Counter

YACHT = lambda dice: 50 if len(set(dice)) == 1 else 0
ONES = lambda dice: sum(x for x in dice if x == 1)
TWOS = lambda dice: sum(x for x in dice if x == 2)
THREES = lambda dice: sum(x for x in dice if x == 3)
FOURS = lambda dice: sum(x for x in dice if x == 4)
FIVES = lambda dice: sum(x for x in dice if x == 5)
SIXES = lambda dice: sum(x for x in dice if x == 6)
LITTLE_STRAIGHT = lambda dice: 30 if sorted(dice) == [1,2,3,4,5] else 0
BIG_STRAIGHT = lambda dice: 30 if sorted(dice) == [2,3,4,5,6] else 0
CHOICE = lambda dice: sum(dice)

def FOUR_OF_A_KIND(dice):
    counts = Counter(dice)

    for key, val in counts.items():
        if val >= 4:
            return key * 4
    return 0

def FULL_HOUSE(dice):
    counts = Counter(dice)

    values = counts.values()
    if sorted(values) == [2,3]:
        return sum(dice)
    else:
        return 0
        
def score(dice, category):
    return category(dice)
    

    

    
        
