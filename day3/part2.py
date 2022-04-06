f1 = open("input.txt", "r")
f2 = open("output2.txt", "w")
a = f1.read()
x1 = 0
y1 = 0
x2 = 0
y2 = 0
x1y1 = [[0,0]]
x2y2 = [[0,0]]
home = []



for i in range(0,len(a),2):
    if a[i]=='^':
        y1=y1+1
    if a[i]=='v':
        y1=y1-1
    if a[i]=='>':
        x1=x1+1
    if a[i]=='<':
        x1=x1-1
    x1y1.append([x1,y1])
    
for i in range(1,len(a),2):
    if a[i]=='^':
        y2=y2+1
    if a[i]=='v':
        y2=y2-1
    if a[i]=='>':
        x2=x2+1
    if a[i]=='<':
        x2=x2-1
    x2y2.append([x2,y2])

x1y1.extend(x2y2)

for i in x1y1:
    if i not in home:
        home.append(i)

f2.write(str(len(home)))
f2.close
f1.close
