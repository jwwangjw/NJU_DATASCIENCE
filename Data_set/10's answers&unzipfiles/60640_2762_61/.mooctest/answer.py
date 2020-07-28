# -*- coding: utf-8 -*-
facingLetter = ["E","N","W","S"]
testCases = int(input().strip())
while testCases > 0:
    testCases -= 1
    numOfMoves = int(input().strip())
    moveDetails = input().strip().split()

    x = 0
    y = 0
    facing = 1 # 0 = east, 1 = north, 2 = west, 3 = south

    for i in range(numOfMoves):
        turn = moveDetails[2 * i]
        distance = int(moveDetails[2 * i + 1])
        if turn == "D":
            facing += 2
        elif turn == "L":
            facing += 1
        elif turn == "R":
            facing -= 1
        facing %= 4
        if facing == 0:
            x += distance
        elif facing == 2:
            x -= distance
        elif facing == 1:
            y += distance
        else:
            y -= distance

    print(str(int((x ** 2 + y ** 2) ** 0.5)) + " " + facingLetter[facing])
