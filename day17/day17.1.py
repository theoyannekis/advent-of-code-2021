import csv


def readInput():
    with open('day17.txt', 'r') as fd:
        line = list(csv.reader(fd))[0]
        splX = line[0].split("..")
        splY = line[1].split("..")
        xMin = int(splX[0][-2:])
        xMax = int(splX[1][:2])
        yMin = int(splY[0][-4:])
        yMax = int(splY[1][:4])
    return (xMin, xMax, yMin, yMax)

def takeStep(xPos, yPos, xVel, yVel):
    newXPos = xPos + xVel
    newYPos = yPos + yVel
    newXVel = xVel - 1
    if newXVel < 0:
        newXVel = 0
    newYVel = yVel - 1
    return (newXPos, newYPos, newXVel, newYVel)

(xMin, xMax, yMin, yMax) = readInput()

def getTargetArea():
    res = []
    for x in range(xMin, xMax + 1):
        for y in range(yMin, yMax + 1):
            res.append((x, y))
    return res

def maxYInPath(xPos, yPos, xVel, yVel):
    maxY = float('-inf')
    while xPos <= xMax and yPos >= yMin:
        if xPos >= xMin and xPos <= xMax and yPos >= yMin and yPos <= yMax:
            return maxY
        maxY = max(maxY, yPos)
        (xPos, yPos, xVel, yVel) = takeStep(xPos, yPos, xVel, yVel)
    return float("-inf")

def getVelocities(xStart):
    res = []
    for x in range(xStart + 1, xMax + 1):
        for y in range(yMin, 500):
            res.append((x,y))
    return res

def findMax(start):
    (xStart, yStart) = start
    maxY = float('-inf')
    velocities = getVelocities(xStart)
    for xVel, yVel in velocities:
        maxY = max(maxY, maxYInPath(xStart, yStart, xVel, yVel))

    return maxY

def main():
    start = (0, 0)
    maxY = findMax(start)
    return maxY

print(main())