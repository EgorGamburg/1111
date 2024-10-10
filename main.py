from character import Character
from paladin import Paladin
from berserk import Berserk
from assassin import Assassin
from samurai import Samurai
from ninja import Ninja
from vampyre import Vampyre
from warlock import Warlock
from arena import Arena

players_list = []

player_1_name = input('Введіть ім\'я першого гравця: ')
player_1_class = input('Введіть клас: ').lower()

if player_1_class == 'paladin':
    player1 = Paladin(player_1_name, 100, 15, 1)
elif player_1_class == 'berserk':
    player1 = Berserk(player_1_name, 150, 20, 2)
elif player_1_class == 'assassin':
    player1 = Assassin(player_1_name, 120, 10, 1)
elif player_1_class == 'samurai':
    player1 = Samurai(player_1_name, 150, 15, 3)
elif player_1_class == 'ninja':
    player1 = Ninja(player_1_name, 100, 20, 2)
elif player_1_class == 'vampyre':
    player1 = Vampyre(player_1_name, 120, 20, 3)
elif player_1_class == 'warlock':
    player1 = Warlock(player_1_name, 150, 15, 2)
else:
    player1 = Character(player_1_name, 100, 10, 0)

print(player1)
players_list.append(player1)

player2 = Paladin('Kakyoin', 100, 15, 1)
player2.show_stats()

while player1.health > 0 and player2.health > 0:
    player1.attack(player2)
    player2.attack(player1)

print(f'\n{player1}\n{player2}\n')