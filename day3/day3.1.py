import csv

def binToDec(lst):
    dec = 0
    lastInd = len(lst) - 1
    i = 0
    while lastInd - i >= 0:
        val = 2 ** i
        dec += val * lst[lastInd - i]
        i += 1
    print(dec)
    return dec

with open('day3.txt', 'r') as fd:
    reader = csv.reader(fd)
    gamma = [0] * 12
    epsilon = [0]* 12
    for row in reader:
        s = row[0]
        for i in range(len(s)):
            bit = int(s[i])
            if bit == 1:
                gamma[i] += 1
            else:
                gamma[i] -= 1

    for i in range(len(gamma)):
        if gamma[i] > 0:
            gamma[i] = 1
            epsilon[i] = 0
        else:
            gamma[i] = 0
            epsilon[i] = 1
    print(gamma)
    print(epsilon)
    print(binToDec(gamma) * binToDec(epsilon))

