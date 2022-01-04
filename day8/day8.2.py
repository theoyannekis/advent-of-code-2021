import csv

def readInput():
    with open('day8.txt', 'r') as fd:
        lst = csv.reader(fd)
        inp = dict()
        out = dict()
        count = 0
        for row in lst:
            spl = row[0].split()
            ind = spl.index("|")
            inp[count] = spl[:ind]
            out[count] = spl[ind+1:]
            count += 1
        return (inp, out)

def diffTwoStrings(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    difference = set1.symmetric_difference(set2)
    return list(difference)

def findZero(lst):
    one = findOne(lst)
    nine = findNine(lst)
    return list(filter(lambda x: len(x) == 6 and len(diffTwoStrings(one, x)) == 4 and x != nine, lst))[0]

def findOne(lst):
    return list(filter(lambda x: len(x) == 2, lst))[0]

def findTwo(lst):
    four = findFour(lst)
    return list(filter(lambda x: len(x) == 5 and len(diffTwoStrings(four, x)) == 5, lst))[0]

def findThree(lst):
    one = findOne(lst)
    return list(filter(lambda x: len(x) == 5 and len(diffTwoStrings(one, x)) == 3, lst))[0]

def findFour(lst):
    return list(filter(lambda x: len(x) == 4, lst))[0]

def findFive(lst):
    two = findTwo(lst)
    three = findThree(lst)
    return list(filter(lambda x: len(x) == 5 and x != two and x != three, lst))[0]

def findSix(lst):
    zero = findZero(lst)
    nine = findNine(lst)
    return list(filter(lambda x: len(x) == 6 and x != zero and x != nine, lst))[0]

def findSeven(lst):
    return list(filter(lambda x: len(x) == 3, lst))[0]

def findEight(lst):
    return list(filter(lambda x: len(x) == 7, lst))[0]

def findNine(lst):
    four = findFour(lst)
    a = findA(lst)
    combo = four + a
    return list(filter(lambda x: len(x) == 6 and len(diffTwoStrings(combo, x)) == 1, lst))[0]

def findA(lst):
    one = findOne(lst)
    seven = findSeven(lst)
    return diffTwoStrings(one, seven)[0]

def createInputMap(d, i):
    inp = d[i]
    inpMap = dict()
    inpMap[findZero(inp)] = 0
    inpMap[findOne(inp)] = 1
    inpMap[findTwo(inp)] = 2
    inpMap[findThree(inp)] = 3
    inpMap[findFour(inp)] = 4
    inpMap[findFive(inp)] = 5
    inpMap[findSix(inp)] = 6
    inpMap[findSeven(inp)] = 7
    inpMap[findEight(inp)] = 8
    inpMap[findNine(inp)] = 9
    return inpMap

def calculateOutput(inputMap, out):
    return inputMap[getMatchingKey(inputMap, out[0])] * 10 ** 3 + inputMap[getMatchingKey(inputMap, out[1])] * 10 ** 2 + inputMap[getMatchingKey(inputMap, out[2])] * 10 + inputMap[getMatchingKey(inputMap, out[3])]

def getMatchingKey(inputMap, s):
    for key in inputMap:
        if len(diffTwoStrings(key, s)) == 0:
            return key

def main():
    (inp, out) = readInput()
    count = 0
    for key in inp:
        inputMap = createInputMap(inp, key)
        count += calculateOutput(inputMap, out[key])
    return count

print(main())