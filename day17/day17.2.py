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
validVelocities = set()

def findValidVelocity(xPos, yPos, xVel, yVel):
    (xStart, yStart) = xVel, yVel
    while xPos <= xMax and yPos >= yMin:
        if xPos >= xMin and xPos <= xMax and yPos >= yMin and yPos <= yMax:
            validVelocities.add((xStart, yStart))
        (xPos, yPos, xVel, yVel) = takeStep(xPos, yPos, xVel, yVel)

def getVelocities(xStart):
    res = []
    for x in range(xStart + 1, xMax + 1):
        for y in range(yMin, 1000):
            res.append((x,y))
    return res

def checkVelocities(start):
    (xStart, yStart) = start
    velocities = getVelocities(xStart)
    for xVel, yVel in velocities:
        findValidVelocity(xStart, yStart, xVel, yVel)

def main():
    start = (0, 0)
    checkVelocities(start)
    return len(validVelocities)

print(main())