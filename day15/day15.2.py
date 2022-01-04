import csv
import heapq

grid = dict()
weights = dict()
heap = []

def readInput():
    with open('day15.txt', 'r') as fd:
        reader = list(csv.reader(fd))
        index = 0
        rows = len(reader)
        cols = len(reader[0][0])
        while index < len(reader):
            line = reader[index][0]
            for j in range(len(line)):
                grid[(index, j)] = int(line[j])
                weights[(index, j)] = float('inf')
                heapq.heappush(heap, (float('inf'), (index, j)))
                addExtraCoords(index, j, rows, cols)
            index += 1
    return (rows, cols)

def addExtraCoords(row, col, rows, cols):
    for i in range(5):
        for j in range(5):
            tot = i + j
            if tot == 0:
                continue
            newRow = row + rows * i
            newCol = col + cols * j
            newWeight = (grid[(row, col)] + tot) % 9
            if newWeight == 0:
                newWeight = 9
            grid[(newRow, newCol)] = newWeight
            weights[(newRow, newCol)] = float('inf')
            heapq.heappush(heap, (float('inf'), (newRow, newCol)))



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
        flag = False
        while flag == False and len(heap) > 0:
            (weight, node) = heapq.heappop(heap)
            if node not in unvisited:
                continue
            if weights[node] == weight:
                flag = True
                currNode = node
            else:
                heapq.heappush(heap, (weights[node], node))

def main():
    (rows, cols) = readInput()
    rows = rows * 5
    cols = cols * 5
    print(rows, cols)
    unvisited = set(grid.keys())
    startNode = (0,0)
    endNode = (cols - 1, rows - 1)
    weights[startNode] = 0
    dijkstra(startNode, endNode, rows, cols, unvisited)

    return weights[endNode]

print(main())