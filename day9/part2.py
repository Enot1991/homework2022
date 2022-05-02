import itertools
import re



f1 = open("input.txt", "r")
f2 = open("output2.txt", "w")
a = f1.read()



data = re.split('\n',a)
new_data = []
sity = []



for i in range(len(data)):
    b = re.split('\s',data[i])
    new_data.append(b)



for i in new_data:
    i.pop(1)
    i.pop(2)



for i in new_data:
    for j in i:
        if j.isdigit() == False:
            if j not in sity:
                 sity.append(j)



combinations = list(itertools.permutations(sity))



count=[]
for i in combinations:
    count1 = 0
    for j in range(len(i)-1):
        for a in new_data:
            if (i[j]==a[0] or i[j]==a[1]) and (i[j+1]==a[0] or i[j+1]==a[1]):
                  count1 += int(a[2])
    count.append(count1)
          


f2.write(str(max(count)))
f2.close
f1.close
