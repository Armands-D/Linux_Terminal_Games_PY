#!/usr/bin/env python

title = [
    "\n \n"
    "  _______ _        _______           _______",
    " |__   __(_)      |__   __|         |__   __|",
    "    | |   _  ___     | | __ _  ___     | | ___   ___ ",
    "    | |  | |/ __|    | |/ _` |/ __|    | |/ _  !/ _ !",
    "    | |  | | (__     | | (_| | (__     | | (_) |  __/",
    "    |_|  |_|L___|    |_|L__,_|L___|    |_|L___/ L___|",
]

plots = [
    "\n",          # 0
    "   |   |   ", # 1
    "___________", # 2
    "   |   |   ", # 3
    "___________", # 4
    "   |   |   ", # 5g
]


coor = [
    "\n",
    " 1 | 2 | 3",
    " " + "-" * 9,
    " 4 | 5 | 6",
    " " + "-" * 9,
    " 7 | 8 | 9"
]

def print_title():
    for x in title:
        print x

print_title()

def print_plot_cord():
    for x in plots:
        print x
    for y in coor:
        print y

print_plot_cord()

# plots
def row(s):
    if 0 < int(s) and int(s) < 4:
        return int(1)
    elif 3 < int(s) and int(s) < 7:
        return int(3)
    elif 6 < int(s) and int(s) < 10:
        return int(5)

# key
def columb(s):
    if int(s) == 1 or int(s) == 4 or int(s) == 7:
        x = 1
        return x
    elif int(s) == 2 or int(s) == 5 or int(s) == 8:
        x = 5
        return x
    elif int(s) == 3 or int(s) == 6 or int(s) == 9:
        x = 9
        return x

def valplay(player):
    if player % 2 == 0:
        return "Player 1"
    else:
        return "Player 2"

def xoro():
    if player % 2 == 0:
        val = "X"
    else:
        val = "O"
    return val

def winner_con():
    if len(seen) == 9:
        print "\n \n   DRAW!!!"
        win = False
        return win
    elif plots[1][1] == xoro() and plots[1][5] == xoro() and plots[1][9] == xoro():
        print "\n \n" + valplay(player) + "  IS THE WINNER"
        win = False
        return win

    elif plots[3][1] == xoro() and plots[3][5] == xoro() and plots[3][9] == xoro():
        print "\n \n" + valplay(player) + "  IS THE WINNER"
        win = False
        return win

    elif plots[5][1] == xoro() and plots[5][5] == xoro() and plots[5][9] == xoro():
        print "\n \n" + valplay(player) + "  IS THE WINNER"
        win = False
        return win

    elif plots[1][1] == xoro() and plots[3][1] == xoro() and plots[5][1] == xoro():
        print "\n \n" + valplay(player) + "  IS THE WINNER"
        win = False
        return win

    elif plots[1][5] == xoro() and plots[3][5] == xoro() and plots[5][5] == xoro():
        print "\n \n" + valplay(player) + "  IS THE WINNER"
        win = False
        return win

    elif plots[1][9] == xoro() and plots[3][9] == xoro() and plots[5][9] == xoro():
        print "\n \n" + valplay(player) + "  IS THE WINNER"
        win = False
        return win

    elif plots[1][1] == xoro() and plots[3][5] == xoro() and plots[5][9] == xoro():
        print "\n \n" + valplay(player) + "  IS THE WINNER"
        win = False
        return win

    elif plots[5][1] == xoro() and plots[3][5] == xoro() and plots[1][9] == xoro():
        print "\n \n" + valplay(player) + "  IS THE WINNER"
        win = False
        return win

    else:
        win = True
        return win


player = 0
seen = {}
n = 8
win = True

s = raw_input("\n"  + valplay(player) + "  " + xoro() + " : ")
while s >= "0" and s <= "9" and win:
    s = int(s)
    y = row(s)
    x = columb(s)
    i = 0
    key = ""
    if s not in seen:
        while i < len(plots[y]):
            if plots[y][i] == "X":
                key = key + "X"

            elif plots[y][i] == "O":
                key = key + "O"

            elif i == x:
                key = key + xoro()

            elif i == 3 or i == 7:
                key = key + "|"

            else:
                key = key + " "
            i += 1
        plots[y] = key
        seen[s] = True
        print_title()
        print_plot_cord()
        player += 1


    else:
        print_title()
        print_plot_cord()
        print "\n \n Enter A Valid Number"

    player = player - 1
    if winner_con():
        player = player + 1
        s = raw_input("\n" + valplay(player) + "  " + xoro() + " : ")
