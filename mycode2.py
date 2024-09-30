from random import randint 
from numpy import random

name = 'chatgpt'

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
    
# def meriteam(team) :
#     boundx=team.getDimensionX()
#     boundy=team.getDimensionY()
class abcd :
    dir = [1]  # Initialize direction
    dir2 = [1]

def spread(pirate):
    j, k = pirate.getPosition()
    t = pirate.getCurrentFrame()

    if t<120 or 500<=t<720 or 900<=t<1200 or 1500<=t<1800 or 2100<=t<2400 or 2700<=t<=3000 :
        if j == 39 and abcd.dir[0] == 1:  # If at rightmost edge and moving right
            abcd.dir[0] = -1  # Change direction to move left
           # print(t)
        elif j == 0 and abcd.dir[0] == -1:  # If at leftmost edge and moving left
            abcd.dir[0] = 1  # Change direction to move right
           # print(t)
        return moveTo(j+abcd.dir[0],k+random.choice([-1,1],p=[0.5+0.85*(k-19.5)/39,0.5-0.85*(k-19.5)/39]),pirate)
    elif '''t<1400 or t>1950''' :
        if k == 39 and abcd.dir[0] == 1:  # If at rightmost edge and moving right
            abcd.dir[0] = -1  # Change direction to move left
           # print(t)
        elif k == 0 and abcd.dir[0] == -1:  # If at leftmost edge and moving left
            abcd.dir[0] = 1  # Change direction to move right
           # print(pirate.getCurrentFrame())
        return moveTo(j+random.choice([-1,1],p=[0.5+0.9*(j-19.5)/39,0.5-0.9*(j-19.5)/39]),k+abcd.dir[0],pirate)
    # else :
    #     if k == 39 and abcd.dir[0] == 1:  # If at rightmost edge and moving right
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
    
    for direction in [up, down, left, right]:
        if direction.startswith("island"):
            island_no = int(direction[-1])
            if s[island_no - 1] != "myCaptured":
                s = direction[-1] + str(x) + "," + str(y)
                pirate.setTeamSignal(s)
                x_diff, y_diff = 0, 0
                if direction == up:
                    y_diff = -1
                elif direction == down:
                    y_diff = 1
                elif direction == left:
                    x_diff = -1
                elif direction == right:
                    x_diff = 1
                return moveTo(x + x_diff, y + y_diff, pirate)
    
    if pirate.getTeamSignal() != "" and pirate.getCurrentFrame() > 800:
        s = pirate.getTeamSignal()
        x, y = map(int, s[1:].split(","))
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
