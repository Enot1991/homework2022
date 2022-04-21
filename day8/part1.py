import re
import itertools



f1 = open("input.txt", "r")
f2 = open("output1.txt", "w")
a = f1.read()



data_1 = re.split("\n",a)
data_2 = []
one = []
two = []
bebra = list(itertools.product('1234567890qwertyuiopasdfghjklzxcvbnm','1234567890qwertyuiopasdfghjklzxcvbnm'))
bibra = []



for stroka in data_1:
    count_1 = 0
    count_1 = len(stroka)
    one.append(count_1)
    new_stroka = stroka[1:-1]
    data_2.append(new_stroka)



for i in range(len(bebra)):
    c = '\\x' + bebra[i][0] +  bebra[i][1]
    bibra.append(c)

    

for stroka in data_2:
    stroka = stroka.replace("\\\\","%")
    stroka = stroka.replace('\\"',"%")
    for i in bibra:
        if i in stroka:
            stroka = stroka.replace(i,"%")
    count_2 = 0
    count_2 = len(stroka)
    two.append(count_2)

s = 0



for i in range(len(one)):
    s += one[i] - two[i]
            


f2.write(str(s))
f2.close
f1.close
