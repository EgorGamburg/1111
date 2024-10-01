from character import Character
import random

class Assassin(Character):

    def __init__(self, name, health, damage, defence, type='human'):
        Character.__init__(self, name, health, damage, defence, type)
        self.critical_damage = 1000
        self.critical_chance = 0.2

    def attack(self, target):
        if random.random() < self.critical_chance:
            print(f"{self.name} завдав критичної шкоди {self.critical_damage} одиниць!")
            target.take_damage(self.critical_damage)
        else:
            print(f"{self.name} атакує звичайною шкодою {self.damage}.")
            target.take_damage(self.damage)
