f1 = open("input.txt", "r")
f2 = open("output1.txt", "w")
a = f1.read()
x = 0
y = 0
xy = [[0,0]]
home = []



for i in a:
    if i=='^':
        y=y+1
    if i=='v':
        y=y-1
    if i=='>':
        x=x+1
    if i=='<':
        x=x-1
    xy.append([x,y])

for i in xy:
    if i not in home:
        home.append(i)

f2.write(str(len(home)))
f2.close
f1.close

