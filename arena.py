from character import Character
from paladin import Paladin
from berserk import Berserk
from assassin import Assassin
from samurai import Samurai
from ninja import Ninja
from vampyre import Vampyre


class Arena:
    players = []


    def __init__(self, players = ()):
        for player in players:
            self.players.append(player)



    def add_player(self):
        player_name = input('Введіть ім\'я гравця: ')
        player_health = input('Введіть кількість здоров\'я гравця: ')
        player_damage = input('Введіть кількість шкоди гравця: ')
        player_defence = input('Введіть кількість захисту гравця: ')
        player_class = input('Введіть клас: ').lower()

        if player_class == 'paladin':
            self.players.append(Paladin(player_name, player_health, player_damage, player_defence))
        elif player_class == 'berserk':
            self.players.append(Berserk(player_name, player_health, player_damage, player_defence))
        elif player_class == 'assassin':
            self.players.append(Assassin(player_name, player_health, player_damage, player_defence))
        elif player_class == 'samurai':
            self.players.append(Samurai(player_name, player_health, player_damage, player_defence))
        elif player_class == 'ninja':
            self.players.append(Ninja(player_name, player_health, player_damage, player_defence))
        elif player_class == 'vampyre':
            self.players.append(Vampyre(player_name, player_health, player_damage, player_defence))
        else:
            self.players.append(Character(player_name, player_health, player_damage, player_defence))
