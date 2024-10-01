from character import Character
from paladin import Paladin
from berserk import Berserk
from assassin import Assassin
from samurai import Samurai
from ninja import Ninja
from vampyre import Vampyre

player1 = Paladin("Kakyoin", 100, 5, 1)
player2 = Berserk("Avdol", 200, 15, 5)
player3 = Assassin("Diavolo", 80, 10, 2)
player4 = Samurai("Polnareff", 150, 15, 3)
player5 = Ninja("Ryu", 90, 12, 1)
player6 = Vampyre("Dio", 120, 20, 5)

print(player1)
print(player2)
print(player3)
print(player4)
print(player5)
print(player6)

player1.attack(player2)
player2.attack(player1)
player3.attack(player4)
player4.attack(player3)
player5.attack(player6)
player6.attack(player5)

print(f"\n{player1}\n{player2}\n{player3}\n{player4}\n{player5}\n{player6}\n")
