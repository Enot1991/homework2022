import re
from collections import defaultdict



def possible_replacements(current, replacement_dict):
    result = []
    molecule = current[0]
    path = current[1]
    for k, v in replacement_dict.items():
        for replacement in v:
            for match in re.finditer(replacement, molecule):
                new_molecule = molecule[:match.start()] + k + molecule[match.start() + len(replacement):]
                list_path = list(path)
                list_path.append((k, replacement, match.start()))
                result.append((new_molecule, tuple(list_path)))
    return result



def replacement_dfs(start, targets, result):
    current = start
    if current in targets:
        return result
    possible = []
    for k, v in replacement_dict.items():
        for replacement in v:
            if replacement in current:
                possible.append((len(replacement), replacement, k))
    possible = sorted(possible, key=lambda tup: tup[0], reverse=True)
    if len(possible) == 0:
        return None
    for poss in possible:
        result_copy = result.copy()
        matches = sorted(list(re.finditer(poss[1], current)), key=lambda match: match.start(), reverse=True)
        match = matches[0]
        new_molecule = current[:match.start()] + poss[2] + current[match.start() + len(poss[1]):]
        list_path = result_copy[-1][1].copy()
        list_path.append((poss[1], poss[2], match.start()))
        result_copy.append((new_molecule, list_path))
        new_result = replacement_dfs(new_molecule, targets, result_copy)
        if new_result is None:
            continue
        if new_result[len(new_result)-1][0] in targets:
            return new_result
    return None



def get_rnar_sections(molecule):
    rn_indices = []
    for match in re.finditer("Rn", molecule):
        rn_indices.append(match.start())
    ar_indices = []
    for match in re.finditer("Ar", molecule):
        ar_indices.append(match.start())
    rnar_sections = []
    for ar in ar_indices:
        for i, rn in enumerate(rn_indices):
            if rn > ar:
                break
        rn = rn_indices[i - 1]
        rnar_sections.append((rn, ar))
        rn_indices.remove(rn)
    return rnar_sections



replacement_dict = defaultdict(list)
molecule = None
for line in open("input.txt"):
    line = line.strip()
    if "=" in line:
        in_out = line.split(" => ")
        replacement_dict[in_out[0]].append(in_out[1])
    else:
        molecule = line



new_molecules = set()
for k, v in replacement_dict.items():
    for replacement in v:
        for match in re.finditer(k, molecule):
            new_molecule = molecule[:match.start()] + replacement + molecule[match.start()+len(k):]
            new_molecules.add(new_molecule)


f2 = open("output1.txt", "w")
f2.write(str(len(new_molecules)))
f2.close

