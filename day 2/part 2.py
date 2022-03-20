import re



f1 = open("input.txt", "r")
f2 = open("output2.txt", "w")
a = f1.read()
data = re.split('\n|x',a)
lenta=0



for i in range(0, len(data) ,3):
    P1 = (int(data[i])+int(data[i+1]))*2
    P2 = (int(data[i+1])+int(data[i+2]))*2
    P3 = (int(data[i+2])+int(data[i]))*2
    V = int(data[i])*int(data[i+1])*int(data[i+2])
    lenta += int(min(P1,P2,P3))+V



f2.write(str(lenta))
f2.close
f1.close

    
    
    







