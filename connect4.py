#!/usr/bin/env python

plots = [
    "\n" * 10,
    "|_ _ _ _ _ _ _|",
    "|_ _ _ _ _ _ _|",
    "|_ _ _ _ _ _ _|",
    "|_ _ _ _ _ _ _|",
    "|_ _ _ _ _ _ _|",
    "|_ _ _ _ _ _ _|",
    "|_ _ _ _ _ _ _|", # -2 bot
    "|_____________|",
    " 1 2 3 4 5 6 7"
    # 1 3 5 7 9 11 13
    "\n \n \n ",
]

def print_board():
    for x in plots:
        print x

def input_to_pos(s):
    s = int(s)
    x = s + s - 1
    return x

def player(turn):
    if turn % 2 == 0:
        return "Player 1 is " + xoro(turn) + ": "
    else:
        return "Player 2 is " + xoro(turn) + ": "

def xoro(turn):
    if turn % 2 == 0:
        return "X"
    else:
        return "O"

print_board()
turn = 0
exit = True

s = raw_input(player(turn))
while s > "7" or s < "1" and exit:
    print s
    if s == "":
        exit = False
    print_board()
    print "Enter A Valid Value Or Exit (Enter)"
    s = raw_input(player(turn))

while s <= "7" and s >= "1" and exit:
    s = int(s)
    i = 3
    while plots[-i][input_to_pos(s)] != "_":
        i += 1

    key = "|"
    j = 1
    while j < 14:
        if j == input_to_pos(s):
            key = key + xoro(turn)
        elif plots[-i][j] == "X":
            key = key + "X"
        elif plots[-i][j] == "O":
            key = key + "O"
        elif j % 2 == 0:
            key = key + " "
        else:
            key = key + "_"
        j += 1

    key = key + "|"
    plots[- i] = key
    turn += 1
    print_board()

    s = raw_input(player(turn))
    while s > "7" or s < "1" and exit:
        if s == "":
            exit = False
        print_board()
        print "Enter A Valid Value Or Exit (Enter)"
        s = raw_input(player(turn))

    if s != "":
        while plots[-9][input_to_pos(s)] != "_":
            print_board()
            s = raw_input("Full Row!\n" + player(turn))
