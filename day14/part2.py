import re



reindeer = dict()
input_pattern = r'(\w*) can fly (\d*) km\/s for (\d*) seconds, but then must rest for (\d*) seconds.*'
for line in open("input.txt"):
    match = re.match(input_pattern, line.strip())
    name = match[1]
    speed = int(match[2])
    speed_time = int(match[3])
    rest_time = int(match[4])
    reindeer[name] = (speed, speed_time, rest_time)



sim = dict()
for k, v in reindeer.items():
    sim[k] = {"dist": 0, "points": 0, "rem_speed": v[1], "rem_rest": 0}



for i in range(2503):
    max_dist = None
    for k, v in reindeer.items():
        if sim[k]["rem_speed"] > 0:
            sim[k]["rem_speed"] -= 1
            sim[k]["dist"] += v[0]
            if sim[k]["rem_speed"] == 0:
                sim[k]["rem_rest"] = v[2]
        elif sim[k]["rem_rest"] > 0:
            sim[k]["rem_rest"] -= 1
            if sim[k]["rem_rest"] == 0:
                sim[k]["rem_speed"] = v[1]
        else:
            assert False
        if max_dist is None or sim[k]["dist"] > max_dist:
            max_dist = sim[k]["dist"]
    for k, v in reindeer.items():
        if sim[k]["dist"] == max_dist:
            sim[k]["points"] += 1



max_dist = None
max_points = None
for k, v in reindeer.items():
    if max_dist is None or sim[k]["dist"] > max_dist:
        max_dist = sim[k]["dist"]
    if max_points is None or sim[k]["points"] > max_points:
        max_points = sim[k]["points"]



f2 = open("output2.txt", "w")
f2.write(str(max_points))
f2.close
