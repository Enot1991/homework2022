from itertools import combinations
from collections import defaultdict



containers = []
for line in open("input.txt"):
    container = int(line.strip())
    containers.append(container)



liters = 150
combs = defaultdict(list)
for i in range(1, len(containers)):
    for comb in combinations(containers, i):
        if sum(comb) == liters:
            combs[i].append(comb)



f2 = open("output1.txt", "w")
f2.write(str(sum(len(x) for x in combs.values())))
f2.close
