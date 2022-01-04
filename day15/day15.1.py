import csv

grid = dict()
weights = dict()

def readInput():
    with open('day15.txt', 'r') as fd:
        reader = list(csv.reader(fd))
        index = 0
        rows = len(reader)
        cols = len(reader[0][0])
        while index < len(reader):
            line = reader[index][0]
            for j in range(len(line)):
                grid[(j, index)] = int(line[j])
            index += 1
    return (rows, cols)

def findNeighbors(node, rows, cols):
    res = []
    if node[0] < cols - 1:
        res.append((node[0] + 1, node[1]))
    if node[0] > 0:
        res.append((node[0] - 1, node[1]))
    if node[1] < rows - 1:
        res.append((node[0], node[1] + 1))
    if node[1] > 0:
        res.append((node[0], node[1] - 1))
    return res


def dijkstra(currNode, endNode, rows, cols, unvisited):
    while len(unvisited) > 0 and endNode in unvisited:
        neighbors = findNeighbors(currNode, rows, cols)
        for node in neighbors:
            if node in unvisited:
                weights[node] = min(weights[currNode] + grid[node], weights[node])
        unvisited.remove(currNode)
        minWeight = float('inf')
        minKey = None
        for key in unvisited:
            if weights[key] <= minWeight:
                minWeight = weights[key]
                minKey = key
        currNode = minKey



def main():
    (rows, cols) = readInput()
    unvisited = set(grid.keys())
    for key in grid:
        weights[key] = float('inf')
    startNode = (0,0)
    endNode = (cols - 1, rows - 1)
    weights[startNode] = 0
    dijkstra(startNode, endNode, rows, cols, unvisited)

    return weights[endNode]

print(main())