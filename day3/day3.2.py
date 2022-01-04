import csv

def binToDec(lst):
    dec = 0
    lastInd = len(lst) - 1
    i = 0
    while lastInd - i >= 0:
        val = 2 ** i
        dec += val * int(lst[lastInd - i])
        i += 1
    print(dec)
    return dec

def mostCommon(lst, i):
    diff = 0
    for num in lst:
        bit = int(num[i])
        if bit == 1:
            diff += 1
        else:
            diff -= 1
    if diff >= 0:
        return 1
    else:
        return 0

def leastCommon(lst, i):
    diff = 0
    for num in lst:
        bit = int(num[i])
        if bit == 1:
            diff += 1
        else:
            diff -= 1
    if diff < 0:
        return 1
    else:
        return 0

def removeVal(lst, i, val):
    res = []
    for num in lst:
        bit = int(num[i])
        if bit == val:
            res.append(num)
    return res

def oxygen(lst):
    i = 0
    while len(lst) > 1:
        commonVal = leastCommon(lst, i)
        lst = removeVal(lst, i, commonVal)
        i += 1
    return lst[0]


def co2(lst):
    i = 0
    while len(lst) > 1:
        commonVal = mostCommon(lst, i)
        lst = removeVal(lst, i, commonVal)
        i += 1
    return lst[0]

with open('day3.txt', 'r') as fd:
    reader = csv.reader(fd)
    text = []
    for row in reader:
        text.append(row[0])
    print(binToDec(oxygen(text)) * binToDec(co2(text)))




