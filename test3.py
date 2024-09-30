from random import randint
from numpy import random

name = 'gpt2'

class Strategy:
    dir = [1]  # Initialize direction

    # Function to move a pirate to a specific position (x, y)
    def moveTo(self, x, y, pirate):
        position = pirate.getPosition()
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

    # Function to spread pirates across the map
    def spread(self, pirate):
        j, k = pirate.getPosition()
        t = pirate.getCurrentFrame()

        if t < 120 or 500 <= t < 720 or 900 <= t < 1200 or 1500 <= t < 1800 or 2100 <= t < 2400 or 2700 <= t <= 3000:
            if j == 39 and Strategy.dir[0] == 1:  # If at rightmost edge and moving right
                Strategy.dir[0] = -1  # Change direction to move left
            elif j == 0 and Strategy.dir[0] == -1:  # If at leftmost edge and moving left
                Strategy.dir[0] = 1  # Change direction to move right
            return self.moveTo(j + Strategy.dir[0], k, pirate)
        else:
            if k == 39 and Strategy.dir[0] == 1:  # If at bottom edge and moving down
                Strategy.dir[0] = -1  # Change direction to move up
            elif k == 0 and Strategy.dir[0] == -1:  # If at top edge and moving up
                Strategy.dir[0] = 1  # Change direction to move down
            return self.moveTo(j, k + Strategy.dir[0], pirate)

    # Function to act based on the team's strategy
    def ActPirate(self, pirate):
        up = pirate.investigate_up()[0]
        down = pirate.investigate_down()[0]
        left = pirate.investigate_left()[0]
        right = pirate.investigate_right()[0]
        x, y = pirate.getPosition()
        pirate.setSignal("")
        s = pirate.trackPlayers()

        # Function to capture islands or attack enemy pirates
        def captureOrAttack(island_no, direction, s):
            if (
                (direction == "up" and s[island_no - 1] != "myCaptured")
                or (direction == "down" and s[island_no - 1] != "myCaptured")
                or (direction == "left" and s[island_no - 1] != "myCaptured")
                or (direction == "right" and s[island_no - 1] != "myCaptured")
            ):
                s = direction[-1] + str(x) + "," + str(y - 1)
                pirate.setTeamSignal(s)

        # Check and set signals for capturing islands or attacking enemy pirates
        captureOrAttack(1, up, s)
        captureOrAttack(2, down, s)
        captureOrAttack(3, left, s)
        captureOrAttack(4, right, s)

        # Move according to the team's strategy
        if pirate.getTeamSignal() != "" and pirate.getCurrentFrame() > 800:
            s = pirate.getTeamSignal()
            l = s.split(",")
            x = int(l[0][1:])
            y = int(l[1])

            return self.moveTo(x, y, pirate)
        else:
            return self.spread(pirate)

    # Function to act based on the team's strategy
    def ActTeam(self, team):
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

# Initialize the strategy
strategy = Strategy()
