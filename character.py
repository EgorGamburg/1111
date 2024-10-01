class Character:
    name = ''
    health = 100
    damage = 1
    defence = 0
    type = 'human'

    def __init__(self, name, health, damage, defence, type='human'):
        self.name = name
        self.health = health
        self.damage = damage
        self.defence = defence
        self.type = type

    def show_stats(self):
        print(self)

    def __str__(self):
        return f"-- {self.name} --\nЗдоров'я: {self.health}\n" \
               f"Шкода: {self.damage}\nЗахист: {self.defence}\n" \
               f"Тип: {self.type}"


    def take_damage(self, damage):
        self.health = max(self.health - damage, 0)

    def attack(self, target):
        target.take_damage(self.damage)