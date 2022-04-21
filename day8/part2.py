import re
import itertools



f1 = open("input.txt", "r")
f2 = open("output2.txt", "w")
a = f1.read()



data_1 = re.split("\n",a)
data_2 = []
one = []
two = []



for stroka in data_1:
    count_1 = 0
    count_1 = len(stroka)
    one.append(count_1)
    new_stroka = stroka[1:-1]
    data_2.append(new_stroka)


    

for stroka in data_2:
    stroka = stroka + "%%%%%%"
    stroka = stroka.replace('\\"','%%%%')
    stroka = stroka.replace('\\','%%')
    count_2 = 0
    count_2 = len(stroka)
    two.append(count_2)


s = 0


for i in range(len(one)):
    s += two[i] - one[i]
            


f2.write(str(s))
f2.close
f1.close
