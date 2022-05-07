f2 = open("output1.txt", "w")



import re
from itertools import permutations



def find_max_happiness(v, e):
    max_happiness = None
    for perm in permutations(v):
        happiness = 0
        prev = None
        for person in perm:
            if prev is not None:
                happiness += e[(prev, person)]
                happiness += e[(person, prev)]
            prev = person
        happiness += e[(prev, perm[0])]
        happiness += e[(perm[0], prev)]

        if max_happiness is None or happiness > max_happiness:
            max_happiness = happiness
    return max_happiness



input_pattern = r'(\w*) would (\w*) (\d*) .* (\w*)'
v = set()
e = dict()
for line in open("input.txt"):
    match = re.match(input_pattern, line.strip())
    person1 = match[1]
    person2 = match[4]
    v.add(person1)
    v.add(person2)
    sign = 0
    if match[2] == "lose":
        sign = -1
    elif match[2] == "gain":
        sign = 1
    else:
        assert False
    weight = int(match[3]) * sign
    e[(person1, person2)] = weight



f2.write(str(find_max_happiness(v,e)))
f2.close
