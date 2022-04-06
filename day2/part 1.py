import re



f1 = open("input.txt", "r")
f2 = open("output1.txt", "w")
a = f1.read()
data = re.split('\n|x',a)
S=0



for i in range(0, len(data) ,3):
    S1 = int(data[i])*int(data[i+1])
    S2 = int(data[i+1])*int(data[i+2])
    S3 = int(data[i+2])*int(data[i])
    min_S = min(S1,S2,S3)
    S+=2*(S1+S2+S3)+min_S



f2.write(str(S))
f2.close
f1.close

    
    
    







