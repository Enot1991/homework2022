f1 = open("input.txt", "r")
f2 = open("output1.txt", "w")
a = f1.read()
floor = 0

for element in a:
    if element == '(':
        floor = floor + 1
    else:
        floor = floor - 1

f2.write(str(floor))
f2.close
f1.close
