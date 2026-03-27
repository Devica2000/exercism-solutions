import random

class Character:
    def ability(self):
        rolls = [random.randint(1, 6) for _ in range(4)]
        return sum(sorted(rolls)[1:])
        
    def __init__(self):
        self.num_list = []
        self.final_list = []
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)


def modifier(value):
    modifier = (value - 10)// 2
    return modifier
