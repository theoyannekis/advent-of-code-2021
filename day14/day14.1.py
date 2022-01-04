import csv

d = dict()
rules = dict()

def readInput():
    with open('day14.txt', 'r') as fd:
        reader = list(csv.reader(fd))
        index = 0
        while index < len(reader):
            line = reader[index]
            if index == 0:
                template = line[0]
            elif len(line) == 0:
                index += 1
                continue
            else:
                spl = line[0].split(' -> ')
                rules[spl[0]] = spl[1]
            index += 1

    return template

def applyRulesPart1(template, rounds):
    res = list(template)
    for i in range(rounds):
        print(i)
        prev = res.copy()
        res = []
        for j in range(len(prev)):
            res.append(prev[j])
            if (j < len(prev) - 1):
                pair = prev[j:j+2]
                res.append(rules[''.join(pair)])

    return ''.join(res)

def applyToPair(pair, rounds):
    if rounds == 0:
        return pair[0]
    if (pair, rounds) not in d:
        insert = rules[pair]
        d[(pair, rounds)] = applyToPair(pair[0] + insert, rounds - 1) + applyToPair(insert + pair[1], rounds - 1)
    return d[(pair, rounds)]

def applyRulesPart2(template, rounds):
    res = ''
    print(len(template))
    for j in range(len(template) - 1):
        if (j % 500000 == 0):
            print(j)
        res = res + applyToPair(template[j:j+2], rounds)

    return res + template[-1]


def main():
    template = readInput()

    polymerPart1 = applyRulesPart1(template, 22)
    polymer = applyRulesPart2(polymerPart1, 18)
    print(len(polymer))

    uniqueElems = list(set(rules.values()))
    counts = list(map(lambda elem: polymer.count(elem), uniqueElems))
    print(d)
    return max(counts) - min(counts)

print(main())

