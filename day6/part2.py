import re

f1 = open("input.txt", "r")
f2 = open("output2.txt", "w")
a = f1.read()



data_1 = []
data_2 = []
data_3 = []
count = 0
c = 0




for x in range (0,1000):
    for y in range (0,1000):
        data_1.append([x, y, 0])



data_2 = re.split('\n',a)




for i in range(len(data_2)):
    babra =  re.split('\s|,',data_2[i])
    if babra[0] == 'turn':
        x1 = int(babra[2])
        y1 = int(babra[3])
        x2 = int(babra[5])
        y2 = int(babra[6])
        for x in range(x1, x2+1):
            for y in range (y1, y2+1):
                if babra[1] == 'on':
                    data_1[x*1000+y][2] += 1
                else:
                    data_1[x*1000+y][2] -= 1
                    if data_1[x*1000+y][2] < 0:
                        data_1[x*1000+y][2] = 0
    else:
        x1 = int(babra[1])
        y1 = int(babra[2])
        x2 = int(babra[4])
        y2 = int(babra[5])
        for x in range(x1, x2+1):
            for y in range (y1, y2+1):
                data_1[x*1000+y][2] += 2



for i in data_1:
    c += i[2]



f2.write(str(c))
f2.close
f1.close
