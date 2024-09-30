from random import randint 
from numpy import random

name = 'HRsample'

def moveTo(x , y , Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0] == x:
        return (position[1] < y) * 2 + 1
    if position[1] == y:
        return (position[0] > x) * 2 + 2
    if random.choice([1, 2]) == 1:
        return (position[0] > x) * 2 + 2
    else:
        return (position[1] < y) * 2 + 1

# def moveTo(x , y , Pirate):
#     position = Pirate.getPosition()
#     if position[0] == x and position[1] == y:
#         return 0
#     if position[0] == x:
#         return (position[1] < y) * 2 + 1
#     if position[1] == y:
#         return (position[0] > x) * 2 + 2
#     present_move=1
#     if  present_move == 1:
#         present_move = 2
#         return (position[0] > x) * 2 + 2
#     else:
#         present_move=1
#         return (position[1] < y) * 2 + 1

class abc :
        dir = [1]  # Initialize direction
        dir2 = [1]

def spread(pirate):
    
    j, k = pirate.getPosition()
    t = pirate.getCurrentFrame()
    print(t)
    boundx=pirate.getDimensionX()
    boundy=pirate.getDimensionY()
    dpx,dpy=pirate.getDeployPoint()
    # if (abs(j-dpx)+abs(k-dpy))<15:
    #     print("inside")
    # if t>40 and (abs(j-dpx)+abs(k-dpy))<17 :
    #             # print("Time:",t)
    #     # print(dpx,dpy)
    #     # print(t)

    #     if j == boundx-1 and abc.dir[0] == 1:  # If at rightmost edge and moving right
    #         abc.dir[0] = -1  # Change direction to move left
    #     elif j == 0 and abc.dir[0] == -1:  # If at leftmost edge and moving left
    #         abc.dir[0] = 1  # Change direction to move right
    #     if k == boundy-1 and abc.dir2[0] == 1:  # If at rightmost edge and moving right
    #         abc.dir2[0] = -1  # Change direction to move left
    #        # print(t)
    #     elif k == 0 and abc.dir[0] == -1:  # If at leftmost edge and moving left
    #         abc.dir2[0] = 1  # Change direction to move right
    #     myline=j+k
    #     if j>k:
    #         if(abc.dir[0]>0) :
    #             return moveTo(j+abc.dir[0],k+random.choice([abc.dir2[0],0]),pirate)
    #         else :
    #             if((myline)<boundx) :
    #                 return moveTo(j+abc.dir[0],k+random.choice([abc.dir2[0],0]),pirate)
    #             else :
    #                 return moveTo(j+random.choice([abc.dir[0],0]),k+abc.dir2[0],pirate)

    #     if j<k :
    #         if(abc.dir2[0]>0) :
    #             return moveTo(j+random.choice([abc.dir[0],0]),k+abc.dir2[0],pirate)
    #         else :
    #             if((myline)<boundx) :
    #                 return moveTo(j+random.choice([abc.dir[0],0]),k+abc.dir2[0],pirate)
    #             else:
    #                 return moveTo(j+abc.dir[0],k+random.choice([abc.dir2[0],0]),pirate)
    #     if j==k :
    #         if randint(1,2)==1 :
    #             if(abc.dir[0]>0) :
    #                 return moveTo(j+abc.dir[0],k+random.choice([abc.dir2[0],0]),pirate)
    #             else :
    #                 if((myline)<boundx) :
    #                     return moveTo(j+abc.dir[0],k+random.choice([abc.dir2[0],0]),pirate)
    #                 else :
    #                     return moveTo(j+random.choice([abc.dir[0],0]),k+abc.dir2[0],pirate)
    #         else:
    #             if(abc.dir2[0]>0) :
    #                 return moveTo(j+random.choice([abc.dir[0],0]),k+abc.dir2[0],pirate)
    #             else :
    #                 if((myline)<boundx) :
    #                     return moveTo(j+random.choice([abc.dir[0],0]),k+abc.dir2[0],pirate)
    #                 else:
    #                     return moveTo(j+abc.dir[0],k+random.choice([abc.dir2[0],0]),pirate)
    # if ((t<80 and (abs(j-boundx/2)+abs(k-boundy/2))>8) )  :
    if(t<60):
        if j == boundx-1 and abc.dir[0] == 1:  # If at rightmost edge and moving right
            abc.dir[0] = -1  # Change direction to move left
        elif j == 0 and abc.dir[0] == -1:  # If at leftmost edge and moving left
            abc.dir[0] = 1  # Change direction to move right
        if k == boundy-1 and abc.dir2[0] == 1:  # If at rightmost edge and moving right
            abc.dir2[0] = -1  # Change direction to move left
           # print(t)
        elif k == 0 and abc.dir[0] == -1:  # If at leftmost edge and moving left
            abc.dir2[0] = 1  # Change direction to move right
        print(t)
        return moveTo(j+abc.dir[0],k+abc.dir2[0],pirate)
        


    # if ((t<300 and (abs(j-boundx/2)+abs(k-boundy/2))>10) or (abs(j-dpx))<20 or abs(j-dpy)<20)  :
    if(t<150) or (abs(j-dpx))<15 or abs(j-dpy)<15:
       
        if j == boundx-1 and abc.dir[0] == 1:  # If at rightmost edge and moving right
            abc.dir[0] = -1  # Change direction to move left
        elif j == 0 and abc.dir[0] == -1:  # If at leftmost edge and moving left
            abc.dir[0] = 1  # Change direction to move right
        if k == boundy-1 and abc.dir2[0] == 1:  # If at rightmost edge and moving right
            abc.dir2[0] = -1  # Change direction to move left
           # print(t)
        elif k == 0 and abc.dir[0] == -1:  # If at leftmost edge and moving left
            abc.dir2[0] = 1  # Change direction to move right
        myline=j+k
        if 0<(k-j)<10:
            # print("upar")
            if(abc.dir[0]>0) :
                return moveTo(j+abc.dir[0],k,pirate)
            else :
                # if((myline)<boundx) :
                return moveTo(j+abc.dir[0],k,pirate)
                # else :
                #     return moveTo(j,k+abc.dir2[0],pirate)

        if 0<(j-k)<10 :
            # print("niche")
            if(abc.dir2[0]>0) :
                return moveTo(j,k+abc.dir2[0],pirate)
            else :
                # if((myline)<boundx) :
                return moveTo(j,k+abc.dir2[0],pirate)
                # else:
                #     return moveTo(j+abc.dir[0],k,pirate)
        if j==k :
            if randint(1,2)==1 :
                if(abc.dir[0]>0) :
                    return moveTo(j+abc.dir[0],k,pirate)
                else :
                    # if((myline)<boundx) :
                    return moveTo(j+abc.dir[0],k,pirate)
                    # else :
                    #     return moveTo(j,k+abc.dir2[0],pirate)
            else:
                if(abc.dir2[0]>0) :
                    return moveTo(j,k+abc.dir2[0],pirate)
                else :
                    # if((myline)<boundx) :
                    return moveTo(j,k+abc.dir2[0],pirate)
                    # else:
                    #     return moveTo(j+abc.dir[0],k,pirate)

    
        return moveTo(j+abc.dir[0],k+abc.dir2[0],pirate)
    
    else :
        # print("Time:",t)
        # print(dpx,dpy)
        # print(t)

        if j == boundx-1 and abc.dir[0] == 1:  # If at rightmost edge and moving right
            abc.dir[0] = -1  # Change direction to move left
        elif j == 0 and abc.dir[0] == -1:  # If at leftmost edge and moving left
            abc.dir[0] = 1  # Change direction to move right
        if k == boundy-1 and abc.dir2[0] == 1:  # If at rightmost edge and moving right
            abc.dir2[0] = -1  # Change direction to move left
           # print(t)
        elif k == 0 and abc.dir[0] == -1:  # If at leftmost edge and moving left
            abc.dir2[0] = 1  # Change direction to move right
        myline=j+k
        if j>k:
            if(abc.dir[0]>0) :
                return moveTo(j+abc.dir[0],k+random.choice([abc.dir2[0],0]),pirate)
            else :
                if((myline)<boundx) :
                    return moveTo(j+abc.dir[0],k+random.choice([abc.dir2[0],0]),pirate)
                else :
                    return moveTo(j+random.choice([abc.dir[0],0]),k+abc.dir2[0],pirate)

        if j<k :
            if(abc.dir2[0]>0) :
                return moveTo(j+random.choice([abc.dir[0],0]),k+abc.dir2[0],pirate)
            else :
                if((myline)<boundx) :
                    return moveTo(j+random.choice([abc.dir[0],0]),k+abc.dir2[0],pirate)
                else:
                    return moveTo(j+abc.dir[0],k+random.choice([abc.dir2[0],0]),pirate)
        if j==k :
            if randint(1,2)==1 :
                if(abc.dir[0]>0) :
                    return moveTo(j+abc.dir[0],k+random.choice([abc.dir2[0],0]),pirate)
                else :
                    if((myline)<boundx) :
                        return moveTo(j+abc.dir[0],k+random.choice([abc.dir2[0],0]),pirate)
                    else :
                        return moveTo(j+random.choice([abc.dir[0],0]),k+abc.dir2[0],pirate)
            else:
                if(abc.dir2[0]>0) :
                    return moveTo(j+random.choice([abc.dir[0],0]),k+abc.dir2[0],pirate)
                else :
                    if((myline)<boundx) :
                        return moveTo(j+random.choice([abc.dir[0],0]),k+abc.dir2[0],pirate)
                    else:
                        return moveTo(j+abc.dir[0],k+random.choice([abc.dir2[0],0]),pirate)

    # else :
    #     print("Time:",t)
    #     print(dpx,dpy)

    #     if j == boundx-1 and abc.dir[0] == 1:  # If at rightmost edge and moving right
    #         abc.dir[0] = -1  # Change direction to move left
    #     elif j == 0 and abc.dir[0] == -1:  # If at leftmost edge and moving left
    #         abc.dir[0] = 1  # Change direction to move right
    #     if k == boundy-1 and abc.dir2[0] == 1:  # If at rightmost edge and moving right
    #         abc.dir2[0] = -1  # Change direction to move left
    #        # print(t)
    #     elif k == 0 and abc.dir[0] == -1:  # If at leftmost edge and moving left
    #         abc.dir2[0] = 1  # Change direction to move right
    #     myline=j+k
    #     if j>=k:
    #         if(abc.dir[0]>0) :
    #             return moveTo(j+abc.dir[0],k+random.choice([1,-1]),pirate)
    #         else :
    #             if((myline)<boundx) :
    #                 return moveTo(j+abc.dir[0],k+random.choice([1,-1]),pirate)
    #             else :
    #                 return moveTo(j+random.choice([1,-1]),k+abc.dir2[0],pirate)

    #     if j<k :
    #         if(abc.dir2[0]>0) :
    #             return moveTo(j+random.choice([1,-1]),k+abc.dir2[0],pirate)
    #         else :
    #             if((myline)<boundx) :
    #                 return moveTo(j+random.choice([1,-1]),k+abc.dir2[0],pirate)
    #             else:
    #                 return moveTo(j+abc.dir[0],k+random.choice([1,-1]),pirate)
                

    # if t<150 or 500<=t<720 or 900<=t<1200 or 1500<=t<1800 or 2100<=t<2400 or 2700<=t<=3000 :
    #     if j == boundx-1 and abcd.dir[0] == 1:  # If at rightmost edge and moving right
    #         abcd.dir[0] = -1  # Change direction to move left
    #        # print(t)
    #     elif j == 0 and abcd.dir[0] == -1:  # If at leftmost edge and moving left
    #         abcd.dir[0] = 1  # Change direction to move right
    #        # print(t)
    #     return moveTo(j+abcd.dir[0],k+random.choice([-1,1])+100,pirate)
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

    
    if pirate.getTeamSignal() != "" and pirate.getCurrentFrame()>350:
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
