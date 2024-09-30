import random
import math
name = "latest"


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
        if boundx<=50 and boundy<=50 :
            if  t<150 and abs(X)<boundx*0.75 and abs(Y)<boundy*0.75 :
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

    else:
        if  t<150 and abs(X)<boundx*0.65 and abs(Y)<boundy*0.65 :
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

def moveInIsland(pirate):
    move=True
    count=0
    while(move) :
        dice=random.randint(1,4)
        if dice==1:
            newpos=pirate.investigate_up()[0]
            if "island" in newpos:
                move=False
                return 1
        if dice==2:
            newpos=pirate.investigate_right()[0]
            if "island" in newpos:
                move=False
                return 2
        if dice==3:
            newpos=pirate.investigate_down()[0]
            if "island" in newpos:
                move=False
                return 3
        if dice==4:
            newpos=pirate.investigate_left()[0]
            if "island" in newpos:
                move=False
                return 4 
        count+=1                        
        if count>=10:
            break

def defend_island(pirate,island,signal) :#island=1,2,3
    list_wall = signal.split(";")
    if list_wall[11+island]==-1 :
        pass
    else :
        if list_wall[11+island]>=30 :
            if list_wall[14+island]<=20 :
                sendtoprotect(pirate,1)

def sendtoprotect(pirate,island,signal) :
    list_num = signal.split(";")
    if(list_num[14+island]>=20) :
        return None
    else :
        set_sendtoisland(pirate)

def set_sendtoisland(pirate,island,signal):
    list1 = signal.split(";")
    if pirate.getSignal() != "" :
        x,y = pirate.getPosition()
        pirate.setSignal(  )
    else :
        return None

def island_enter(pirate):
    signal=pirate.getTeamSignal()
    arg=pirate.getPosition()
    found=0
    list=signal.split(";")
    for i in list[3:9:2]:
        if i:
            if (int(i) in range(arg[0]-1,arg[0]+2)) and (int(list[list.index(i)+1]) in range(arg[1]-1,arg[1]+2)):
                found=1
    if found==1:
        island=closestIsland(pirate.getPosition(),pirate.getTeamSignal())
        
        
    else:
        if list[3]=="0":
            island=3
        elif list[5]=='0':
            island=5
        else:
            island=7
    list5=pirate.getSignal().split(";")                    
    list5[7]=str(island)
    signal=""
    for i in list5:
           signal+=i
           if i !="t":
                signal+=";"
    pirate.setSignal(signal)     

def pirate_count_update(team):
    sig=team.getTeamSignal()
    list=sig.split(";")
    all_sig=team.getListOfSignals()
    list[12]='0';list[13]='0';list[14]='0'
    for i in all_sig:
        
        list_temp=i.split(";")
        if(len(list_temp))==1:
            continue
        if int(list_temp[7])==3:
            list[12]=str(int(list[12])+1)
        if int(list_temp[7])==5:
            list[13]=str(int(list[13])+1)    
        if int(list_temp[7])==7:
            list[14]=str(int(list[14])+1)   
    signal=""
    for i in list:
           signal+=i
           if i !="t":
                signal+=";"
    team.setTeamSignal(signal)

def assign_duty(pirate,num):
    list=pirate.getSignal().split(";")
    list[8]=str(num)
    signal=""
    for i in list:
           signal+=i
           if i !="t":
                signal+=";"
    pirate.setSignal(signal)
    
def count_pirates(team):
    N=team.getTotalPirates()
    list=team.getTeamSignal().split(";")
    list[15]=N
    signal=""
    for i in list:
           signal+=i
           if i !="t":
                signal+=";"
    team.setTeamSignal(signal)
        
def ActPirate(pirate):
    # complete this function
    #teamsignal=f;deployx;deployy;islx;is1y;is2x;is2y;is3x;is3y;wallstatus_previous;wallstatus_current;modulo;pirates_count1;2;3;totalpir;t
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    x, y = pirate.getPosition()
    dppx,dppy=pirate.getDeployPoint()
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
    if pirate.getSignal() =="" :
            if(dppx!=0 and dppy==0):
                pirate.setSignal("-1;1;0;0;0;0;0;0;2;0;t")
            if(dppx!=0 and dppy!=0):
                pirate.setSignal("-1;-1;0;0;0;0;0;0;2;0;t")
            if(dppx==0 and dppy==0):
                pirate.setSignal("1;1;0;0;0;0;0;0;2;0;t")
            if(dppx==0 and dppy!=0):
                pirate.setSignal("1;-1;0;0;0;0;0;0;2;0;t")    #xdir,ydir,lastmove,lastx,lasty,diag_check,....,island_no,duty,...,t
    ####       
    #### 
          
    #print(pirate.getTeamSignal())
    N=pirate.getCurrentFrame()
    pirate.setTeamSignal(checkWalls(pirate,pirate.getTeamSignal()))

    if(N<300):
        if checkIsland(pirate):
            island=closestIsland(pirate.getPosition(),pirate.getTeamSignal())
            island_index=int((island-3)/2)
            list=pirate.getTeamSignal().split(";")
            if int(list[12+island_index]) <= 5:
                island_enter(pirate)
                assign_duty(pirate,1)
                return moveInIsland(pirate)
        else:
            return spread(pirate)    
     
    else:
        iD=pirate.getID()
        sig=pirate.getTeamSignal()
        list=sig.split(";")
        sig_pir=pirate.getSignal().split(";")
        
        list_count = [int(list[12]),int(list[13]),int(list[14])]
        list_count_sort = sorted(list_count)
        rem_mod5 = (int(pirate.getID())%5)
        if checkIsland(pirate) :
            return moveInIsland(pirate)
        
        
        else :
          
         if rem_mod5==0 or rem_mod5==1 :   
            min_count_island = int(list_count_sort[0])
            island = int(list_count.index(min_count_island)*2+3)
            #island=closestIsland(pirate.getPosition(),pirate.getTeamSignal())
            #if str(island) in list[9]:
            if island==3:
                return moveTo(int(list[3]),int(list[4]),pirate)
            if island==5:
                return moveTo(int(list[5]),int(list[6]),pirate)
            if island==7:
                return moveTo(int(list[7]),int(list[8]),pirate)   
         else:
              
              if int(rem_mod5) == 2 :
                middle_count_island = int(list_count_sort[1])
                island = int(list_count.index(middle_count_island)*2+3)
                  
              #(x,y)=(pirate.getDeployPoint()[0]-int(list[1]),pirate.getDeployPoint()[1]-int(list[2]))
              #island=closestIsland((x,y),pirate.getTeamSignal())
              #if str(island) in list[9]:
                if island==3:
                    return moveTo(int(list[3]),int(list[4]),pirate)
                if island==5:
                    return moveTo(int(list[5]),int(list[6]),pirate)
                if island==7:
                    return moveTo(int(list[7]),int(list[8]),pirate) 
              elif int(rem_mod5)==3 :
                max_count_island = int(list_count_sort[2])
                island = int(list_count.index(max_count_island)*2+3)
                if island==3:
                    return moveTo(int(list[3]),int(list[4]),pirate)
                if island==5:
                    return moveTo(int(list[5]),int(list[6]),pirate)
                if island==7:
                    return moveTo(int(list[7]),int(list[8]),pirate) 
              else :
                  return spread(pirate)    
            
"""            if (int(list[12])< int(N/4)) or (int(list[13])<int(N/4)) or (int(list[14])<int(N/4)):
                isl=closestIsland(pirate.getPosition(),pirate.getSignal())
                index_isl=(isl-3)//2
                if (int(list[12+index_isl])<N//4):
                    assign_duty(pirate,1)
                    return moveTo(int(list[isl]),int(list[isl+1]),pirate)
                list_count=[int(x) for x in list[12:15]]
                min=sorted(list_count)[0]
                index_closest=list.index(str(min))
                index_req=(index_closest-12)*2+3
                assign_duty(pirate,1)
                return moveTo(int(list[index_req]),int(list[index_req+1]),pirate) """
        
                
                            
                      
"""   if checkIsland(pirate):
        if (int(pirate.getID())%2)==0:
               return (moveInIsland(pirate))
        
    if (N<500)or (int(int(pirate.getID())%4)==0):
       return spread(pirate)
    
    else:
        sig= pirate.getTeamSignal()
        list=sig.split(";")
        island=closestIsland(pirate.getPosition(),pirate.getTeamSignal())
        #if str(island) in list[9]:
        if island==3:
                return moveTo(int(list[3]),int(list[4]),pirate)
        if island==5:
                return moveTo(int(list[5]),int(list[6]),pirate)
        if island==7:
                return moveTo(int(list[7]),int(list[8]),pirate)   
        else:
            return spread(pirate)  """
    
def ActTeam(team):
    # complete this function
    #initializing team signal
    
    if team.getTeamSignal()=="" :
        team.setTeamSignal("0;0;0;0;0;0;0;0;0;;;1;0;0;0;t")
    
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
    N=team.getCurrentFrame()
    if (N>1):
     pirate_count_update(team)
    print(team.getTeamSignal())
    print(team.getCurrentFrame())