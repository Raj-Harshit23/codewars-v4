import random
import math

name = "scriptblue"


def moveTo(x, y, Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0] == x:
        return (position[1] < y) * 2 + 1
    if position[1] == y:
        return (position[0] > x) * 2 + 2
    if random.randint(1, 2) == 1:
        return (position[0] > x) * 2 + 2
    else:
        return (position[1] < y) * 2 + 1

def spread(pirate):
    #pirate.setSignal(xdir(1 or -1);ydir(1 or -1);last move(0,1,2,3,4);lastx;lasty;Diagmove(0 or 1);spreadno.(1,2,3,...))
    j, k = pirate.getPosition()
    sigList=pirate.getSignal().split(";")
    t = pirate.getCurrentFrame()
    boundx=pirate.getDimensionX()
    boundy=pirate.getDimensionY()
    dpx,dpy=pirate.getDeployPoint()
    X=j-dpx
    Y=k-dpy
    #####updating list:

    sigList[3]=j
    sigList[4]=k
    psignal=""
    for i in sigList:
        psignal+=str(i)
        if i != "t":
            psignal+=";"
        pirate.setSignal(psignal)
    
    if t<200 :
        if  t<150 and abs(X)<boundx*0.65 and abs(Y)<boundy*0.65 :
            print(t)
            return moveTo(boundx-dpx,boundy-dpy,pirate)
        else:
            if j == boundx-1 :  # If at rightmost edge and moving right
                sigList[0] = "-1"  # Change direction to move left
            elif j == 0 :  # If at leftmost edge and moving left
                sigList[0] = "1"  # Change direction to move right
            if k == boundy-1 :  # If at rightmost edge and moving right
                sigList[1] = "-1"  # Change direction to move left
            elif k == 0 :  # If at leftmost edge and moving left
                sigList[1] = "1"  # Change direction to move right
            dir=[int(sigList[0]),int(sigList[1])]
            psignal=""
            for i in sigList:
                psignal+=str(i)
                if i != "t":
                    psignal+=";"
            pirate.setSignal(psignal)
            # print(pirate.getSignal())

            if abs(X)>abs(Y):
                return moveTo(j+dir[0],k+random.choice([1,-1]),pirate)
            else :
                return moveTo(j+random.choice([1,-1]),k+dir[1],pirate)


            # myline=j+k
            # if j>k:
            #     if(dir[0]>0) :
            #         return moveTo(j+dir[0],k+random.choice([1,-1]),pirate)
            #     else :
            #         if((myline)<boundx) :
            #             return moveTo(j+dir[0],k+random.choice([1,-1]),pirate)
            #         else :
            #             return moveTo(j+random.choice([1,-1]),k+dir[1],pirate)

            # if j<k :
            #     if(dir[1]>0) :
            #         return moveTo(j+random.choice([1,-1]),k+dir[1],pirate)
            #     else :
            #         if((myline)<boundx) :
            #             return moveTo(j+random.choice([1,-1]),k+dir[1],pirate)
            #         else:
            #             return moveTo(j+dir[0],k+random.choice([1,-1]),pirate)
            # if j==k :
            #     if random.randint(1,2)==1 :
            #         if(dir[0]>0) :
            #             return moveTo(j+dir[0],k+random.choice([1,-1]),pirate)
            #         else :
            #             if((myline)<boundx) :
            #                 return moveTo(j+dir[0],k+random.choice([1,-1]),pirate)
            #             else :
            #                 return moveTo(j+random.choice([1,-1]),k+dir[1],pirate)
            #     else:
            #         if(dir[1]>0) :
            #             return moveTo(j+random.choice([1,-1]),k+dir[1],pirate)
            #         else :
            #             if((myline)<boundx) :
            #                 return moveTo(j+random.choice([1,-1]),k+dir[1],pirate)
            #             else:
            #                 return moveTo(j+dir[0],k+random.choice([1,-1]),pirate)
    else :
        if j == boundx-1 :  # If at rightmost edge and moving right
            sigList[0] = "-1"  # Change direction to move left
        elif j == 0 :  # If at leftmost edge and moving left
            sigList[0] = "1"  # Change direction to move right
        if k == boundy-1 :  # If at rightmost edge and moving right
            sigList[1] = "-1"  # Change direction to move left
        elif k == 0 :  # If at leftmost edge and moving left
            sigList[1] = "1"  # Change direction to move right
        dir=[int(sigList[0]),int(sigList[1])]
        psignal=""
        for i in sigList:
            psignal+=str(i)
            if i != "t":
                psignal+=";"
        pirate.setSignal(psignal)

        if abs(X)>abs(Y):
            return moveTo(j+dir[0],k+random.choice([1,-1]),pirate)
        else :
            return moveTo(j+random.choice([1,-1]),k+dir[1],pirate)


        # myline=j+k
        # if j>k:
        #     if(dir[0]>0) :
        #         return moveTo(j+dir[0],k+random.choice([1,-1]),pirate)
        #     else :
        #         if((myline)<boundx) :
        #             return moveTo(j+dir[0],k+random.choice([1,-1]),pirate)
        #         else :
        #             return moveTo(j+random.choice([1,-1]),k+dir[1],pirate)

        # if j<k :
        #     if(dir[1]>0) :
        #         return moveTo(j+random.choice([1,-1]),k+dir[1],pirate)
        #     else :
        #         if((myline)<boundx) :
        #             return moveTo(j+random.choice([1,-1]),k+dir[1],pirate)
        #         else:
        #             return moveTo(j+dir[0],k+random.choice([1,-1]),pirate)
        # if j==k :
        #     if random.randint(1,2)==1 :
        #         if(dir[0]>0) :
        #             return moveTo(j+dir[0],k+random.choice([1,-1]),pirate)
        #         else :
        #             if((myline)<boundx) :
        #                 return moveTo(j+dir[0],k+random.choice([1,-1]),pirate)
        #             else :
        #                 return moveTo(j+random.choice([1,-1]),k+dir[1],pirate)
        #     else:
        #         if(dir[1]>0) :
        #             return moveTo(j+random.choice([1,-1]),k+dir[1],pirate)
        #         else :
        #             if((myline)<boundx) :
        #                 return moveTo(j+random.choice([1,-1]),k+dir[1],pirate)
        #             else:
        #                 return moveTo(j+dir[0],k+random.choice([1,-1]),pirate)
        # return moveTo((boundx-dpx)*math.sin(t/200),(boundy-dpy)*math.cos(t/200),pirate)
        


def ActPirate(pirate):
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    x, y = pirate.getPosition()
    dppx,dppy = pirate.getDeployPoint()
    s = pirate.trackPlayers()
    t=pirate.getCurrentFrame()
    if pirate.getSignal() =="" :
        if(dppx!=0 and dppy==0):
            pirate.setSignal("-1;1;0;0;0;0;0;t")
        if(dppx!=0 and dppy!=0):
            pirate.setSignal("-1;-1;0;0;0;0;0;t")
        if(dppx==0 and dppy==0):
            pirate.setSignal("1;1;0;0;0;0;0;t")
        if(dppx==0 and dppy!=0):
            pirate.setSignal("1;-1;0;0;0;0;0;t")
    
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

    
    if pirate.getTeamSignal() != "" and t>300:
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
    # print(team.getListOfSignals())

    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)
    # print(team.getTeamSignal())
    # print(team.trackPlayers())
    if s:
        island_no = int(s[0])
        signal = l[island_no - 1]
        if signal == "myCaptured":
            team.setTeamSignal("")
