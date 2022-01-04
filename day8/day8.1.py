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

def countUnique(d, i):
    count = 0
    for s in d[i]:
        if len(s) == 2 or len(s) == 3 or len(s) == 4 or len(s) == 7:
            count += 1
    return count

def main():
    (inp, out) = readInput()
    count = 0
    for key in out:
        count += countUnique(out, key)
    return count

print(main())