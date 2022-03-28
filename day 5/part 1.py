import re



f1 = open("input.txt", "r")
f2 = open("output1.txt", "w")
a = f1.read()

data_a = a.split('\n')
glas = ['a','e','i','o','u']
count = 0
new_data_a = []
new_new_data_a = []
new_new_new_data_a = []

for i in range(len(data_a)):
    x = data_a[i]
    if 'ab' not in x:
        if 'cd' not in x:
            if 'pq' not in x:
                if 'xy' not in x:
                    new_data_a.append(x)
                    
for i in range(len(new_data_a)):
    y = new_data_a[i]
    for l in range(len(y)-1):
        if y[l]==y[l+1]:
            new_new_data_a.append(y)
            break
            
for i in range(len(new_new_data_a)):
    z = new_new_data_a[i]
    for n in range(len(z)):
        if z[n] in glas:
            count += 1
        if count > 2:
            new_new_new_data_a.append(z)
            break
    count = 0


f2.write(str(len(new_new_new_data_a)))
f2.close
f1.close

