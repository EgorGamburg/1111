from character import Character


class Samurai(Character):

    def __init__(self, name, health, damage, defence, type='human'):
        Character.__init__(self, name, health, damage, defence, type)
        self.bonus_multiplier = 1.0
        self.max_multiplier = 1.5
        self.increment = 0.1

    def attack(self, target):
        actual_damage = self.damage * self.bonus_multiplier
        target.take_damage(actual_damage)
        print(f"{self.name} завдав {actual_damage} шкоди!")

        if self.bonus_multiplier < self.max_multiplier:
            self.bonus_multiplier += self.increment
            self.bonus_multiplier = min(self.bonus_multiplier, self.max_multiplier)
        else:
            print(f"{self.name} досяг максимального множника шкоди!")

    def __str__(self):
        return Character.__str__(self) + f'\nМножник шкоди: {self.bonus_multiplier}'
