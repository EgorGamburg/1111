from character import Character

class Warlock(Character):

    def __init__(self, name, health, damage, defence, type='undead'):
        Character.__init__(self, name, health, damage, defence, type)
        self.curse_damage = 5
        self.curse_duration = 3
        self.active_curses = {}

    def attack(self, target):
        target.take_damage(self.damage)
        print(f"{self.name} завдав {self.damage} шкоди {target.name}!")

        self.apply_curse(target)

    def apply_curse(self, target):
        self.active_curses[target.name] = self.curse_duration
        print(f"{self.name} наклав прокляття на {target.name}! {target.name} буде отримувати {self.curse_damage} шкоди протягом {self.curse_duration} ходів.")

    def apply_curse_damage(self):
        for target_name in list(self.active_curses):
            self.active_curses[target_name] -= 1
            print(f"{target_name} отримує {self.curse_damage} шкоди від прокляття!")
            if self.active_curses[target_name] <= 0:
                print(f"Прокляття на {target_name} зникло.")
                del self.active_curses[target_name]

    def __str__(self):
        return Character.__str__(self) + f'\nПрокляття: {self.curse_damage} шкоди протягом {self.curse_duration} ходів'
