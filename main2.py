from person import Person, PersonDied, Depression, Bankrupt
from action import Action, Work, Rest
import random

people = [
    Person(name='Тарас', money=100, mood=80, health=90),
    Person(name='Олена', money=50, mood=60, health=70),
    Person(name='Іван', money=150, mood=50, health=80)
]

actions = [
    Work(name='Піти на завод', money=50, mood=-10, health=-5),
    Rest(name='Сходити в парк', money=0, mood=20, health=10),
    Action(name='Піти в лікарню', money=-20, mood=-5, health=30)
]

while people:
    for person in people[:]:
        action = random.choice(actions)
        try:
            person.do(action)
            print(f"{person.name} виконав дію: {action.name}")
            print(person)
        except (PersonDied, Depression, Bankrupt) as e:
            print(e)
            people.remove(person)

    if not people:
        print("Всі люди загинули або збанкрутували.")
        break
