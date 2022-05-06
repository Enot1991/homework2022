import json



f1 = open("input.txt", "r")
f2 = open("output2.txt", "w")
a = f1.read()



def sum_json(something, exclude_red):
    result = 0
    if isinstance(something, int):
        result += something
    elif isinstance(something, list):
        for item in something:
            result += sum_json(item, exclude_red)
    elif isinstance(something, dict):
        for value in something.values():
            if exclude_red and value == "red":
                return 0
            result += sum_json(value, exclude_red)
    return result



json_object = json.JSONDecoder().decode(a)



f2.write(str(sum_json(json_object, True)))
f2.close
f1.close
