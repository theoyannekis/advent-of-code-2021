import csv

def readInput():
    with open('day7.txt', 'r') as fd:
        crabs = csv.reader(fd)
        return list(map(int, list(crabs)[0]))

def crabCost(pos, goal):
    n = abs(pos - goal)
    return n * (n + 1) / 2

def main():
    crabs = readInput()
    maxCrab = max(crabs)
    minCost = 100000000
    for i in range(maxCrab):
        cost = 0
        for crab in crabs:
            cost += crabCost(crab, i)
        minCost = min(minCost, cost)
    return minCost

print(main())