f1 = open("input.txt", "r")
f2 = open("output1.txt", "w")
a = f1.read()



def text(a):
    count = 1
    b = ''
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            count = count + 1
        else:
            b += str(count) + str(a[i])
            count = 1
    return b



for i in range(40):
    a += 'h'
    a = text(a)

    
            
f2.write(str(len(a)))
f2.close
f1.close
