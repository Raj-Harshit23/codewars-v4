import random
import numpy as np
import re
import math

#from ActPirate import *

name = "myscript"

class Task_Enum:
	def __init__(self):
		self.RANDOM = 1
		self.CIRCLE=2
		self.MV_TO=4
		self.RND_CNF=8

Task = Task_Enum()

# island_locations(x11x12y11y12x21x22y21y22...)x:y:task:probability,…
#   Random: no params
#   Move-to: no params
#   Circle: no params, default radius = 2
#   Random-confined: no params, default h,w = 3
def ReadTeamSignal(signal):
	list = []
	if(signal == ""):
		return ([(-1,-1),(-1,-1),(-1,-1)],[])
	islandLocations=[(int(signal[:2]),int(signal[2:4])), (int(signal[4:6]), int(signal[6:8])), ( int(signal[8:10]), int(signal[10:12]) )]
	signalList = signal[12:].split(",")
	if(signalList == ['']):	return (islandLocations, [])
	for sig in signalList:
		sigParams = sig.split(':')
		x = int(sigParams[0])
		y = int(sigParams[1])
		p = float(sigParams[3])
		t = int(sigParams[2])

		list.append((x,y,t,p))

	return (islandLocations,list)

def WriteTeamSignal(islandLocations, list):
	string = ""
	for x,y in islandLocations:
		x = str(x)
		y = str(y)
		if(len(x) == 1):
			x = "0" + x
		if(len(y)==1):
			y = "0" + y
		string = string + x + y
	for target in list:
		x=target[0]
		y=target[1]
		task=target[2]
		p=int(target[3])
		string = string + f"{x}:{y}:{task}:{p},"
	if(string[-1] == ','):	string = string[:-1]
	return string

#return True if pirate is on an island
def checkIsland(pirate):
    up = pirate.investigate_up()
    down = pirate.investigate_down()
    left = pirate.investigate_left()
    right = pirate.investigate_right()
    if (up[0:-1] == "island" or down[0:-1] == "island") and (left[0:-1] == "island" or right[0:-1] == "island"):
        return True
    else:
        return False

def ReadPirateSignal(signal):
	if(signal == ""):
		signalList = [-1,-1,-1,-1,0,-1,-1,-1,-1,0,'']
		prevMoves = []
		return signalList, prevMoves

	signalList= signal.split(":")
	signalList[0]=int(float(signalList[0]))
	signalList[1]=int(float(signalList[1]))
	signalList[2]=int(float(signalList[2]))
	signalList[3]=int(float(signalList[3]))
	signalList[4]=int(float(signalList[4]))
	signalList[5]=int(float(signalList[5]))
	signalList[6]=int(float(signalList[6]))
	signalList[7]=int(float(signalList[7]))
	signalList[8]=int(float(signalList[8]))
	signalList[9]=int(signalList[9])

	stringOfPrevMoves=signalList[10]
   	# first extract this string into list.
	listOfPrevMoves=list(stringOfPrevMoves)
	
	x=signalList[0]
	y=signalList[1]
	listContainingPrevLocationsX=[0 for i in range(len(listOfPrevMoves))]
	listContainingPrevLocationsY=[0 for i in range(len(listOfPrevMoves))]
	for i in range(len(listOfPrevMoves)):
		if i==0:
			if listOfPrevMoves[i]=='u':
				listContainingPrevLocationsX[i]=x
				listContainingPrevLocationsY[i]=y+1
			elif listOfPrevMoves[i]=='d':
				listContainingPrevLocationsX[i]=x
				listContainingPrevLocationsY[i]=y-1

			elif listOfPrevMoves[i]=='l':
				listContainingPrevLocationsX[i]=x+1
				listContainingPrevLocationsY[i]=y

			elif listOfPrevMoves[i]=='r':
				listContainingPrevLocationsX[i]=x-1
				listContainingPrevLocationsY[i]=y

			else:
				pass
		else:
			if listOfPrevMoves[i]=='u':
				listContainingPrevLocationsX[i]=listContainingPrevLocationsX[i-1]
				listContainingPrevLocationsY[i]=listContainingPrevLocationsY[i-1]+1

			elif listOfPrevMoves[i]=='u':
				listContainingPrevLocationsX[i]=listContainingPrevLocationsX[i-1]
				listContainingPrevLocationsY[i]=listContainingPrevLocationsY[i-1]-1

			elif listOfPrevMoves[i]=='u':
				listContainingPrevLocationsX[i]=listContainingPrevLocationsX[i-1]+1
				listContainingPrevLocationsY[i]=listContainingPrevLocationsY[i-1]

			elif listOfPrevMoves[i]=='u':
				listContainingPrevLocationsX[i]=listContainingPrevLocationsX[i-1]-1
				listContainingPrevLocationsY[i]=listContainingPrevLocationsY[i-1]
			else:
				pass
	listContainingPrevLocations=list(zip(listContainingPrevLocationsX,listContainingPrevLocationsY))
	return signalList,listContainingPrevLocations
# So finally the pirate signal returns the following:
	# coordinates of the pirate, coordinates of where the pirate is headed towards
	# target task
	# island number if found otherwise -1
	# island coordinates if found otherwise -1
	# wallStatus if found 
	# wallStatus: 0 if no wall found
	# 1 if we are capturing the island
	# 2 if opponent is capturing the island
##Pirate Signal Format:
##"{x}:{y}:{tx}:{ty}:{targetTask}:{island_indice}:{island_x}:{island_y}:{wallStatus}:{enemyStatus}:{prevMoves}
def sendPirateSignal(pirate,tx,ty,targetTask,currentMove,prevSignal):
	prevSignalList,_=ReadPirateSignal(prevSignal)
	#prevCoorTuple not used here.
	coor=pirate.getPosition()
	x=coor[0]
	y=coor[1]

	if(currentMove == 1):
		currentMove='u'
	elif(currentMove == 2):
		currentMove='r'
	elif(currentMove == 3):
		currentMove = 'd'
	elif(currentMove==4):
		currentMove='l'
	else:
		currentMove = ''

	prevMovesRelString=prevSignalList[10]
	prevMovesRelString=currentMove+prevMovesRelString

	#if not found, default is -1
	island_indice = -1
	#done
	island_name = -1
	#done
	island_x = -1
	#done
	island_y = -1
	#done
	island_status_opp_view = ''
	#done
	island_status_my_view = ''
	#done

	up=pirate.investigate_up()
	down=pirate.investigate_down()
	left=pirate.investigate_left()
	right=pirate.investigate_right()
	sw=pirate.investigate_sw()
	nw=pirate.investigate_nw()
	ne=pirate.investigate_ne()
	se=pirate.investigate_se()

	##searching for an empty island.
	##if we find an empty island, we will call send that signal with coordinates.
	islandFound=(up[0]=='island1' or up[0]=='island2' or up[0]=='island3' or down[0]=='island1' or down[0]=='island2' or down[0]=='island3' or left[0]=='island1' or left[0]=='island2' or left[0]=='island3' or right[0]=='island1' or right[0]=='island2' or right[0]=='island3')
	if(islandFound):
	#checking for islands::
		if(up[0]=='island1' or up[0]=='island2' or up[0]=='island3'):
			island_name=up[0]
			if(ne[0]==up[0] and nw[0]!=up[0] and down[0]!=up[0]):
				island_x=x+1
				island_y=y-2
			
			if(ne[0]==up[0] and nw[0]==up[0] and down[0]!=up[0]):
				island_x=x
				island_y=y-2

			if(ne[0]!=up[0] and nw[0]==up[0] and down[0]!=up[0]):
				island_x=x-1
				island_y=y-2

			if(nw[0]==up[0] and left[0]==up[0] and ne[0]!=up[0] and right[0]!=up[0] and down[0]!=up[0]):
				island_x=x-1
				island_y=y-1

			if(nw[0]==up[0] and left[0]==up[0] and ne[0]==up[0] and right[0]==up[0] and down[0]!=up[0]):
				island_x=x
				island_y=y-1

			if(down[0]!=up[0] and right[0]==up[0] and ne[0]==up[0] and nw[0]!=up[0] and left[0]!=up[0]):
				island_x=x+1
				island_y=y-1

			if(nw[0]==up[0] and left[0]==up[0] and ne[0]!=up[0] and right[0]!=up[0] and down[0]==up[0]):
				island_x=x-1
				island_y=y

			if(nw[0]==up[0] and left[0]==up[0] and ne[0]==up[0] and right[0]==up[0] and down[0]==up[0]):
				island_x=x
				island_y=y

			if(down[0]==up[0] and right[0]==up[0] and ne[0]==up[0] and nw[0]!=up[0] and left[0]!=up[0]):
				island_x=x+1
				island_y=y

			island_indice=int(up[0][6])
			island_status_my_view=(pirate.trackPlayers())[island_indice-1]
			island_status_opp_view=(pirate.trackPlayers())[island_indice-1+3]


		elif(down[0]=='island1' or down[0]=='island2' or down[0]=='island3'):
			island_name=down[0]
			if(se[0]==down[0] and sw[0]==down[0]):
				island_x=x
				island_y=y+2
			
			if(se[0]==down[0] and sw[0]!=down[0]):
				island_x=x+1
				island_y=y+2

			if(sw[0]==down[0] and se[0]!=down[0]):
				island_x=x-1
				island_y=y+2

			if(up[0]!=down[0] and left[0]==down[0] and sw[0]==down[0] and right[0]!=down[0] and se[0]!=down[0]):
				island_x=x-1
				island_y=y+1

			if(up[0]!=down[0] and left[0]==down[0] and sw[0]==down[0] and right[0]==down[0] and se[0]==down[0]):
				island_x=x
				island_y=y+1

			if(up[0]!=down[0] and left[0]!=down[0] and sw[0]!=down[0] and right[0]==down[0] and se[0]==down[0]):
				island_x=x+1
				island_y=y+1


			island_indice=int(down[0][6])
			island_status_my_view=(pirate.trackPlayers())[island_indice-1]
			island_status_opp_view=(pirate.trackPlayers())[island_indice-1+3]


		elif(left[0]=='island1' or left[0]=='island2' or left[0]=='island3'):
			island_name=left[0]
			if(sw[0]==left[0] and nw[0]!=left[0]):
				island_x=x-2
				island_y=y+1
			
			if(nw[0]==up[0] and sw[0]==up[0]):
				island_x=x-2
				island_y=y


			if(sw[0]!=up[0] and nw[0]==up[0]):
				island_x=x-2
				island_y=y-1

			island_indice=int(left[0][6])
			island_status_my_view=(pirate.trackPlayers())[island_indice-1]
			island_status_opp_view=(pirate.trackPlayers())[island_indice-1+3]

		elif(right[0]=='island1' or right[0]=='island2' or right[0]=='island3'):
			island_name=right[0]
			if(ne[0]==right[0] and se[0]!=right[0]):
				island_x=x+2
				island_y=y-1
			
			if(ne[0]==right[0] and se[0]==right[0]):
				island_x=x+2
				island_y=y


			if(ne[0]!=right[0] and se[0]==right[0]):
				island_x=x+2
				island_y=y+1


			island_indice=int(right[0][6])
			island_status_my_view=(pirate.trackPlayers())[island_indice-1]
			island_status_opp_view=(pirate.trackPlayers())[island_indice-1+3]

		elif(ne[0]=='island1' or ne[0]=='island2' or ne[0]=='island3'):
			island_name=ne[0]
			if(right[0]!=ne[0] and up[0]!=ne[0]):
				island_x=x+1
				island_y=y-1

			island_indice=int(ne[0][6])
			island_status_my_view=(pirate.trackPlayers())[island_indice-1]
			island_status_opp_view=(pirate.trackPlayers())[island_indice-1+3]

		elif(nw[0]=='island1' or nw[0]=='island2' or nw[0]=='island3'):
			island_name=nw[0]
			if(left[0]!=nw[0] and up[0]!=nw[0]):
				island_x=x-1
				island_y=y-1

			island_indice=int(nw[0][6])
			island_status_my_view=(pirate.trackPlayers())[island_indice-1]
			island_status_opp_view=(pirate.trackPlayers())[island_indice-1+3]

		elif(se[0]=='island1' or se[0]=='island2' or se[0]=='island3'):
			island_name=se[0]
			if(right[0]!=se[0] and down[0]!=se[0]):
				island_x=x+1
				island_y=y+1

			island_indice=int(se[0][6])
			island_status_my_view=(pirate.trackPlayers())[island_indice-1]
			island_status_opp_view=(pirate.trackPlayers())[island_indice-1+3]

		elif(sw[0]=='island1' or sw[0]=='island2' or sw[0]=='island3'):
			island_name=sw[0]
			if(left[0]!=sw[0] and down[0]!=sw[0]):
				island_x=x-1
				island_y=y+1

			island_indice=int(sw[0][6])
			island_status_my_view=(pirate.trackPlayers())[island_indice-1]
			island_status_opp_view=(pirate.trackPlayers())[island_indice-1+3]
	else:
		island_indice=-1
		island_x=-1
		island_y=-1
		island_status_my_view=''
		island_status_opp_view=''
## now finding the status of walls
## walls can be on opponent islands or on our islands
## parameters: wall on opponent island or wall on our island
##return 0 if no wall found
## return 1 if wall found and island is ours capturing
## return 2 if wall found and island is opponents capturing
	 
	###obviously if wall is found, island must be there, which is being captured.
	wallFound=(up[0]=='wall' or down[0]=='wall' or right[0]=='wall' or left[0]=='wall')
	wallStatus = 0
	if(wallFound):
		if island_status_my_view=='myCapturing' or (island_status_my_view=='myCaptured' and island_status_opp_view!='oppCapturing'):
			wallStatus=1
		elif island_status_opp_view=='oppCapturing' or (island_status_opp_view=='oppCaptured' and island_status_my_view!='myCapturing'):
			wallStatus=2
	else:
		wallStatus=0

	#enemy: 0 or 1	
	enemyFound=int(up[1]=='enemy' or down[1]=='enemy' or right[1]=='enemy' or left[1]=='enemy' or sw[1]=='enemy' or se[1]=='enemy' or ne[1]=='enemy' or nw[1]=='enemy')
	enemyStatus=enemyFound



#tx, ty, targetTask
	#pirateSig=x+":"+y+":"+tx+":"+ty+":"+targetTask+":"+island_indice+":"+island_x+":"+island_y+":"+wallStatus
	#pirateSig=f"{int(x)}:{int(y)}:{int(tx)}:{int(ty)}:{int(targetTask)}:{int(island_indice)}:{int(island_x)}:{int(island_y)}:{int(wallStatus)}:{int(enemyStatus)}"
	# So finally the pirate signal returns the following:
	# coordinates of the pirate, coordinates of where the pirate is headed towards
	# target task
	# island number if found otherwise -1
	# island coordinates if found otherwise -1
	# wallStatus if found
	# wallStatus: -1 if no wall found
	# 1 if we are capturing the island
	# 2 if opponent is capturing the island
	####print(pirateSig)
	pirateSig=f"{x}:{y}:{tx}:{ty}:{targetTask}:{island_indice}:{island_x}:{island_y}:{wallStatus}:{enemyStatus}:{prevMovesRelString}"
	
	pirateSig = pirateSig[:99]
	return pirateSig

def visited(x, y, prevMoves):
	return any((a, b) == (x, y) for a, b in prevMoves)

def MoveTo(x, y, tx, ty, pirate, direct=False, prevMoves= []):
	dx = tx - x
	dy = ty - y
	d = abs(dx)+abs(dy)
	if dx==0 and dy==0:
		return 0
	# sqaure 
	if d < 5:
		direct= True
	
	#direct
	if (direct):
		if dx==0:
			if pirate.investigate_up()[0] == "wall" or pirate.investigate_down()[0] == "wall":
				return 2
			else:
				return (3 if dy>0 else 1)
		
		elif dy==0:
			if pirate.investigate_left()[0] == "wall" or pirate.investigate_right()[0] == "wall":
				return 1
			else:
				return (2 if dy>0 else 4)
		else :
			r = random.random()
			if(dx>0 and dy>0):
				if pirate.investigate_down()[0] == "wall":
					return 2
				if pirate.investigate_right()[0] == "wall":
					return 3
				else:	
					return (3 if r>=0.5 else 2)
			elif(dx<0 and dy>0):
				if pirate.investigate_down()[0] == "wall":
					return 4
				if pirate.investigate_left()[0] == "wall":
					return 3
				else:
					return (3 if r>=0.5 else 4)
			elif(dx>0 and dy<0):
				if pirate.investigate_up()[0] == "wall":
					return 2
				if pirate.investigate_right()[0] == "wall":
					return 1
				else:
					return (1 if r>=0.5 else 2)
			else:
				if pirate.investigate_up()[0] == "wall":
					return 4
				if pirate.investigate_left()[0] == "wall":
					return 1
				else:
					return (1 if r>=0.5 else 4)
			
	else: 
		up,down,left,right = 1,1,1,1
		if (dx==0):
			up=down=0
			if dy>0: down = dy
			else: up = dy
			right= math.sqrt(abs(dy))
			left = math.sqrt(abs(dy))
			if visited(x,y+1,prevMoves): right = 0
			if visited(x,y-1,prevMoves): left = 0

		elif (dy==0):
			left=right=0
			if dx>0: right = dx
			else: left = dx
			up= math.sqrt(abs(dx))
			down = math.sqrt(abs(dx))
			if visited(x,y+1,prevMoves): down = 0
			if visited(x,y-1,prevMoves): up = 0

		else:
			if(dx>0 and dy>0):
				down= dy
				up= 1/dy
				right= dx
				left= 1/dx
				if visited(x-1, y, prevMoves): left = 0
				if visited(x+1, y, prevMoves): right = 1
				if visited(x, y-1, prevMoves): up = 0
				if visited(x, y+1, prevMoves): down = 1

			elif(dx<0 and dy>0):
				down= dy
				up= 1/dy
				right= -1/dx
				left= -dx
				if visited(x-1, y, prevMoves): left = 1
				if visited(x+1, y, prevMoves): right = 0
				if visited(x, y-1, prevMoves): up = 0
				if visited(x, y+1, prevMoves): down = 1

			elif(dx>0 and dy<0):
				down= -1/dy
				up= -dy
				right= dx
				left= 1/dx
				if visited(x-1, y, prevMoves): left = 0
				if visited(x+1, y, prevMoves): right = 1
				if visited(x, y-1, prevMoves): up = 1
				if visited(x, y+1, prevMoves): down = 0
				
			else:
				down= -1/dy
				up= -dy
				right= -1/dx
				left= -dx
				if visited(x-1, y, prevMoves): left = 1
				if visited(x+1, y, prevMoves): right = 0
				if visited(x, y-1, prevMoves): up = 1
				if visited(x, y+1, prevMoves): down = 0

		####print(up, down, right, left)
		if pirate.investigate_up()[0] == "wall":
			up = 0
		elif pirate.investigate_down()[0] == "wall":
			down = 0
		elif pirate.investigate_left()[0] == "wall":
			left = 0
		elif pirate.investigate_right()[0] == "wall":
			right = 0
		else :
			pass
			
		dM= up + down + left + right
		r= random.random() * dM
		if r < up: 
			return 1
		elif r < up + down: 
			return 3
		elif r < up + down +left : 
			return 4
		else : 
			return 2

def circleAround(x, y, radius, Pirate):
	px,py = Pirate.getPosition()
	#inside
	if (inRect(px,py,x-radius+1, y-radius+1,2*radius-1,2*radius-1)):
		pts = [
			(px, y-radius),
			(px, y+radius),
			(x+radius, py),
			(x-radius, py)
		]
		dists = [(abs(px-pt[0])+abs(py-pt[1])) for pt in pts]
		dst = pts[np.argmin(dists)]
		#return MoveTo(px,py,x,y,direct=True)
		return RandomMove(px,py,Pirate,x,y,confine=2*radius+1)
	#on circle
	elif (inRect(px,py,x-radius, y-radius,2*radius+1,2*radius+1)):
		if(px == x-radius):
			if(inRect(px,py-1,x-radius, y-radius,2*radius+1,2*radius+1)):
				return MoveTo(px,py,px,py-1,Pirate,  direct=True)
			else:
				return MoveTo(px,py,px+1,py,Pirate, direct=True)
		elif(py == y-radius):
			if(inRect(px+1,py,x-radius, y-radius,2*radius+1,2*radius+1)):
				return MoveTo(px,py,px+1,py,Pirate,  direct=True)
			else:
				return MoveTo(px,py,px,py+1,Pirate, direct=True)
		elif(px == x+radius):
			if(inRect(px,py+1,x-radius, y-radius,2*radius+1,2*radius+1)):
				return MoveTo(px,py,px,py+1,Pirate,  direct=True)
			else:
				return MoveTo(px,py,px-1,py,Pirate, direct=True)
		elif(py == y+radius):
			if(inRect(px-1,py,x-radius, y-radius,2*radius+1,2*radius+1)):
				return MoveTo(px,py,px-1,py,Pirate,  direct=True)
			else:
				return MoveTo(px,py,px,py-1,Pirate, direct=True)
			
	else:
		return MoveTo(px,py,x,y,Pirate, direct=True)

def RandomMove(x, y,pirate, tx=None, ty=None, confine=None, prevMoves = [], mapDim = 64):
	up = 1
	down = 1
	left = 1
	right = 1
	if(visited(x+1,y,prevMoves)):	right = 0.05
	if(visited(x-1,y,prevMoves)):	left  = 0.05
	if(visited(x,y+1,prevMoves)):	down  = 0.05
	if(visited(x,y-1,prevMoves)):	up    = 0.05

	if(confine!=None):
		max_dist = confine // 2
		if(x+1-tx > max_dist): right = 0
		if(tx - (x-1) > max_dist): left = 0
		if(y+1-ty > max_dist): down = 0
		if(ty - (y-1) > max_dist): up = 0
	
	if up==0 and down==0 and right==0 and left==0 :
		return MoveTo(x,y,tx,ty,pirate,prevMoves=prevMoves)
	sum = up+down+left+right
	x = random.random() * sum
	if   x < up: return 1
	elif x < right+up: return 2
	elif x < right+up+down: return 3
	else:  return 4	

"""
#change this
def moveTo(x, y, Pirate, direct=True):
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

#returns whether pirate is on island


"""

def inRect(x, y, xr, yr, h, w):
	return (x>xr and y>yr and x<(xr+w) and y<(yr+h))

"""
Target Probabilities:
	All pirates choose a particular target if its p is greater than 900
	Pirate prefers currently set target unless its p is less than 50
	Pirate prefers a target set anywhere on board if its p is greater than 500
	Pirate prefers a target in the same sub-quarter if its p is greater than 200
	Pirates then chooses randomly between all other targets based on their p-value and distances
"""
def ActPirate(pirate):
	pirateID = pirate.getID()
	islandDimensions = pirate.getDimensionX()
	teamSig = pirate.getTeamSignal()
	pirateSig = pirate.getSignal()
	islandLocations, teamTargets = ReadTeamSignal(teamSig)
	pirateInfo, prevMoves = ReadPirateSignal(pirateSig)
	#prevMoves = []
	currentPirateTarget = {
		"tx": pirateInfo[2],
		"ty": pirateInfo[3],
		"tt": pirateInfo[4]
	}
	x,y = pirate.getPosition()

	preferredTargets = []

	pirateTargets= []
	for target in teamTargets:
		tx,ty,t,p = target
		#target same as currently set
		if(tx==currentPirateTarget["tx"] and ty==currentPirateTarget["ty"] and t==currentPirateTarget["tt"]):
			if(p > 50):
				preferredTargets.append((tx,ty,t,100))
			else:
				pirateTargets.append((tx,ty,t,p))
		elif(p >= 900):
			preferredTargets.clear()
			pirateTargets.clear()
			preferredTargets.append((tx,ty,t,100))
			pirateTargets.append((tx,ty,t,100))
			break
		elif(p >= 500):
			preferredTargets.append((tx,ty,t,100))
		#inner rectangle
		elif(inRect(x,y, tx-islandDimensions/8, ty-islandDimensions/8, islandDimensions/4, islandDimensions/4)):
			if(p >= 200):
				preferredTargets.append((tx,ty,t,100))
			else:
				pirateTargets.append((tx,ty,t,p))
		#outer rectangle
		elif(inRect(x,y, tx-islandDimensions/4, ty-islandDimensions/4, islandDimensions/2, ty+islandDimensions/2)):
			if(p >= 200):
				pirateTargets.append((tx,ty,t,p/2))
			else:
				pirateTargets.append((tx, ty, t, p/2))
		#whole board
		else:
			pirateTargets.append((tx,ty,t,p/6))

	#choose a target
	finalPirateTarget = {}
	random1 = np.random.random()
	if(len(preferredTargets) == 0):
		random1 = 1
	if(len(pirateTargets) == 0):
		random1 = -1
	if(random1 < 0.80 and random1 >= 0):

		#preferred targets
		random2 = np.random.randint(0,len(preferredTargets))
		finalPirateTarget={
			"tx": preferredTargets[random2][0],
			"ty": preferredTargets[random2][1],
			"tt": preferredTargets[random2][2],
		}
	elif(random1>=0 and random1<=1):
		#all targets
		sum = 0.0
		for i in pirateTargets:
			sum += i[3]
		random2 = np.random.random() * sum
		cummulative_sum = 0.0
		for target in pirateTargets:
			cummulative_sum += target[3]
			if(random2 < cummulative_sum):
				finalPirateTarget = {
					"tx": target[0],
					"ty": target[1],
					"tt": target[2]
				}
				break
	else:
		finalPirateTarget = {
			"tx": islandDimensions/2,
			"ty": islandDimensions/2,
			"tt": Task.RANDOM
		}

	frame = pirate.getCurrentFrame()
	
	#Act on the set target
	moveDir = 0
	tx,ty,tt = finalPirateTarget["tx"], finalPirateTarget["ty"], finalPirateTarget["tt"]
	if(tt == Task.RANDOM):
		if(inRect(x, y, tx-islandDimensions/4, ty-islandDimensions/4, islandDimensions/2, islandDimensions/2)):
			moveDir = RandomMove(x, y,pirate, prevMoves, mapDim=islandDimensions)
		else:
			direct = (frame < 100)
			moveDir = MoveTo(x,y,tx,ty,pirate,direct,prevMoves )
	elif(tt == Task.CIRCLE):
		moveDir = circleAround(tx, ty, 3, pirate)
	elif(tt == Task.MV_TO):
		moveDir = MoveTo(x, y, tx, ty,pirate, direct=True, prevMoves=prevMoves)
	elif(tt == Task.RND_CNF):
		moveDir = RandomMove(x, y, pirate, tx, ty, confine=3, prevMoves=prevMoves, mapDim=islandDimensions)


	
	
	finalPirateSignal = sendPirateSignal(pirate, tx, ty, tt,moveDir, pirateSig)
	pirate.setSignal(finalPirateSignal)
	####print(finalPirateSignal)
	return moveDir


def underAttack(pirate,pirateInfo,islandLocations):

    underAttack = [False,-1]
    

    for p in pirateInfo:
        x = p[0]
        y = p[1]
        tx = p[2]
        ty = p[3]
        if (tx,ty) not in islandLocations:
            pass
        else :
            d = abs(x-tx)+abs(y-ty)

            up=(pirate.investigate_up())[1]
            down=(pirate.investigate_down())[1]
            left=(pirate.investigate_left())[1]
            right=(pirate.investigate_right())[1]
            sw=(pirate.investigate_sw())[1]
            nw=(pirate.investigate_nw())[1]
            ne=(pirate.investigate_ne())[1]
            se=(pirate.investigate_se())[1]
            
            if d == 2 & (up or down or left or right or sw or nw or ne or se == "enemy"):
                underAttack[0] = True
            else :
                pass

            for i in range (3) :
                if islandLocations[i] == (tx,ty):
                    underAttack[1] = i+1


    return underAttack

def ActTeam(team):
	
	frame = team.getCurrentFrame()
	print(frame)
	if frame>120:
		team.buildWalls(1)
		team.buildWalls(2)
		team.buildWalls(3)
	sigList=team.getListOfSignals()
	###print([ReadPirateSignal(sig) for sig in sigList])
	pirateInfo  = [(ReadPirateSignal(sig))[0] for sig in sigList]
	####print(pirateInfo)
	islandLocations, signalList = ReadTeamSignal(team.getTeamSignal())
	mapDim = team.getDimensionX()

	quadCentres=[
		(0, 0),
		(0, mapDim),
		(mapDim, 0),
		(mapDim, mapDim) 
	]


	edgeCentres=[
		(mapDim//2,0),
		(0, mapDim//2),
		(mapDim, mapDim//2),
		(mapDim//2, mapDim)
		
	]

	deployPoint = team.getDeployPoint()
	myQuad=np.argmin([abs(deployPoint[0]-qx) + abs(deployPoint[1]-qy) for qx,qy in quadCentres])
	oppQuad=myQuad ^ 3

	islandStatus = [0,0,0]

	underAttack = False
	attackedIsland = []

	newIsland = False
	islandFound = -1
	for sig in pirateInfo:
		if sig[5]==-1:
			pass
		else:
			if(islandLocations[sig[5]-1][0] == -1):
				islandFound = sig[5]-1
				newIsland = True
				islandLocations[sig[5]-1] = (sig[6],sig[7])
				if(sig[8] > 0): islandStatus[sig[5]-1] += 16

				if(sig[9] > 0):
					for i in range(3):
						if(inRect(sig[0],sig[1],islandLocations[i][0]-3,islandLocations[i][1]-3,7,7)):
							underAttack = True
							attackedIsland.append(i+1)
			
	
	islandInfo = team.trackPlayers()
	#island statuses:
	#1: my capturing
	#2: my captured
	#4: opp capturing
	#8: opp captured
	#16: wall
	myCapturing = [False,-1]



	for i in range(6):
		index = i % 3  
		if islandInfo[i] == '':
			islandStatus[index] += 0
		if islandInfo[i] == 'myCapturing':
			islandStatus[index] += 1
			myCapturing = [True, index]
		if islandInfo[i] == 'myCaptured':
			islandStatus[index] += 2
		if islandInfo[i] == '':
			islandStatus[index] += 0
		if islandInfo[i] == 'oppCapturing':
			islandStatus[index] += 4
		if islandInfo[i] == 'oppCaptured':
			islandStatus[index] += 8
		if islandStatus[index] == 6:
			under_attack = [True, index+1]
	#if(frame == 180):
	#	x , y = (1,2,3)
	exploring = False
	
	targets = []
	if(frame < 180):
		exploring = True
		targets.append((
					int((quadCentres[oppQuad][0])), 
					int((quadCentres[oppQuad][1])), 
					1, 140))
		if(frame<140):
			for i in range(4):
				if i!=myQuad and i!=oppQuad:
					targets.append((
						int((quadCentres[i][0])),
						int((quadCentres[i][1])),
						4,100))
					
		if(frame > 140):
			for i in range(4):
				if i!=myQuad and i!=oppQuad:
					targets.append((
						int((3*quadCentres[i][0]+quadCentres[oppQuad][0])/4),
						int((3*quadCentres[i][1]+quadCentres[oppQuad][1])/4),
						1,140))
		for i in range(3):
			if(islandStatus[i] & 1 and frame > 120):
				targets.append((islandLocations[i][0], islandLocations[i][1], 8, 180))
				team.buildWalls(i+1)
			elif(islandStatus[i] & 2 ):
					targets.append((islandLocations[i][0], islandLocations[i][1], 2, 39))
					team.buildWalls(i+1)
		if(newIsland):
			if(islandStatus[islandFound] & 4):
				if(islandStatus[islandFound] & 16):
					pass
				else:
					targets.append((islandLocations[islandFound][0], islandLocations[islandFound][1], 8, 200))
			elif(islandStatus[islandFound] == 0):
				targets.append((islandLocations[i][0], islandLocations[i][1], 8, 80))
	else:

		noPirates = team.getTotalPirates()
		if(noPirates > 60 * ((mapDim/40)**2)) * ((3000-frame)/3000):
			
			#capturing all
			if(all([(i & 0b11) for i in islandStatus])):
				targets.clear()
				for ix,iy in islandLocations:
					targets.append((ix,iy,8,350))

			#otherwise
			for i in range(3):
				if i in attackedIsland:
						team.buildWalls(i+1)
				if(islandStatus[i] & 1):
					targets.append((islandLocations[i][0],islandLocations[i][1], 8, 270))
				elif(islandStatus[i] & 2):
					targets.append((islandLocations[i][0],islandLocations[i][1], 2, 240))
				elif(islandStatus[i] & 4):
					targets.append((islandLocations[i][0],islandLocations[i][1], 1, 150))
				elif(islandStatus[i] & 8):
					targets.append((islandLocations[i][0],islandLocations[i][1], 8, 240))
				else:
					targets.append((islandLocations[i][0],islandLocations[i][1], 8, 500))




				for t in targets:
					if(t[0]==-1 and t[1] == -1):
						exploring=True
						targets.remove(t)
						for x,y in quadCentres:
							targets.append((x,y,1,199))
			

		#lesser pirates, play defence
		else:
			focusedIslands = []
			min_dist = 128
			temp = [(0,1),(1,2),(0,2)]
			ind = np.argmin([  ( abs(islandLocations[i[0]][0] - islandLocations[i[1]][0]) + abs(islandLocations[i[0]][1] - islandLocations[i[1]][1])) for i in temp])
			focusedIslands = [temp[ind][0], temp[ind][1]]
			thirdIsland = 3 - np.sum(focusedIslands)
			if(islandStatus[thirdIsland] & 0b11 or islandStatus[thirdIsland] == 0):
				if(islandStatus[focusedIslands[0]] & 0b11):
					focusedIslands = [focusedIslands[0], thirdIsland]
				else:
					focusedIslands = [focusedIslands[1], thirdIsland]

			
			for i in focusedIslands:
				task = (2 if islandStatus[i] & 0b10 else 8)
				if(not islandStatus[i] & 3):
					targets.append((islandLocations[i][0],islandLocations[i][1],task,900))
					continue
				targets.append((islandLocations[i][0],islandLocations[i][1],task,300))
				if i in attackedIsland:
					team.buildWalls(i+1)

		if(team.getTotalGunpowder() < 1000 or exploring):
			t = (frame // 50) % 2
			if t == 0:
				for qx,qy in quadCentres:
					targets.append((qx,qy,4, 250))
			else:
				for qx,qy in edgeCentres:
					targets.append((qx,qy,4, 250))


	targets = sorted(targets, key=lambda t: t[3])
	if(len(targets) > 7): targets = targets[-7:]

	modifiedTargets = []
	#changing p values
	commonTargets = []
	if(underAttack):
		print("Should Build Walls Now")

	#for s in sigList:
		#print(s)

	for t in targets:
		if((t[0],t[1]) in [(tar[0],tar[1]) for tar in signalList]):
			pCount=0
			finalP = t[3]
			for p in pirateInfo:
				if(p[2]==t[0] and p[3]==t[1]):	pCount += 1
			percentage = pCount / max(1,team.getTotalPirates())
			##print(percentage)
			if(percentage < 0.1):
				finalP *= 1.2
			elif(percentage < 0.25):
				if(finalP>500):	finalP *= 1.2
			elif(percentage < 0.5):
				if(finalP < 300): finalP *= 0.9
			elif(percentage < 0.75):
				if(finalP < 700): finalP *= 0.80
			else:
				finalP *= 0.75
			finalP = int(finalP)	
			modifiedTargets.append((t[0],t[1],t[2],finalP))		
		else: 
			modifiedTargets.append(t)

	signal=WriteTeamSignal(islandLocations,modifiedTargets)
	
	##print(frame, signal)
	team.setTeamSignal(signal)



"""
def ActPirate(pirate):
	x,y = pirate.getPosition()
	targets = [(10,10), (30, 10), (10,30), (30, 30)]
	a = np.random.randint(0,4)
	tx,ty = targets[a]
	if((tx,ty) == pirate.getDeployPoint()):
		tx = 40-tx
		ty=40-ty
	if pirate.getSignal() == "":
		pirate.setSignal(f"{tx}:{ty}")
	else:
		tx, ty = pirate.getSignal().split(":")
		tx=int(tx)
		ty=int(ty)

	move = RandomMove(x, y,tx, ty, 15)
	return move
	"""


if __name__ == '__main__':
	signal_list  = ["12:23:1:1:1:-1:-1:-1:0:0:uuuuuuuuuuuuuu" for i in range(5)]
	x = [(ReadPirateSignal(signal))[0] for signal in signal_list]
	for sig in x:
		pass
		###print(sig[5])