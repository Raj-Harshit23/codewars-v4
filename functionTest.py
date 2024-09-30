from random import randint 
from numpy import random

name = 'HRsample2'

def moveTo(x , y , Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0] == x:
        return (position[1] < y) * 2 + 1
    if position[1] == y:
        return (position[0] > x) * 2 + 2
    if randint(1, 2) == 1:
        return (position[0] > x) * 2 + 2
    else:
        return (position[1] < y) * 2 + 1

class abcd :
    dir = [1]  # Initialize direction
    dir2 = [1]

def spread(pirate):
    j, k = pirate.getPosition()
    t = pirate.getCurrentFrame()
    boundx=pirate.getDimensionX()
    boundy=pirate.getDimensionY()

    if t<200  :
        if j == boundx-1 and abcd.dir[0] == 1:  # If at rightmost edge and moving right
            abcd.dir[0] = -1  # Change direction to move left
           # print(t)
        elif j == 0 and abcd.dir[0] == -1:  # If at leftmost edge and moving left
            abcd.dir[0] = 1  # Change direction to move right
           # print(t)
        print(t)
        return moveTo(j+abcd.dir[0],k+random.choice([-1,1])+100,pirate)
    # elif '''t<1400 or t>1950''' :
    #     if k == boundy-1 and abcd.dir[0] == 1:  # If at rightmost edge and moving right
    #         abcd.dir[0] = -1  # Change direction to move left
    #        # print(t)
    #     elif k == 0 and abcd.dir[0] == -1:  # If at leftmost edge and moving left
    #         abcd.dir[0] = 1  # Change direction to move right
    #        # print(pirate.getCurrentFrame())
    #     return moveTo(j+random.choice([-1,1]),k+abcd.dir[0],pirate)
    # else :
    #     if k == meriteam[] and abcd.dir[0] == 1:  # If at rightmost edge and moving right
    #         abcd.dir[0] = -1  # Change direction to move left
    #        # print(t)
    #     elif k == 0 and abcd.dir2[0] == -1:  # If at leftmost edge and moving left
    #         abcd.dir2[0] = 1  # Change direction to move right
    #        # print(pirate.getCurrentFrame())
    #         return moveTo(j+abcd.dir[0],k+abcd.dir2[0],pirate)

    
    
def ActPirate(pirate):
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    x, y = pirate.getPosition()
    pirate.setSignal("")
    s = pirate.trackPlayers()
    
    if (
        (up == "island1" and s[0] != "myCaptured")
        or (up == "island2" and s[1] != "myCaptured")
        or (up == "island3" and s[2] != "myCaptured")
    ):
        s = up[-1] + str(x) + "," + str(y - 1)
        pirate.setTeamSignal(s)

    if (
        (down == "island1" and s[0] != "myCaptured")
        or (down == "island2" and s[1] != "myCaptured")
        or (down == "island3" and s[2] != "myCaptured")
    ):
        s = down[-1] + str(x) + "," + str(y + 1)
        pirate.setTeamSignal(s)

    if (
        (left == "island1" and s[0] != "myCaptured")
        or (left == "island2" and s[1] != "myCaptured")
        or (left == "island3" and s[2] != "myCaptured")
    ):
        s = left[-1] + str(x - 1) + "," + str(y)
        pirate.setTeamSignal(s)

    if (
        (right == "island1" and s[0] != "myCaptured")
        or (right == "island2" and s[1] != "myCaptured")
        or (right == "island3" and s[2] != "myCaptured")
    ):
        s = right[-1] + str(x + 1) + "," + str(y)
        pirate.setTeamSignal(s)

    
    if pirate.getTeamSignal() != "" and pirate.getCurrentFrame()>700:
        s = pirate.getTeamSignal()
        l = s.split(",")
        x = int(l[0][1:])
        y = int(l[1])
    
        return moveTo(x, y, pirate)

    else:
        return spread(pirate)
def ActTeam(team):
    l = team.trackPlayers()
    s = team.getTeamSignal()

    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)

    if s:
        island_no = int(s[0])
        signal = l[island_no - 1]
        if signal == "myCaptured":
            team.setTeamSignal("")
