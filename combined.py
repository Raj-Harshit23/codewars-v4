import random
import math
from numpy import random
name = "script"


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
    # else :
    #     Altmove(position[0],x,y,Pirate)



def moveAway(x, y, Pirate):
    print(2)
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return random.randint(1, 4)
    if random.randint(1, 2) == 1:
        return (position[0] < x) * 2 + 2
    else:
        return (position[1] > y) * 2 + 1

def circleAround(x, y, radius, Pirate, initial="abc", clockwise=True):
    position = Pirate.getPosition();print(1)
    rx = position[0]
    ry = position[1]
    pos = [[x + i, y + radius] for i in range(-1 * radius, radius + 1)]
    pos.extend([[x + radius, y + i] for i in range(radius - 1, -1 * radius - 1, -1)])
    pos.extend([[x + i, y - radius] for i in range(radius - 1, -1 * radius - 1, -1)])
    pos.extend([[x - radius, y + i] for i in range(-1 * radius + 1, radius)])
    if [rx, ry] not in pos: 
        
        #if initial != "abc":
        #    return moveTo(int(initial[0]), int(initial[1]), Pirate)
        if rx in [x + i for i in range(-1 * radius, radius + 1)] and ry in [
            y + i for i in range(-1 * radius, radius + 1)
        ]:
            
            return moveAway(x, y, Pirate)
        else:
            print(7)
            return moveTo(x, y, Pirate)
    else:
        print(2)
        index = pos.index([rx, ry])
        
        return moveTo(
            int(pos[(index + (clockwise * 2) - 1) % len(pos)][0]),
            int(pos[(index + (clockwise * 2) - 1) % len(pos)][1]),
            Pirate,
        )
    
def checkIsland(pirate):
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    if (up[0:-1] == "island" or down[0:-1] == "island") and (left[0:-1] == "island" or right[0:-1] == "island"):
        return True
    else:
        return False

def islandPosition(arg,signal):  #arg=(x,y)
    found=0
    list=signal.split(";")
    for i in list[3:9:2]:
        if i:
            if (i==str(arg[0])) and (list[list.index(i)+1]==str(arg[1])):
                found=1
    if found==1:
        return signal       
        
    else:
        index=0
        for i in range(6):
            if list[3+i]=='0':
                 index= (i+3)
                 break
        if index:
            list[index],list[index+1] =arg     
        signal=""
        for i in list:
           signal+=str(i)
           if i != "t":
                signal+=";" 
        return signal                         
           
def closestIsland(arg,signal): #arg=position of pirate

    list = signal.split(";")
    list1=[int(x) for x in list[3:9:2]]
    if list1!=[0,0,0]:
        dist=[]
        for i in list1:
            if i:
                dist.append(abs(arg[0]-i)+abs(arg[1]-int(list[list.index(str(i))+1])))
        return dist.index(min(dist))*2+3

def centreIsland(pirate):
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    right = pirate.investigate_right()[0]
    left = pirate.investigate_left()[0]
    x, y = pirate.getPosition()
    
    if up[0:-1] == "island" and down[0:-1] == "island" and right[0:-1] == "island" and left[0:-1] == "island":
        return (x,y)   
    if up[0:-1] != "island" and right[0:-1] == "island" and left[0:-1] != "island" and down[0:-1] == "island":
        return (x+1,y+1)
    if up[0:-1] != "island" and right[0:-1] != "island" and left[0:-1] == "island" and down[0:-1] == "island":
        return (x-1,y+1)
    if up[0:-1] == "island" and right[0:-1] != "island" and left[0:-1] == "island" and down[0:-1] != "island":
        return (x-1,y-1)
    if up[0:-1] == "island" and right[0:-1] == "island" and left[0:-1] != "island" and down[0:-1] != "island":
        return (x+1,y-1)
    if up[0:-1] == "island" and down[0:-1] == "island" and left[0:-1] == "island" and right[0:-1] != "island":
        return (x-1,y)
    if up[0:-1] == "island" and down[0:-1] == "island" and left[0:-1] != "island" and right[0:-1] == "island":
        return (x+1,y)
    if up[0:-1] != "island" and down[0:-1] == "island" and left[0:-1] == "island" and right[0:-1] == "island":
        return (x,y+1)
    if up[0:-1] == "island" and down[0:-1] != "island" and left[0:-1] == "island" and right[0:-1] == "island":
        return (x,y-1)
class abc :
    dir = [1]  # Initialize direction
    dir2 = [1]

def spread(pirate):
    
    j, k = pirate.getPosition()
    t = pirate.getCurrentFrame()
    boundx=pirate.getDimensionX()
    boundy=pirate.getDimensionY()
    dpx,dpy=pirate.getDeployPoint()

    # if t>40 and (abs(j-dpx)+abs(k-dpy))<17 :
    #         # print("Time:",t)
    # # print(dpx,dpy)
    # # print(t)

    #     if j == boundx-1 and abc.dir[0] == 1:  # If at rightmost edge and moving right
    #         abc.dir[0] = -1  # Change direction to move left
    #     elif j == 0 and abc.dir[0] == -1:  # If at leftmost edge and moving left
    #         abc.dir[0] = 1  # Change direction to move right
    #     if k == boundy-1 and abc.dir2[0] == 1:  # If at rightmost edge and moving right
    #         abc.dir2[0] = -1  # Change direction to move left
    #         # print(t)
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
    #         if random.randint(1,2)==1 :
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


    if ((t<300 and (abs(j-boundx/2)+abs(k-boundy/2))>12) or (abs(j-dpx)+abs(k-dpy))<21)  :
       
        if j == boundx-1 and abc.dir[0] == 1:  # If at rightmost edge and moving right
            abc.dir[0] = -1  # Change direction to move left
        elif j == 0 and abc.dir[0] == -1:  # If at leftmost edge and moving left
            abc.dir[0] = 1  # Change direction to move right
        if k == boundy-1 and abc.dir2[0] == 1:  # If at rightmost edge and moving right
            abc.dir2[0] = -1  # Change direction to move left
           # print(t)
        elif k == 0 and abc.dir[0] == -1:  # If at leftmost edge and moving left
            abc.dir2[0] = 1  # Change direction to move right
    
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
            if random.randint(1,2)==1 :
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

    # if (abs(j-dpx)+abs(k-dpy))<15:
    #     print("inside")
    # if t>100 and (abs(j-dpx)+abs(k-dpy))<17 :
    #         # print("Time:",t)
    # # print(dpx,dpy)
    # # print(t)

    #     if j == boundx-1 and abc.dir[0] == 1:  # If at rightmost edge and moving right
    #         abc.dir[0] = -1  # Change direction to move left
    #     elif j == 0 and abc.dir[0] == -1:  # If at leftmost edge and moving left
    #         abc.dir[0] = 1  # Change direction to move right
    #     if k == boundy-1 and abc.dir2[0] == 1:  # If at rightmost edge and moving right
    #         abc.dir2[0] = -1  # Change direction to move left
    #         # print(t)
    #     elif k == 0 and abc.dir[0] == -1:  # If at leftmost edge and moving left
    #         abc.dir2[0] = 1  # Change direction to move right
    #     myline=j+k
    #     if j>k:
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
    #     if j==k :
    #         if random.randint(1,2)==1 :
    #             if(abc.dir[0]>0) :
    #                 return moveTo(j+abc.dir[0],k+random.choice([1,-1]),pirate)
    #             else :
    #                 if((myline)<boundx) :
    #                     return moveTo(j+abc.dir[0],k+random.choice([1,-1]),pirate)
    #                 else :
    #                     return moveTo(j+random.choice([1,-1]),k+abc.dir2[0],pirate)
    #         else:
    #             if(abc.dir2[0]>0) :
    #                 return moveTo(j+random.choice([1,-1]),k+abc.dir2[0],pirate)
    #             else :
    #                 if((myline)<boundx) :
    #                     return moveTo(j+random.choice([1,-1]),k+abc.dir2[0],pirate)
    #                 else:
    #                     return moveTo(j+abc.dir[0],k+random.choice([1,-1]),pirate)


    # if (t<200 and (abs(j-boundx/2)+abs(k-boundy/2))>(19-t/20) or (abs(j-dpx)+abs(k-dpy))<20)  :
       
    #     if j == boundx-1 and abc.dir[0] == 1:  # If at rightmost edge and moving right
    #         abc.dir[0] = -1  # Change direction to move left
    #     elif j == 0 and abc.dir[0] == -1:  # If at leftmost edge and moving left
    #         abc.dir[0] = 1  # Change direction to move right
    #     if k == boundy-1 and abc.dir2[0] == 1:  # If at rightmost edge and moving right
    #         abc.dir2[0] = -1  # Change direction to move left
    #        # print(t)
    #     elif k == 0 and abc.dir[0] == -1:  # If at leftmost edge and moving left
    #         abc.dir2[0] = 1  # Change direction to move right

    #     return moveTo(j+abc.dir[0],k+abc.dir2[0],pirate)
    
    # else :
    #     # print("Time:",t)
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
    #             return moveTo(j+abc.dir[0],k+random.choice([1,-1]),pirate)
    #         else :
    #             if((myline)<boundx) :
    #                 return moveTo(j+abc.dir[0],k+random.choice([1,-1]),pirate)
    #             else :
    #                 return moveTo(j+random.choice([1,-1]),k+abc.dir2[0],pirate)

    #     if j<k :
    #         if(abc.dir2[0]>0) :
    #              return moveTo(j+random.choice([1,-1]),k+abc.dir2[0],pirate)
    #         else :
    #             if((myline)<boundx) :
    #                  return moveTo(j+random.choice([1,-1]),k+abc.dir2[0],pirate)
    #             else:
    #                 return moveTo(j+abc.dir[0],k+random.choice([1,-1]),pirate)
    #     if j==k :
    #         if random.randint(1,2)==1 :
    #             if(abc.dir[0]>0) :
    #                 return moveTo(j+abc.dir[0],k+random.choice([1,-1]),pirate)
    #             else :
    #                 if((myline)<boundx) :
    #                     return moveTo(j+abc.dir[0],k+random.choice([1,-1]),pirate)
    #                 else :
    #                      return moveTo(j+random.choice([1,-1]),k+abc.dir2[0],pirate)
    #         else:
    #             if(abc.dir2[0]>0) :
    #                  return moveTo(j+random.choice([1,-1]),k+abc.dir2[0],pirate)
    #             else :
    #                 if((myline)<boundx) :
    #                      return moveTo(j+random.choice([1,-1]),k+abc.dir2[0],pirate)
    #                 else:
    #                     return moveTo(j+abc.dir[0],k+random.choice([1,-1]),pirate)
    #        # print(pirate.getCurrentFrame())
    #         return moveTo(j+abcd.dir[0],k+abcd.dir2[0],pirate)
def checkWalls(pirate,signal):
    list=signal.split(";")
    status=list[10]
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    right = pirate.investigate_right()[0]
    left = pirate.investigate_left()[0]
    curr=pirate.investigate_current()[0]
    ne=pirate.investigate_ne()[0]
    nw=pirate.investigate_nw()[0]
    se=pirate.investigate_se()[0]
    sw=pirate.investigate_se()[0]
    if up=="wall" or down=="wall" or right=="wall" or left=="wall" or curr=="wall" or ne =="wall" or nw=="wall" or se=="wall" or sw=="wall":
       y = closestIsland(pirate.getPosition(),signal) 
       if (str(y) not in status) and (y != None) :
           list[10]+=str(y)
           signal=''
           for i in list:
            signal+=str(i)
            if i != "t":
                signal+=";" 
    return signal   
                      

def ActPirate(pirate):
    # complete this function
    #teamsignal=f;deployx;deployy;islx;is1y;is2x;is2y;is3x;is3y;wallstatus_previous;wallstatus_current;modulo;isl3;isl5;isl7;t
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    x, y = pirate.getPosition()
    t=pirate.getTeamSignal()
    list = t.split(";")
    if t[0]=="0":
        list[0]="1";list[1]=str(x);list[2]=str(y)
        signal=""
        for i in list:
           signal+=i
           if i != "t":
                signal+=";"
        pirate.setTeamSignal(signal)       
    if list[7]=='0': 
        if checkIsland(pirate):
           pirate.setTeamSignal(islandPosition(centreIsland(pirate),pirate.getTeamSignal()))
    sig= pirate.getTeamSignal()
    list=sig.split(";")
    list[11]=str(1-int(list[11]))
    signal=""
    for i in list:
           signal+=i
           if i !="t":
                signal+=";"
    pirate.setTeamSignal(signal) 
    
    ####       
    #### 
          
    print(pirate.getTeamSignal())
    N=pirate.getCurrentFrame()
    
    if checkIsland(pirate):
            sig= pirate.getTeamSignal()
            list=sig.split(";")
            if list[11]:
               return 0
        
    if (N<300):
       pirate.setTeamSignal(checkWalls(pirate,pirate.getTeamSignal()))
       return spread(pirate)
    
    else:
        sig= pirate.getTeamSignal()
        list=sig.split(";")
        island=closestIsland(pirate.getPosition(),pirate.getTeamSignal())
        if str(island) in list[9]:
            if island==3:
                return moveTo(int(list[3]),int(list[4]),pirate)
            if island==5:
                return moveTo(int(list[5]),int(list[6]),pirate)
            if island==7:
                return moveTo(int(list[7]),int(list[8]),pirate)   
        else:
            return spread(pirate)


def ActTeam(team):
    # complete this function
    #initializing team signal
    
    if team.getTeamSignal()=="" :
        team.setTeamSignal("0;0;0;0;0;0;0;0;0;;;1;t")
    
    l = team.trackPlayers()
    s = team.getTeamSignal() 
    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)
    t =  team.getTeamSignal()
    print(t)
    list = t.split(";")
    list[9]=list[10]
    list[10]=""
    signal=''
    for i in list:
            signal+=str(i)
            if (i != "t"):
                signal+=";"
   
    team.setTeamSignal(signal)
    print(team.getTeamSignal())