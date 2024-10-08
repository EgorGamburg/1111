class Action:
    def __init__(self, name, health=0, mood=0, money=0):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

    def __str__(self):
        return f"Action: {self.name} (Здоров'я: {self.health}, Настрій: {self.mood}, Гроші: {self.money})"

class Work(Action):
    pass

class Rest(Action):
    pass
