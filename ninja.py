from character import Character
import random

class Ninja(Character):

    def __init__(self, name, health, damage, defence, type='human'):
        Character.__init__(self, name, health, damage, defence, type)
        self.dodge_chance = 0.3

    def take_damage(self, damage):
        if random.random() < self.dodge_chance:
            print(f"{self.name} ухилився від атаки!")
        else:
            print(f"{self.name} не зміг ухилитися і отримав {damage} шкоди.")
            Character.take_damage(self, damage)

    def __str__(self):
        return Character.__str__(self) + f'\nШанс ухилитися: {self.dodge_chance * 100}%'
