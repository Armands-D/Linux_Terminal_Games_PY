import sys
import random
# import os
# clear = lambda: os.system('cls')

from os import system, name 
def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

# Player Object
class Player(object):

    def __init__(self, name):
        self.name = name
        self.health = 30
        self.mana = 1
        self.board = []
        self.hand = []

    def __str__(self):
        b = "BOARD: [\n " + " ".join(self.board) + "]"
        h = "HAND : [\n " + " ".join(self.hand) + "]"
        item1 = "Name: " + self.name
        item2 = "Health: " + str(self.health)
        item3 = "Mana: " + str(self.mana)
        l = ["\n", item1, item2, item3, b, h]
        return "\n".join(l)

    def print_enemy(self):
        b = "BOARD: [\n " + " ".join(self.board) + "]"
        item1 = "Name: " + self.name
        item2 = "Health: " + str(self.health)
        item3 = "Mana: " + str(self.mana)
        l = ["\n", item1, item2, item3, b]
        return "\n".join(l)

    def draw_card(self, cards):
        n = random.randint(0, len(cards) - 1)
        self.hand.append(cards[n].__str__())


# CARD OBJECT
class Card(object):
    bc = []

    def __init__(self, name, health=1, attack=0, mana=0, bat=None):
        self.name = name
        self.health = health
        self.attack = attack
        self.mana = mana
        if bat is not None:
            self.batcry = Card.bc[bat]
        else:
            self.batcry = None

    def __str__(self):
        l = [["Name:" , self.name], ["Attack:", str(self.attack), "Health: ", str(self.health), "Mana: ", str(self.mana)], ["BattleCry", str(self.batcry), "\n"]]
        l1 = [" ".join(n) for n in l]
        return " ".join(l1)

# Card Defining and List 
imp = Card("Lil Imp", health=2, attack=1, mana=1)

cards = [
    imp
]
# Print Board
def print_board(play1, enemy, turn):
    print("TURN ", turn)
    print(Player.print_enemy(enemy))
    print(play1)

# Deal Hand and Define Players
player1 = Player("player1")
player2 = Player("player2")
players = [player1, player2]

while len(player1.hand) != 4:
    player1.draw_card(cards)

while len(player2.hand) != 4:
    player2.draw_card(cards)


# Play Event
player_pick = [True, False][random.randint(0,1)]
turn = 1
while player1.health > 0 and player2.health > 0:
    if player_pick:
        c_player = player1
        n_player = player2
    else:
        c_player = player2
        n_player = player1
    print_board(c_player, n_player, turn)
    player_pick = not player_pick
    s = input("PLACE HOLDER")

    clear()
    turn += 1

#C:/Users/arman/OneDrive/Desktop/DCU/Python/CA117/projects
