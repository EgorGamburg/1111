from character import Character

class Vampyre(Character):

    def __init__(self, name, health, damage, defence, type='undead'):
        Character.__init__(self, name, health, damage, defence, type)
        self.life_steal_percent = 0.1

    def attack(self, target):
        target.take_damage(self.damage)
        health_restored = self.damage * self.life_steal_percent
        self.health = min(self.health + health_restored, 100)  # Здоров'я не більше 100%
        print(f"{self.name} завдав {self.damage} шкоди і відновив {health_restored} здоров'я!")

    def __str__(self):
        return Character.__str__(self) + f'\nВідновлення здоров\'я: {self.life_steal_percent * 100}% від завданої шкоди'
