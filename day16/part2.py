import re



def find_sue(aunts, aunt_sue, ranges):
    for i, aunt in enumerate(aunts):
        equal = True
        for k, v in aunt.items():
            if ranges and (k == "cats" or k == "trees"):
                if aunt_sue[k] >= v:
                    equal = False
                    break
            elif ranges and (k == "pomeranians" or k == "goldfish"):
                if aunt_sue[k] <= v:
                    equal = False
                    break
            elif aunt_sue[k] != v:
                equal = False
                break
        if equal:
            return i + 1
    return 0



input_pattern = r'Sue \d*: (.*)'
aunts = []
for line in open("input.txt"):
    match = re.match(input_pattern, line.strip())
    items = match.group(1).split(", ")
    item_dict = dict()
    for item in items:
        key_value = item.split(": ")
        item_dict[key_value[0]] = int(key_value[1])
    aunts.append(item_dict)



aunt_sue = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
            }



f2 = open("output2.txt", "w")
f2.write(str(find_sue(aunts, aunt_sue, True)))
f2.close
