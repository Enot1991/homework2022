import re


f1 = open("input.txt", "r")
f2 = open("output2.txt", "w")
a = f1.read()

data_a = a.split('\n')
new_data_a = []
new_new_data_a = []

for i in range(len(data_a)):
    y = data_a[i]
    for l in range(len(y)-2):
        if y[l]==y[l+2]:
            new_data_a.append(y)
            break
for b in range(len(new_data_a)):
    count = 0
    x = new_data_a[b]
    for m in range(len(x)):
        if x[m:m+2] in x[(m+2):]:
            count+=1
    if count > 0:
        new_new_data_a.append(x)

            
f2.write(str(len(new_new_data_a)))
f2.close
f1.close

