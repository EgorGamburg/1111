from action import Work, Rest

class PersonDied(Exception):
    pass

class Depression(Exception):
    pass

class Bankrupt(Exception):
    pass

class Person:
    max_health = 100  # Максимальне здоров'я
    max_mood = 100    # Максимальний настрій

    def __init__(self, name, health=100, mood=100, money=0):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

    def __str__(self):
        return f"=== {self.name} ===\nЗдоров'я: {self.health}\nНастрій: {self.mood}\nГроші: {self.money} грн"

    def change_state(self, health=0, mood=0, money=0):
        # Оновлюємо поля здоров'я, настрою та грошей
        self.health += health
        self.mood += mood
        self.money += money

        # Перевіряємо на наявність помилок, якщо значення падають нижче 0
        if self.health < 0:
            raise PersonDied(f"{self.name} помер!")
        if self.mood < 0:
            raise Depression(f"{self.name} впав у депресію!")
        if self.money < 0:
            raise Bankrupt(f"{self.name} збанкрутував!")

        # Обмежуємо максимальні значення
        self.health = min(self.health, self.max_health)
        self.mood = min(self.mood, self.max_mood)

    def do(self, action):
        if type(action) == Work:
            money = action.money
            if self.mood > 90:
                money *= 1.1  # 10% більше грошей при настрої більше 90
            self.change_state(health=action.health, mood=action.mood, money=money)
        elif type(action) == Rest:
            mood = action.mood
            if self.health < 40:
                mood *= 0.8  # Настрій додається на 20% менше, якщо здоров'я нижче 40
            self.change_state(health=action.health, mood=mood, money=action.money)
        else:
            self.change_state(health=action.health, mood=action.mood, money=action.money)
