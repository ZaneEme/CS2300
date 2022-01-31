from Board import Board
from Vector import Vector


class Game:
    def run(self):
        firstInfo = ""
        restOfLines = [""]        
        with open("pa2_input_2.txt") as f:
            firstInfo = f.readline().split()
            restOfLines = f.readlines()
        
        boardSize = int(firstInfo[0])
        turnHistory = int(firstInfo[1])

        boardOne = Board(boardSize)
        print("Board created!")
        boardOne.printBoard()
    

        # main loop
        totalVectors = []
        currentBresenhams = []
        whoMadeInvalid = [0, 0]
        whosTurn = 0
        boardUpdateCounter = 1
        for turn in restOfLines:
            #Flip who's turn it is
            whosTurn = 1 if whosTurn == 0 else 0

            coords = [int(i) for i in turn.split()]
            curTurnLine = Vector([coords[0] - 1, coords[1] - 1], [coords[2] - 1, coords[3] - 1])

            
            turnValid = self.isTurnValid(totalVectors, curTurnLine)

            if (turnValid == False):
                whoMadeInvalid[whosTurn] += 1
            else:
                totalVectors.append(curTurnLine)
                
                bresenhamOfLine = self.bresenham(curTurnLine)
                currentBresenhams.append(bresenhamOfLine)

                if(len(currentBresenhams) >= turnHistory):
                    currentBresenhams.pop(0)


            for bresenham in currentBresenhams:
                boardUpdateCounter += 1
                for location in bresenham:
                    X = int(location[0])
                    Y = int(location[1])
                    # X if player 1, O if player 2
                    if(boardUpdateCounter % 2 == 0):
                        boardOne.gameBoard[X][Y] = "X"
                    else:
                        boardOne.gameBoard[X][Y] = "O"
            

            if(all(whoMadeInvalid) > 0):
                break

            
            boardOne.printBoard()
            boardOne.printToFile("pa2_output_2.txt")
            print(f"Player one: {whoMadeInvalid[0]}, Player two: {whoMadeInvalid[1]}\n")
        pOnePoints = 0
        pTwoPoints = 0
        for row in boardOne.gameBoard:
            for col in row:
                if col == "X":
                    pOnePoints += 1
                elif col == "O":
                    pTwoPoints += 1
        print(f"Player one total points: {pOnePoints} \nPlayer two total points: {pTwoPoints}")

            


    def isTurnValid(self, totalVectors, curTurnLine):
        # check every other line to test if turn is valid
        for a in range(0, len(totalVectors) - 1):
            lineToCheck = totalVectors[a]
            # check start points used
            if(curTurnLine.start[0] == lineToCheck.start[0] and curTurnLine.start[1] == lineToCheck.start[1]):
                return False
            # check end points used
            elif(curTurnLine.end[0] == lineToCheck.end[0] and curTurnLine.end[1] == lineToCheck.end[1]):
                return False
            # check slope
            elif(lineToCheck.slope == curTurnLine.slope):
                return False
            # check midpoints
            elif(lineToCheck.midpoint == curTurnLine.midpoint):
                return False
        return True

    def bresenham(self, vector):
        x0 = vector.start[0]
        x1 = vector.end[0]
        y0 = vector.start[1]
        y1 = vector.end[1]

        # change in x, change in y
        dx = x1 - x0
        dy = y1 - y0

        # change sign according to slope
        xSign = 1 if dx > 0 else -1
        ySign = 1 if dy > 0 else -1

        dx = abs(dx)
        dy = abs(dy)

        if dx > dy:
            ax, ay, bx, by = xSign, 0, 0, ySign
        else:
            dx, dy = dy, dx
            ax, ay, bx, by = 0, ySign, xSign, 0

        D = 2 * dy - dx
        y = 0

        for x in range(dx + 1):
            yield x0 + (x * ax) + (y * bx), y0 + (x * ay) + (y * by)
            if D >= 0:
                y += 1
                D -= (2 * dx)
            D += (2 * dy)