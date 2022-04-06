import hashlib



f1 = open("input.txt", "r")
f2 = open("output1.txt", "w")
a = f1.read()


for i in range(0,1000000):
    hash_object = a+str(i)
    hash_object = hash_object.encode('utf-8')
    hash_object = hashlib.md5(hash_object)
    hash_object = hash_object.hexdigest()
    if hash_object[0:5]=="00000":
        break



f2.write(str(i))
f2.close
f1.close
