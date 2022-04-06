f1 = open("input.txt", "r")
f2 = open("output2.txt", "w")
a = f1.read()
floor = 0
count = 0

for element in a:
    if element == '(':
        floor = floor + 1
        count = count + 1
    else:
        floor = floor - 1
        count = count + 1
    if floor == -1:
        f2.write(str(count))
        break
     
f2.close
f1.close
